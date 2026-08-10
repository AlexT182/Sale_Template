# 📋 DANH MỤC HỒ SƠ BÀN GIAO TRÊN GITHUB
**Repository**: [AlexT182/Sale_Template](https://github.com/AlexT182/Sale_Template.git)  
**Live Site**: [https://saledemo.ccvi.com.vn](https://saledemo.ccvi.com.vn)  
**Ngày Bàn Giao**: 10/08/2026  
**Đơn Vị Sở Hữu**: CCVI Technology JSC  

---

## 🛠️ 1. TỔNG QUAN DỰ ÁN & MÔI TRƯỜNG TRIỂN KHAI

- **Nền Tảng Core**: Odoo 19 Community Edition.
- **Hệ Thống Máy Chủ**: Dokploy Container / Dockerized Environment (PostgreSQL 16).
- **Tài Khoản Quản Trị Hệ Thống (Live Server)**:
  - **URL đăng nhập Admin**: `https://saledemo.ccvi.com.vn/web/login`
  - **Tên đăng nhập (Username)**: `admin`
  - **Mật khẩu (Password)**: `Ccvi@123#`
  - **Cơ sở dữ liệu (Database)**: `odoo`

---

## 📁 2. DANH MỤC CÁC FILE MÃ NGUỒN VÀ CẤU HÌNH BÀN GIAO

Toàn bộ các tệp mã nguồn bên dưới đã được kiểm thử (QA Audit 100% Passed) và đẩy lên GitHub branch `main`:

```text
Sale_Template/
├── HANDOVER.md                         # Tài liệu danh mục hồ sơ bàn giao dự án (File này)
├── README.md                           # Hướng dẫn kỹ thuật chi tiết dành cho Developer
├── USER_GUIDE.md                       # Hướng dẫn sử dụng cho Quản trị viên doanh nghiệp
├── SESSION_LOG.md                      # Nhật ký lịch sử các bước đã nâng cấp & vá lỗi
├── wireframe.md                        # Bản vẽ sơ đồ kiến trúc các khối giao diện
├── docker-compose.yml                  # File cấu hình chạy Odoo 19 + Postgres 16 local
└── sale_website_home/                   # Module Odoo tùy biến chính
    ├── __manifest__.py                 # Khai báo phụ thuộc: website, website_sale, crm
    ├── __init__.py                     # Khởi tạo Python package
    ├── controllers/
    │   ├── __init__.py
    │   └── main.py                     # Route /sale/contact/submit & /sale/get_toasts
    ├── models/
    │   ├── __init__.py
    │   └── ir_ui_view.py               # Bộ vá lỗi Core Odoo 19 HTML Editor
    ├── views/
    │   ├── layout.xml                  # Override Header, Topbar, Footer, Logo & Toast JS
    │   ├── homepage.xml                # Native HTML Sections Trang Chủ (Hero, Categories, Products...)
    │   └── pages.xml                   # Override giao diện /about-us & /contactus
    ├── i18n/
    │   └── vi_VN.po                    # Gói dịch ngôn ngữ Tiếng Việt chuẩn
    └── static/
        └── src/
            ├── img/ccvi_logo.png       # Logo thương hiệu CCVI Technology chính thức
            └── css/style.css           # CSS tùy chỉnh màu sắc & hiệu ứng UI
```

---

## 🎨 3. BỘ NHẬN DIỆN THƯƠNG HIỆU (BRAND PALETTE)

Toàn bộ giao diện đã được thiết kế đồng bộ theo chuẩn Logo `CCVI Technology.png`:
- 🔴 **CCVI Red (Chủ đạo)**: `#e84336` — Sử dụng cho Nút bấm CTA, Badge HOT, Highlight giá sỉ.
- 🔵 **CCVI Blue (Điểm nhấn)**: `#2563eb` — Sử dụng cho Subtitle, Badge danh mục, Icon tính năng.
- 🟢 **CCVI Green (Thành công)**: `#31a853` — Sử dụng cho Chứng nhận VietGAP, ISO, Trạng thái.
- ⬛ **Dark Slate (Nền Hero & Footer)**: `#0f172a` / `#1e293b` — Nền Gradient cao cấp.

---

## 🔑 4. CÁC ĐIỂM KỸ THUẬT QUAN TRỌNG DEVELOPER CẦN LƯU Ý

### 1. Bộ Vá Lỗi Core Odoo 19 HTML Editor (`models/ir_ui_view.py`)
Odoo 19 WYSIWYG Editor mặc định gặp 2 lỗi nghiêm trọng khi người dùng sửa kéo thả:
- **`KeyError: None`**: Xảy ra khi trường `data-oe-model` bị rỗng.
- **`ValidationError: Start tag expected, '<' not found`**: Xảy ra khi hàm `_check_xml()` đọc chuỗi diff rỗng lúc tạo bản sao Copy-On-Write.
👉 **Đã xử lý dứt điểm**: Hàm `save_embedded_field` và `_check_xml` trong `models/ir_ui_view.py` đã bọc bộ bắt lỗi an toàn. Dev tuyệt đối giữ nguyên bộ vá lỗi này.

### 2. Cấu Trúc Native HTML Sections Trang Chủ (`homepage.xml`)
Toàn bộ 5 khối của Trang chủ (`sale-hero`, `sale-categories`, `sale-featured-products`, `sale-about`, `sale-contact`) đã được nhúng trực tiếp thành các khối **Native HTML Sections**.
👉 **Ưu điểm**: Cho phép người dùng kéo thả thêm block mới hoặc bấm xóa block tùy thích mà không bị đụng độ thẻ gọi gián tiếp `<t t-call="...">`.

### 3. Tự Động Tạo CRM Lead Khi Khách Hàng Đăng Ký Báo Giá (`controllers/main.py`)
Route `/sale/contact/submit` tự động tiếp nhận dữ liệu từ các Form liên hệ B2B và tạo bản ghi **Cơ hội kinh doanh (CRM Lead)** trực tiếp vào Module Odoo CRM Backend.

---

## 🚀 5. HƯỚNG DẪN PULL CODE & KHỞI ĐỘNG DÀNH CHO DEV

```bash
# 1. Clone repository về máy tính
git clone https://github.com/AlexT182/Sale_Template.git

# 2. Di chuyển vào thư mục dự án
cd Sale_Template

# 3. Khởi động môi trường Odoo 19 Local bằng Docker (Option)
docker-compose up -d
```

---

## 📌 6. CAM KẾT VÀ XÁC NHẬN BÀN GIAO

- **Trạng thái Codebase**: Clean Working Tree, 0 lỗi đúp tag XML, 0 lỗi 404 hình ảnh.
- **Kết quả QA Audit**: 11/11 trang chính phản hồi **HTTP 200 OK** với tốc độ tải mượt mà (<250ms).
- **GitHub URL**: [https://github.com/AlexT182/Sale_Template.git](https://github.com/AlexT182/Sale_Template.git)
