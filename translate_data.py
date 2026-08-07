import json
import time
import sys
from deep_translator import GoogleTranslator

# Force UTF-8 stdout
sys.stdout.reconfigure(encoding='utf-8')

translator = GoogleTranslator(source='vi', target='en')
cache = {}

def translate_text(text):
    if not text:
        return ""
    if text in cache:
        return cache[text]
    
    try:
        translated = translator.translate(text)
        cache[text] = translated
        return translated
    except Exception as e:
        time.sleep(1) # Simple backoff
        try:
            translated = translator.translate(text)
            cache[text] = translated
            return translated
        except:
            return text

# Load VI data
with open("cleaned_products_vi.json", "r", encoding="utf-8") as f:
    vi_records = json.load(f)

en_records = []

print("Starting translation...")
for i, record in enumerate(vi_records):
    if i % 10 == 0:
        print(f"Translating product {i+1}/{len(vi_records)}...")
        
    en_records.append({
        "category": translate_text(record["category"]),
        "product_name": translate_text(record["product_name"]),
        "features": translate_text(record["features"]),
        "inner_pack": translate_text(record["inner_pack"]),
        "outer_pack": translate_text(record["outer_pack"])
    })

# Save EN data
with open("cleaned_products_en.json", "w", encoding="utf-8") as f:
    json.dump(en_records, f, ensure_ascii=False, indent=4)

# Generate Markdown
with open("All_Products_Review.md", "w", encoding="utf-8") as f:
    f.write("# DANH SÁCH TOÀN BỘ SẢN PHẨM ĐÃ CHUẨN HÓA (VI & EN)\n\n")
    
    for i in range(len(vi_records)):
        vi = vi_records[i]
        en = en_records[i]
        
        f.write(f"## SẢN PHẨM {i+1}\n")
        f.write("**[TIẾNG VIỆT]**\n")
        f.write(f"- **Danh mục:** {vi['category']}\n")
        f.write(f"- **Tên sản phẩm:** {vi['product_name']}\n")
        f.write(f"- **Đặc tính:** {vi['features']}\n")
        f.write(f"- **Bao bì (Trong/Ngoài):** {vi['inner_pack']} / {vi['outer_pack']}\n\n")
        
        f.write("**[TIẾNG ANH]**\n")
        f.write(f"- **Category:** {en['category']}\n")
        f.write(f"- **Product Name:** {en['product_name']}\n")
        f.write(f"- **Features:** {en['features']}\n")
        f.write(f"- **Packaging (Inner/Outer):** {en['inner_pack']} / {en['outer_pack']}\n\n")
        
        f.write("---\n\n")

print("Finished generating All_Products_Review.md")
