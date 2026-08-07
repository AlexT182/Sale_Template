import xmlrpc.client
import base64
import json
import os
import re
from unidecode import unidecode

def slugify(text):
    text = unidecode(text).lower()
    return re.sub(r'[\W_]+', '-', text).strip('-')

def main():
    url = "https://ely-world.ccvi.com.vn"
    db = "odoo"
    username = "admin"
    api_key = "693c960fe86d4212a3522973f880eeb76c602238"

    print("Đang kết nối đến Odoo (https://ely-world.ccvi.com.vn) ...")
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    uid = common.authenticate(db, username, api_key, {})
    if not uid:
        print("Lỗi: Xác thực thất bại.")
        return

    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

    internal_cat_cache = {}
    public_cat_cache = {}

    def get_or_create_internal_category(name_vi, name_en):
        if name_vi in internal_cat_cache:
            return internal_cat_cache[name_vi]
            
        # Tìm bằng name_en vì tài khoản API đang ở ngôn ngữ base là Tiếng Anh
        cat_ids = models.execute_kw(db, uid, api_key, 'product.category', 'search', [[['name', '=', name_en]]])
        if cat_ids:
            cat_id = cat_ids[0]
        else:
            cat_id = models.execute_kw(db, uid, api_key, 'product.category', 'create', [{'name': name_en}])
            models.execute_kw(db, uid, api_key, 'product.category', 'write', [[cat_id], {'name': name_vi}], {'context': {'lang': 'vi_VN'}})
            models.execute_kw(db, uid, api_key, 'product.category', 'write', [[cat_id], {'name': name_en}], {'context': {'lang': 'en_US'}})
            
        internal_cat_cache[name_vi] = cat_id
        return cat_id

    def get_or_create_public_category(name_vi, name_en):
        if name_vi in public_cat_cache:
            return public_cat_cache[name_vi]
            
        cat_ids = models.execute_kw(db, uid, api_key, 'product.public.category', 'search', [[['name', '=', name_en]]])
        if cat_ids:
            cat_id = cat_ids[0]
        else:
            cat_id = models.execute_kw(db, uid, api_key, 'product.public.category', 'create', [{'name': name_en}])
            models.execute_kw(db, uid, api_key, 'product.public.category', 'write', [[cat_id], {'name': name_vi}], {'context': {'lang': 'vi_VN'}})
            models.execute_kw(db, uid, api_key, 'product.public.category', 'write', [[cat_id], {'name': name_en}], {'context': {'lang': 'en_US'}})
            
        public_cat_cache[name_vi] = cat_id
        return cat_id

    # Đọc dữ liệu JSON VI và EN
    with open('cleaned_products_vi.json', 'r', encoding='utf-8') as f:
        products_vi = json.load(f)
    with open('cleaned_products_en.json', 'r', encoding='utf-8') as f:
        products_en = json.load(f)

    img_dir = "product_images"
    print("\nBắt đầu đẩy TOÀN BỘ 136 sản phẩm lên Odoo...")
    
    for idx, (p_vi, p_en) in enumerate(zip(products_vi, products_en)):
        name_vi = p_vi.get('product_name', '')
        if not name_vi: continue
        
        category_name_vi = p_vi.get('category', 'SẢN PHẨM KHÁC').capitalize()
        category_name_en = p_en.get('category', 'OTHER PRODUCTS').capitalize()
            
        # 1. Tạo hoặc lấy Danh mục nội bộ (Internal Category)
        internal_cat_id = get_or_create_internal_category(category_name_vi, category_name_en)
        
        # 2. Tạo hoặc lấy Danh mục Website (eCommerce Category)
        public_cat_id = get_or_create_public_category(category_name_vi, category_name_en)
        
        # Lấy Tên Tiếng Anh
        name_en = p_en.get('product_name', name_vi)
        
        # Dữ liệu mô tả Text (cho trường description_sale - trường này dịch thuật bình thường)
        desc_vi = f"Đặc điểm: {p_vi.get('features', '')}\nĐóng gói (trong): {p_vi.get('inner_pack', '')}\nĐóng gói (ngoài): {p_vi.get('outer_pack', '')}"
        desc_en = f"Features: {p_en.get('features', '')}\nInner pack: {p_en.get('inner_pack', '')}\nOuter pack: {p_en.get('outer_pack', '')}"
        
        # Tạo nội dung Song ngữ cho HTML (Vì Odoo chặn dịch ngoài cho trường HTML)
        desc_html_bilingual = f"""
        <div class="container mt-3">
            <p><strong>Đặc điểm / Features:</strong><br/>
            🇻🇳 {p_vi.get('features', '')}<br/>
            🇺🇸 {p_en.get('features', '')}</p>
            
            <p><strong>Đóng gói trong / Inner pack:</strong><br/>
            🇻🇳 {p_vi.get('inner_pack', '')}<br/>
            🇺🇸 {p_en.get('inner_pack', '')}</p>
            
            <p><strong>Đóng gói ngoài / Outer pack:</strong><br/>
            🇻🇳 {p_vi.get('outer_pack', '')}<br/>
            🇺🇸 {p_en.get('outer_pack', '')}</p>
        </div>
        """
        
        # Đọc hình ảnh đã gen
        slug_name = slugify(name_vi)
        filename = f"{idx+1:03d}_{slug_name}.jpg"
        filepath = os.path.join(img_dir, filename)
        
        image_base64 = False
        if os.path.exists(filepath):
            with open(filepath, "rb") as image_file:
                image_base64 = base64.b64encode(image_file.read()).decode('utf-8')
        
        # Cực kỳ quan trọng: Tìm sản phẩm bằng Tên tiếng Anh (Ngôn ngữ base) VÀ phải thuộc đúng danh mục hiện tại
        existing_product_ids = models.execute_kw(
            db, uid, api_key, 'product.template', 'search', 
            [[['name', '=', name_en], ['categ_id', '=', internal_cat_id]]]
        )
        
        # Values cơ sở (Tiếng Anh)
        vals_base = {
            'name': name_en,
            'categ_id': internal_cat_id,
            'public_categ_ids': [(6, 0, [public_cat_id])],
            'description_sale': desc_en,
            'description_ecommerce': desc_html_bilingual, # Ép dùng song ngữ
            'type': 'consu',
            'is_published': True,
        }
        if image_base64:
            vals_base['image_1920'] = image_base64
            
        # Values Tiếng Việt (Chỉ dịch Tên và Mô tả Text)
        vals_vi = {
            'name': name_vi,
            'description_sale': desc_vi,
        }
        
        try:
            prod_id = False
            # Bước 1: Tạo/Cập nhật bản Record gốc
            if existing_product_ids:
                prod_id = existing_product_ids[0]
                models.execute_kw(db, uid, api_key, 'product.template', 'write', [[prod_id], vals_base])
                print(f"[{idx+1}/1] Đã CẬP NHẬT bản gốc: {name_en}")
            else:
                prod_id = models.execute_kw(db, uid, api_key, 'product.template', 'create', [vals_base])
                print(f"[{idx+1}/1] Đã TẠO MỚI bản gốc: {name_en}")
                
            # Bước 2: Ghi bản dịch Tiếng Việt (dùng context, chỉ áp dụng được cho trường Text/Char)
            models.execute_kw(db, uid, api_key, 'product.template', 'write', [[prod_id], vals_vi], {'context': {'lang': 'vi_VN'}})
            
            # Bước 3: Xác nhận lại Tiếng Anh
            models.execute_kw(db, uid, api_key, 'product.template', 'write', [[prod_id], {'name': name_en, 'description_sale': desc_en}], {'context': {'lang': 'en_US'}})
            
            print(f"   -> Đã xử lý xong!")
                
        except Exception as e:
            print(f"[{idx+1}/1] Lỗi khi xử lý '{name_vi}': {e}")

    print("\nHoàn tất test 1 sản phẩm! Hãy kiểm tra lại Danh mục trên web Odoo.")

if __name__ == '__main__':
    main()
