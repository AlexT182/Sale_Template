# 🚀 CCVI Technology — Sale Demo ERP & Website Module (Odoo 19)

Dự án giao diện **Website Bán Hàng & ERP Doanh Nghiệp CCVI Technology** được xây dựng và tùy biến cho **Odoo 19 Community Edition**. Module chính `sale_website_home` tích hợp giao diện hiện đại chuẩn UX/UI, đa ngôn ngữ (Tiếng Việt & Tiếng Anh), đồng bộ dữ liệu Lead/Yêu cầu báo giá tự động về CRM Odoo Backend.

---

## 🛠️ 1. Công Nghệ & Môi Trường Triển Khai

- **Nền tảng**: Odoo 19 Community Edition (Docker / Dokploy Container).
- **Domain Live Demo**: [https://saledemo.ccvi.com.vn](https://saledemo.ccvi.com.vn)
- **Tài khoản Admin Backend**:
  - **Username**: `admin`
  - **Password**: `Ccvi@123#`
  - **Database**: `odoo`

---

## 🎨 2. Bộ Nhận Diện Thương Hiệu CCVI Brand Palette

Toàn bộ các trang và giao diện đã được chuẩn hóa theo đúng bảng màu Logo `CCVI Technology.png`:

- 🔴 **CCVI Red (Chủ đạo)**: `#e84336` (Nút bấm CTA, Badge HOT, Highlight giá, Accent card)
- 🔵 **CCVI Blue (Phụ)**: `#2563eb` / `#517bbd` (Badge danh mục, Subtitle, Icon)
- 🟢 **CCVI Green (Thành công)**: `#31a853` (Badge VietGAP, ISO, Trạng thái đơn)
- ⬛ **Dark Slate (Nền Hero & Footer)**: `#0f172a` / `#1e293b` (Gradient nền cao cấp)

---

## 📁 3. Cấu Trúc Mã Nguồn Dự Án (Repository Structure)

```text
Sale_Template/
├── sale_website_home/                   # Module Odoo chính
│   ├── __manifest__.py                 # Khai báo Module (depends: website, website_sale, crm)
│   ├── __init__.py                     # Import controllers & models
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── main.py                     # Route /sale/contact/submit (Đồng bộ Lead CRM & Toast)
│   ├── models/
│   │   ├── __init__.py
│   │   └── ir_ui_view.py               # Vá lỗi Odoo 19 html_editor (KeyError None & XML syntax)
│   ├── views/
│   │   ├── layout.xml                  # Override Header, Topbar, Footer, Brand Logo & Toast JS
│   │   ├── homepage.xml                # Native HTML Snippets & Homepage layout override
│   │   └── pages.xml                   # Giao diện /about-us & /contactus chuẩn CCVI Red
│   ├── i18n/
│   │   └── vi_VN.po                    # Gói dịch Tiếng Việt cho module
│   └── static/
│       └── src/
│           ├── img/ccvi_logo.png       # Logo chính thức CCVI Technology
│           └── css/style.css           # CSS tùy chỉnh thương hiệu & hiệu ứng animation
├── docker-compose.yml                  # File cấu hình chạy Odoo 19 + PostgreSQL 16
├── USER_GUIDE.md                       # Hướng dẫn sử dụng chi tiết cho người quản trị
├── SESSION_LOG.md                      # Nhật ký các bước đã nâng cấp & tối ưu
├── wireframe.md                        # Kiến trúc thiết kế các khối giao diện
└── README.md                           # Tài liệu bàn giao dành cho Developer (File này)
```

---

## ⚡ 4. Các Điểm Kỹ Thuật Nổi Bật & Bộ Vá Lỗi Core (Important Developer Notes)

### 🔑 A. Bộ Vá Lỗi Odoo 19 HTML Editor Backend (`ir_ui_view.py`)
Khi kéo thả hoặc sửa đổi Snippet trong Odoo 19 WYSIWYG Editor, Odoo Core có 2 lỗi nguy hiểm:
1. `KeyError: None`: Do thuộc tính `data-oe-model` trả về `None` khi gọi `self.env[None]`.
2. `ValidationError: Start tag expected, '<' not found`: Phát sinh khi hàm `_check_xml()` đọc chuỗi diff rỗng trong lúc tạo bản sao COW (Copy-On-Write).

👉 **Cách xử lý**: Module `sale_website_home/models/ir_ui_view.py` đã kế thừa và bọc bảo vệ cả 2 hàm `save_embedded_field` và `_check_xml`. Ngăn chặn hoàn toàn lỗi sụp server khi kéo thả/thêm/xóa Snippet!

### 🛒 B. Đồng Bộ Yêu Cầu Báo Giá B2B Về CRM Backend (`main.py`)
- Route `/sale/contact/submit`: Tiếp nhận dữ liệu Form liên hệ từ Trang chủ và Trang `/contactus`.
- Tự động tạo bản ghi **Cơ hội kinh doanh (CRM Lead)** trong Odoo CRM với các trường: `name`, `phone`, `email`, `description`, `type='lead'`.

### 🌐 C. Đa Ngôn Ngữ Dịch Tự Động (Multi-Language Menu)
- Menu Header được nạp động từ `website.menu`.
- Cả 2 bản **Tiếng Việt (`vi_VN`)** và **Tiếng Anh (`en_US`)** đã được cập nhật bản dịch `update_field_translations` tương ứng (Sản phẩm ➔ Products, Giới thiệu ➔ About Us...).

---

## 🚀 5. Hướng Dẫn Dành Cho Dev Khi Pull Code Về Local

### Bước 1: Clone Repository
```bash
git clone https://github.com/AlexT182/Sale_Template.git
cd Sale_Template
```

### Bước 2: Khởi Động Bằng Docker (Nếu chạy Local)
```bash
docker-compose up -d
```
Sau đó truy cập `http://localhost:8069`, vào **Apps (Ứng dụng)** ➔ Tìm `sale_website_home` ➔ Bấm **Install (Cài đặt)** hoặc **Upgrade (Nâng cấp)**.

### Bước 3: Deploy Lên Dokploy / VPS Server
Chỉ cần đẩy code lên branch `main` của GitHub [AlexT182/Sale_Template](https://github.com/AlexT182/Sale_Template.git), Dokploy sẽ tự động trigger Webhook pull code và restart container.

---

## 📝 6. Hỗ Trợ Kỹ Thuật & Liên Hệ

- **GitHub Repository**: [https://github.com/AlexT182/Sale_Template.git](https://github.com/AlexT182/Sale_Template.git)
- **Maintainer**: CCVI Technology JSC
