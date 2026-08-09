# 🎨 Sơ Đồ Kiến Trúc Giao Diện & Wireframe Website Sale Demo (UX/UI Standard)

## 📌 1. Tổng Quan Hệ Thống Giao Diện (UX/UI Design System)

### 🎨 1.1 Palette Màu Sắc Thương Hiệu (Brand Palette)
- **Primary Color**: `#0d6efd` (Deep Royal Blue) - Thể hiện tính chuyên nghiệp, tin cậy B2B.
- **Secondary Color**: `#0b5ed7` (Navy Accent) - Tăng độ tương phản cho button & badge.
- **Accent Color**: `#ff4757` (Vibrant Coral Red) - Nổi bật cho nút *"Báo Giá B2B"*, Badge *"🔥 HOT"*.
- **Dark Mode Background**: `#0f172a` (Slate Dark) - Dùng cho Topbar, Hero Overlay & Footer.
- **Light Surface**: `#f8fafc` (Soft Snow White) - Nền trang nhã tôn vinh hình ảnh nông sản & sản phẩm.
- **Text Primary**: `#1e293b` - Chữ đậm dễ đọc chuẩn Accessibility WCAG 2.1.

### ✒️ 1.2 Typography & Grid System
- **Font-Family**: `'Outfit', 'Inter', -apple-system, sans-serif`.
- **Grid Layout**: Bootstrap 5 Responsive Grid (12 Columns, Container Max-Width 1320px).
- **Border Radius**: Cards `1rem` (16px), Buttons `50rem` (Pill Shapes), Modals `1.25rem`.

### ✨ 1.3 Hiệu Ứng Động & Micro-Animations
1. **Hero Video Ambient Banner**: Video nền lặp mượt phủ lớp mờ Glassmorphism (`backdrop-filter: blur(12px)`).
2. **Hover Lift & Zoom**: Thẻ sản phẩm nổi nhẹ `translateY(-6px)` kèm hiệu ứng zoom ảnh nhẹ.
3. **CTA Shine Effect**: Ánh kim luân chuyển trên các nút CTA báo giá chính.
4. **Sales Toast Notification**: Thẻ thông báo chốt đơn thời gian thực góc trái dưới màn hình.
5. **Floating Action Bar**: Bộ ba nút Zalo / Hotline / Báo giá góc phải màn hình với hiệu ứng mạch đập (`pulse`).
6. **Mobile Sticky CTA**: Thanh hành động cố định chân màn hình di động cho trải nghiệm mua sắm 1-touch.

---

## 🏛️ 2. Structure & Wireframe Các Trang Frontend

```
+-----------------------------------------------------------------------------------+
| TOPBAR: 🕒 T2 - T7: 08:00 - 18:00  |  📞 Hotline  |  ✉️ Email  | 🌐 VI/EN Selector|
+-----------------------------------------------------------------------------------+
| HEADER: [LOGO Sale Demo]   [ Trang chủ | Sản phẩm (Dropdown) | Giới thiệu | Tin tức ]|
|                            [🔍 Search]  [🛒 Cart (Badge)]  [👤 User]  [🚀 Báo Giá] |
+-----------------------------------------------------------------------------------+
```

### 🏠 2.1 Trang Chủ (Homepage `/`)
- **Block 1: Hero Video Banner**:
  - Video ambient nền nông sản / cà phê / xưởng đóng gói xuất khẩu.
  - Tiêu đề nổi bật: *"Nâng Tầm Thương Hiệu Bán Hàng & Xuất Khẩu B2B"*.
  - Thẻ Glassmorphism hiển thị KPI *"Tối Ưu 300% Tỷ Lệ Chuyển Đổi"*.
- **Block 2: Dynamic Category Carousel / Grid**:
  - Tự động quét từ `product.public.category`.
  - Hiệu ứng Hover Lift 3D & nút *"Xem ngay"*.
- **Block 3: Featured Products Grid**:
  - Tự động quét từ `product.template` (Top 8 sản phẩm bán chạy).
  - Giá bán định dạng VNĐ, Badge *"HOT"*, Nút thêm giỏ hàng nhanh.
- **Block 4: Company Capacity & Quality Badges**:
  - Các chứng nhận chất lượng: HACCP, ISO 22000, VietGAP, FDA.
- **Block 5: Fast Lead Capture Form**:
  - Form nhận bảng giá sỉ B2B đẩy trực tiếp về CRM Odoo Backend.

### 🛍️ 2.2 Trang Cửa Hàng & Danh Mục (`/shop`)
- **Sidebar Filter**:
  - Bộ lọc theo Danh mục công khai (`product.public.category`).
  - Bộ lọc khoảng giá & Từ khóa tìm kiếm.
- **Product Main Grid**:
  - Phân trang chuẩn UX (Grid 3-4 cột).
  - Tải động hình ảnh sản phẩm từ Odoo DB.

### 📝 2.3 Trang Chi Tiết Sản Phẩm (`/shop/product/<id>`)
- **Left Column**: Gallery ảnh sản phẩm sắc nét, nút Zoom full-size.
- **Right Column**: Tên sản phẩm, Mã SKU, Giá niêm yết, Mô tả ngắn B2B, Nút *"Thêm vào giỏ hàng"* & *"Yêu cầu báo giá sỉ lượng lớn"*.
- **Bottom Tabs**: Thông số kỹ thuật sản phẩm, Chứng nhận & Đánh giá khách hàng.

### 🏢 2.4 Trang Giới Thiệu (`/about-us`)
- **Section Mission & Vision**: Tầm nhìn trở thành nhà cung ứng nông sản hàng đầu.
- **Interactive Timeline**: Lịch sử phát triển & Cột mốc doanh nghiệp.
- **Core Values**: 4 Trụ cột giá trị cốt lõi.

### 📞 2.5 Trang Liên Hệ & Yêu Cầu Báo Giá (`/contactus`)
- **Form Báo Giá Chuyên Nghiệp**: Tên, Số điện thoại, Email, Công ty, Danh mục quan tâm & Số lượng dự kiến.
- **Embedded Google Map & Chi tiết Chi nhánh**: Trụ sở chính & Nhà máy sản xuất.

---

## 🛠️ 3. Structure & Wireframe Backend Admin CMS (`/web`)

```
+-----------------------------------------------------------------------------------+
| ODOO BACKEND HEADER: [LOGO CCVI / Sale Demo]  [Search Apps...]  [🔔] [👤 Admin]   |
+-----------------------------------------------------------------------------------+
| DASHBOARD MAIN:                                                                   |
| [ 📊 DOANH SỐ BÁN HÀNG ] [ 📑 LEAD MỚI TỪ WEBSITE ] [ 📦 CẢNH BÁO TỒN KHO ]       |
+-----------------------------------------------------------------------------------+
| APPS DASHBOARD:                                                                   |
|  [ 🌐 Website ]    [ 🎯 CRM ]    [ 🛍️ Sales ]    [ 📦 Inventory ]  [ 🧾 Invoicing ] |
+-----------------------------------------------------------------------------------+
```

### ⚙️ 3.1 Màn Hình Đăng Nhập CMS (`/web/login`)
- Phủ màu Gradient thương hiệu chuyên nghiệp.
- Card Đăng nhập căn giữa thiết kế bo tròn mượt mà, chứa Logo Sale Demo & slogan *"Hệ Thống Quản Trị Doanh Nghiệp Toàn Diện"*.

### 📊 3.2 Màn Hình Tổng Quan Administration (`/web`)
- **Icon App Switcher**: Các icon được thiết kế lại nổi bật với màu sắc phân biệt từng phân hệ.
- **Thanh Navigation Bar Topbar**: Hiển thị tên doanh nghiệp *"Sale Demo - CCVI ERP"*, bộ công cụ tìm kiếm nhanh & thông báo.
- **Tích hợp Tự động hóa CRM**: Mọi Yêu cầu báo giá gửi từ Frontend lập tức biến thành Lead trong App CRM Backend.
