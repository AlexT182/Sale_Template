# 🚀 SALE TEMPLATE — HE THONG BAN HANG & ERP DOANH NGHIEP (ODOO 19 COMMUNITY)

[![Odoo 19](https://img.shields.io/badge/Odoo-19.0%20Community-8f8f8f.svg)](https://www.odoo.com/)
[![License LGPL--3](https://img.shields.io/badge/License-LGPL--3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0.en.html)
[![QA Audit Status](https://img.shields.io/badge/QA%20Audit-11%2F11%20Passed%20(100%25)-success.svg)](https://saledemo.ccvi.com.vn)

Hệ thống tích hợp toàn diện **Website Bán Hàng B2B, Thương Mại Điện Tử, Quản Lý Kho và CRM Chăm Sóc Khách Hàng Tự Động** xây dựng trên nền tảng **Odoo 19 Community Edition**.

- **Production Live Site**: [https://saledemo.ccvi.com.vn](https://saledemo.ccvi.com.vn)
- **Admin CMS Login**: [https://saledemo.ccvi.com.vn/web/login](https://saledemo.ccvi.com.vn/web/login) (`admin` / `Ccvi@123#`)
- **GitHub Repository**: [AlexT182/Sale_Template](https://github.com/AlexT182/Sale_Template.git)

---

## 📚 BỘ TÀI LIỆU DỰ ÁN (PROJECT DOCUMENTATION)

Toàn bộ tài liệu kỹ thuật, sơ đồ wireframe, nhật ký nâng cấp và hướng dẫn bàn giao đã được tập trung trong thư mục **[`docs/`](file:///D:/Project/QQ/Sale_template/docs)**:

| File Tài Liệu | Nội Dung / Mục Đích | Người Sử Dụng |
| :--- | :--- | :--- |
| 📋 **[`docs/HANDOVER.md`](file:///D:/Project/QQ/Sale_template/docs/HANDOVER.md)** | **Hồ Sơ Bàn Giao Dự Án & Hướng Dẫn Kỹ Thuật Developer** | Lập trình viên tiếp nhận |
| 📘 **[`docs/USER_GUIDE.md`](file:///D:/Project/QQ/Sale_template/docs/USER_GUIDE.md)** | **Hướng Dẫn Tùy Biến Giao Diện & Quản Trị Website (No-Code)** | Admin / Quản trị viên |
| 🎨 **[`docs/wireframe.md`](file:///D:/Project/QQ/Sale_template/docs/wireframe.md)** | **Sơ Đồ Kiến Trúc Giao Diện & Triết Lý Thiết Kế UX/UI** | UI/UX Designer / Dev |
| 📝 **[`docs/SESSION_LOG.md`](file:///D:/Project/QQ/Sale_template/docs/SESSION_LOG.md)** | **Nhật Ký Phiên Làm Việc, Lịch Sử Vá Lỗi & Audit Log** | Tech Lead / Project Manager |
| 📦 **[`docs/All_Products_Review.md`](file:///D:/Project/QQ/Sale_template/docs/All_Products_Review.md)** | **Danh Sách Toàn Bộ 53 Sản Phẩm Đã Chuẩn Hóa VI & EN** | Nội dung / Sản phẩm |

---

## 🎨 BỘ NHẬN DIỆN THƯƠNG HIỆU (BRAND PALETTE)

- 🔴 **CCVI Red (Chủ đạo)**: `#e84336` — Nút bấm CTA, Badge HOT, Highlight giá sỉ VNĐ.
- 🔵 **CCVI Blue (Điểm nhấn)**: `#2563eb` — Subtitle, Badge danh mục, Icon tính năng.
- 🟢 **CCVI Green (Thành công)**: `#31a853` — Chứng nhận VietGAP, ISO, Trạng thái.
- ⬛ **Dark Slate (Nền Hero & Footer)**: `#0f172a` / `#1e293b` — Gradient cao cấp.

---

## 📁 CẤU TRÚC MÃ NGUỒN REPOSITORY

```text
Sale_Template/
├── docs/                               # Thư mục tài liệu kỹ thuật & bàn giao
│   ├── HANDOVER.md                     # Tài liệu bàn giao dành cho Lập trình viên
│   ├── USER_GUIDE.md                   # Hướng dẫn tùy biến No-Code cho Admin
│   ├── wireframe.md                    # Sơ đồ thiết kế Wireframe ASCII Layouts
│   ├── SESSION_LOG.md                  # Nhật ký phiên làm việc & vá lỗi
│   └── All_Products_Review.md          # Danh sách sản phẩm chuẩn hóa
├── sale_website_home/                  # Module Odoo tùy biến chính (Presentation Layer)
│   ├── __manifest__.py                 # Phụ thuộc: website, website_sale, crm
│   ├── __init__.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── main.py                     # Route /sale/contact/submit & /sale/get_toasts
│   ├── models/
│   │   ├── __init__.py
│   │   └── ir_ui_view.py               # Bộ vá lỗi Core Odoo 19 HTML Editor
│   ├── views/
│   │   ├── layout.xml                  # Header, Topbar, Footer & Toast JS
│   │   ├── homepage.xml                # Native HTML Sections Trang Chủ
│   │   └── pages.xml                   # Override /about-us & /contactus
│   ├── i18n/
│   │   └── vi_VN.po                    # Gói dịch ngôn ngữ Tiếng Việt chuẩn
│   └── static/
│       └── src/
│           ├── img/ccvi_logo.png       # Logo thương hiệu CCVI Technology
│           └── css/style.css           # CSS tùy chỉnh màu sắc & UI
├── README.md                           # File này
└── docker-compose.yml                  # Khởi chạy Odoo 19 + Postgres 16 Local
```

---

## 🚀 HƯỚNG DẪN KHỞI ĐỘNG DÀNH CHO DEVELOPER

### 1. Clone Repository
```bash
git clone https://github.com/AlexT182/Sale_Template.git
cd Sale_Template
```

### 2. Khởi Động Local Bằng Docker (Tuỳ chọn)
```bash
docker-compose up -d
```

### 3. Cấu Hình Toast Notification Mua Hàng
Xem hướng dẫn chi tiết tại [`docs/HANDOVER.md`](file:///D:/Project/QQ/Sale_template/docs/HANDOVER.md#31-cấu-hình-toast-notification-mua-hàng-social-proof-popup) để thay đổi danh sách kịch bản `buyers` trong `sale_website_home/controllers/main.py`.

---

© 2026 **CCVI Technology JSC**. All Rights Reserved.
