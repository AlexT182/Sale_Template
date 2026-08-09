# 🎨 Sơ Đồ Kiến Trúc Giao Diện, Wireframe & Triết Lý UX/UI Sale Demo

---

## 📌 1. Tổng Quan Hệ Thống Giao Diện (Design System & Color Psychology)

### 🎨 1.1 Bộ Bảng Màu & Tâm Lý Học Thiết Kế B2B
- **Primary Color (`#0d6efd` - Deep Royal Blue)**: 
  - *Mục đích*: Tạo sự tin tưởng tuyệt đối, tính chính trực và chuyên nghiệp của một doanh nghiệp cung ứng B2B quy mô lớn.
- **Dark Mode Background (`#0f172a` - Slate Dark)**:
  - *Mục đích*: Tăng chiều sâu thị giác ở Topbar, Hero Overlay và Footer, tạo cảm giác sang trọng và tập trung ánh nhìn vào các khối nội dung trắng giữa trang.
- **Light Surface (`#f8fafc` - Soft Snow White)**:
  - *Mục đích*: Làm nền cho sản phẩm nông sản / cà phê, giúp hình ảnh nổi bật 100% không bị chi phối bởi màu sắc tương phản gắt.
- **Accent Color (`#ff4757` - Vibrant Coral Red)**:
  - *Mục đích*: Dùng cho các nút báo giá gấp, badge *"🔥 HOT"* và icon số điện thoại để kích thích hành động (Call To Action).

### ✒️ 1.2 Typography & Quy Tắc Tỷ Lệ Vàng Về Độ Tương Phản (WCAG 2.1)
- **Font Tiêu đề**: `'Outfit', sans-serif` (Bo tròn hiện đại, mạnh mẽ).
- **Font Văn bản**: `'Inter', sans-serif` (Sắc nét, chuẩn đọc hiểu trên mọi màn hình di động/desktop).
- **Độ tương phản (Contrast Ratio)**: Mọi chữ trên trang chủ & footer đều tuân thủ độ tương phản **4.5:1 đến 18:1** (Đã loại bỏ hoàn toàn chữ xám đục mờ).

---

## 🏛️ 2. Wireframe Chi Tiết & Triết Lý UX Bố Trí Cấu Trúc Các Trang

---

### 🏠 2.1 Trang Chủ (Homepage `/`)

#### 📐 ASCII Layout Structure Diagram:
```
+-----------------------------------------------------------------------------------+
| 🕒 TOPBAR: Giờ làm việc | 📞 Hotline | ✉️ Email | 🌐 VI/EN Language Switcher      |
+-----------------------------------------------------------------------------------+
| 🧭 HEADER: [Logo Sale Demo]  [Trang chủ | Sản phẩm ▾ | Giới thiệu | Liên hệ]        |
|                              [🔍 Tìm kiếm] [🛒 Giỏ hàng] [👤 User] [🚀 Báo Giá B2B] |
+-----------------------------------------------------------------------------------+
| 🚀 HERO SECTION (Dark Blue Gradient / Ambient Media Video)                        |
| +-----------------------------------------+ +-----------------------------------+ |
| | - Badge: Solution B2B                   | | 💳 HERO CARD (Solid White Card)   | |
| | - Title: Nâng Tầm Thương Hiệu B2B       | | - Icon: 📊 Growth Chart         | |
| | - Subtitle: Hệ thống tự động CRM        | | - Title: Tối Ưu 300% Chuyển Đổi  | |
| | - Action: [🛒 Khám Phá] [🚀 Nhận Báo Giá]| | - Desc: Tải dưới 1s, CRM Odoo     | |
| +-----------------------------------------+ | - Action: [Tư Vấn Trực Tiếp]      | |
|                                             +-----------------------------------+ |
+-----------------------------------------------------------------------------------+
| 📦 BLOCK 2: DYNAMIC PRODUCT CATEGORIES (Light Gray Background)                    |
| Header: "Danh mục sản phẩm" -> "Khám Phá Danh Mục Nông Sản B2B"                   |
| Grid 4 Cột: [Nông Sản Sấy]   [Cà Phê Robusta]   [Hạt Điều]   [Combo B2B]          |
| (Mỗi Card: Icon 3D + Tên Danh mục + Button "Xem ngay ➔")                           |
+-----------------------------------------------------------------------------------+
| 🔥 BLOCK 3: FEATURED PRODUCTS GRID (White Background)                              |
| Header: "Sản phẩm bán chạy" -> "Sản Phẩm Xuất Khẩu Tiêu Biểu" [Xem Tất Cả ➔]       |
| Grid 4 Cột Sản Phẩm:                                                              |
| +------------------+ +------------------+ +------------------+ +------------------+ |
| | [Badge HOT]      | | [Badge HOT]      | | [Badge HOT]      | | [Badge HOT]      | |
| | [Ảnh Sản Phẩm]   | | [Ảnh Sản Phẩm]   | | [Ảnh Sản Phẩm]   | | [Ảnh Sản Phẩm]   | |
| | - Tên sản phẩm   | | - Tên sản phẩm   | | - Tên sản phẩm   | | - Tên sản phẩm   | |
| | - Giá: 125.000đ  | | - Giá: 240.000đ  | | - Giá: 165.000đ  | | - Giá: 210.000đ  | |
| | - [🛒 Thêm Giỏ]  | | - [🛒 Thêm Giỏ]  | | - [🛒 Thêm Giỏ]  | | - [🛒 Thêm Giỏ]  | |
| +------------------+ +------------------+ +------------------+ +------------------+ |
+-----------------------------------------------------------------------------------+
| 🛡️ BLOCK 4: CAPACITY & CERTIFICATIONS (Light Gray Background)                     |
| Left Column: Shield Icon + Text "Chứng Nhận Quốc Tế HACCP, ISO 22000, VietGAP, FDA" |
| Right Column: "Năng Lực Cung Ứng & Xuất Khẩu Toàn Cầu" + 2 Tích chọn Nguồn Hàng    |
+-----------------------------------------------------------------------------------+
| 📩 BLOCK 5: FAST LEAD CAPTURE FORM (Blue Gradient Container)                      |
| Left Column: "Yêu Cầu Báo Giá Xuất Khẩu / Bán Sỉ" + Stat (1500+ Đơn B2B, 99.8% OK)|
| Right Column: Form [Họ tên] [SĐT] [Email] [Nội dung yêu cầu] -> [🚀 Gửi Báo Giá]  |
+-----------------------------------------------------------------------------------+
| 💬 FLOATING WIDGETS (Bottom Overlay):                                             |
| [Left: 🛒 Sales Toast Notification]             [Right: 📞 Zalo/Phone/Quote Floating]|
+-----------------------------------------------------------------------------------+
| ⚓ FOOTER: [Logo + Slogan] | [Về Chúng Tôi] | [Sản Phẩm] | [Liên Hệ] | © 2026      |
+-----------------------------------------------------------------------------------+
```

#### 🎯 UX Rationale (Vì sao lại sắp xếp Layout Trang chủ như vậy?):
1. **Hero Section đặt đầu tiên**: 
   - *Lý do*: Khách hàng B2B truy cập website chỉ dành 3 giây đầu tiên để xác định *"Doanh nghiệp này làm gì & có đáng tin không?"*. Tiêu đề rõ ràng + Khối Hero Card trắng nổi bật giúp truyền tải ngay lập tức giá trị cốt lõi.
2. **Danh mục sản phẩm (Block 2) đặt ngay sau Hero**:
   - *Lý do*: Giúp phân loại luồng nhu cầu người mua (Nông sản, Cà phê hay Hạt điều), giảm tỷ lệ thoát trang (Bounce Rate).
3. **Sản phẩm xuất khẩu tiêu biểu (Block 3) đặt ở trung tâm**:
   - *Lý do*: Đưa sản phẩm thực tế kèm giá niêm yết minh bạch ra mặt tiền, kích thích hành động bỏ giỏ hàng hoặc bấm xem chi tiết ngay.
4. **Chứng nhận năng lực (Block 4)**:
   - *Lý do*: Khách hàng mua buôn / mua xuất khẩu luôn lo ngại rủi ro chất lượng. Khối chứng nhận ISO/HACCP/FDA đóng vai trò giải tỏa tâm lý nghi ngờ (Trust Building).
5. **Form đăng ký báo giá (Block 5) ở cuối cùng**:
   - *Lý do*: Điểm chốt hạ hành trình trải nghiệm người dùng (Conversion Point). Sau khi đã xem qua năng lực, danh mục và sản phẩm, khách hàng sẵn sàng điền form báo giá 15 phút.

---

### 🛍️ 2.2 Trang Cửa Hàng & Danh Mục Sản Phẩm (`/shop`)

#### 📐 ASCII Layout Structure Diagram:
```
+-----------------------------------------------------------------------------------+
| TOPBAR & HEADER NAV                                                               |
+-----------------------------------------------------------------------------------+
| BREADCRUMB: Trang chủ / Cửa Hàng / Danh Mục Nông Sản                             |
+-----------------------------------------------------------------------------------+
| LEFT SIDEBAR (Bộ Lọc Taxonomy - 25% Width)| MAIN PRODUCT GRID (75% Width)         |
| +---------------------------------------+ | Header: Hiển thị 8 sản phẩm [Sắp xếp ▾]|
| | 🔍 TÌM KIẾM SẢN PHẨM                  | | Grid 3 Cột:                           |
| | [Input search...                   ]  | | +-------------+ +-------------+       |
| |                                       | | | [Ảnh]       | | [Ảnh]       |       |
| | 📁 DANH MỤC CÔNG KHAI                 | | | Tên SP      | | Tên SP      |       |
| |  [x] Tất cả sản phẩm                  | | | Giá VNĐ     | | Giá VNĐ     |       |
| |  [ ] Nông sản & Trái cây sấy          | | | [🛒 Bỏ Giỏ] | | [🛒 Bỏ Giỏ] |       |
| |  [ ] Cà phê & Đồ uống                 | | +-------------+ +-------------+       |
| |  [ ] Hạt dinh dưỡng & Gia vị          | |                                       |
| |                                       | | PAGINATION: [1] [2] [Next ➔]          |
| | 💰 KHOẢNG GIÁ                         | |                                       |
| | [Slider 100k - 1,000k              ]  | |                                       |
| +---------------------------------------+ +---------------------------------------+
+-----------------------------------------------------------------------------------+
| FOOTER                                                                            |
+-----------------------------------------------------------------------------------+
```

#### 🎯 UX Rationale (Mục đích layout `/shop`):
- **Cấu trúc Sidebar Trái + Grid Phải**: Là chuẩn mực e-Commerce kinh điển (Golden Standard). Dễ dàng cho người mua sỉ lọc danh mục và khoảng giá mà không mất phương hướng.
- **Sắp xếp theo thứ tự ưu tiên**: Ô tìm kiếm đặt trên cùng Sidebar giúp khách có mã sản phẩm tìm thấy kết quả chỉ trong 1s.

---

### 📦 2.3 Trang Chi Tiết Sản Phẩm (`/shop/product/<id>`)

#### 📐 ASCII Layout Structure Diagram:
```
+-----------------------------------------------------------------------------------+
| HEADER NAV                                                                        |
+-----------------------------------------------------------------------------------+
| LEFT GALLERY (50% Width)                 | RIGHT PRODUCT ACTION BOX (50% Width)   |
| +--------------------------------------+ | - Badge: Nông Sản Sấy Export           |
| | [ Ảnh Sản Phẩm Chính HD - 400px ]    | | - Title: XOÀI SẤY DẺO EXPORT PREMIUM   |
| |                                      | | - Rating: ⭐⭐⭐⭐⭐ (4.9/5 - 48 đánh giá) |
| | [Thumbnail 1] [Thumbnail 2] [Thumb 3]| | - Price: 125.000 đ / Gói 500g          |
| +--------------------------------------+ | - Mô tả ngắn B2B: Chuẩn xuất khẩu EU...|
|                                          | - Số lượng: [-] [ 1 ] [+]              |
|                                          | - Buttons:                             |
|                                          |   [ 🛒 THÊM VÀO GIỎ HÀNG (Primary) ]   |
|                                          |   [ 🚀 YÊU CẦU BÁO GIÁ SỈ (Red CTA) ]  |
|                                          | - Cam kết: 🚚 Giao toàn quốc | 🛡️ ISO  |
+-----------------------------------------------------------------------------------+
| TABS NỘI DUNG CHI TIẾT (Below Grid):                                              |
| [ Thẻ 1: Mô Tả Kỹ Thuật ]  [ Thẻ 2: Tiêu Chuẩn Xuất Khẩu ]  [ Thẻ 3: Đánh Giá ]    |
| - Độ ẩm: <15% | Hạn sử dụng: 12 tháng | Quy cách đóng thùng: 20kg/thùng.           |
+-----------------------------------------------------------------------------------+
| FOOTER                                                                            |
+-----------------------------------------------------------------------------------+
```

#### 🎯 UX Rationale (Mục đích layout Chi tiết Sản phẩm):
- **Khối mua hàng & Báo giá sỉ đặt sát tầm mắt (Right Sticky Column)**: Người dùng không cần cuộn trang vẫn nhìn thấy ngay Giá, Nút Mua và Nút Báo Giá Sỉ.
- **Phân tách Tabs kỹ thuật bên dưới**: Giúp trang chi tiết gọn gàng, khách muốn xem sâu chỉ số độ ẩm hay chứng nhận chỉ cần chuyển tab.

---

## 🛠️ 3. Wireframe & Cấu Trúc Backend Admin CMS (`/web`)

```
+-----------------------------------------------------------------------------------+
| ODOO BACKEND TOPBAR: [Logo CCVI ERP]  [Search Apps...]  [💬 Messages] [👤 Admin]  |
+-----------------------------------------------------------------------------------+
| APPS DASHBOARD MAIN (Modern App Switcher Icons):                                  |
|  [ 🌐 Website ]    [ 🎯 CRM ]    [ 🛍️ Sales ]    [ 📦 Inventory ]  [ 🧾 Invoicing ] |
|  (Quản lý Web)     (Quản lý Lead)(Đơn hàng B2B)  (Quản lý Kho)    (Thu tiền/Thẻ)  |
+-----------------------------------------------------------------------------------+
| KPI METRICS SUMMARY DASHBOARD (Khi truy cập CRM/Sales):                           |
| +------------------+ +------------------+ +------------------+ +------------------+ |
| | 📈 DOANH SỐ      | | 📑 LEAD BÁO GIÁ  | | 📦 TỒN KHO CANH  | | 🛒 ĐƠN HÀNG MỚI  | |
| | 1.250.000.000 đ  | | 48 Yêu cầu mới   | | 12 Mặt hàng      | | 15 Đơn chờ duyệt| |
+------------------+ +------------------+ +------------------+ +------------------+ |
+-----------------------------------------------------------------------------------+
```

#### 🎯 UX Rationale (Mục đích layout Backend Admin):
- **Tập trung vào 5 Ứng dụng Cốt lõi**: Đã tinh gọn bảng điều khiển Odoo ERP để nhân viên không bị rối mắt bởi hàng chục module phụ.
- **Tự động hóa hoàn toàn Lead từ Website**: Mọi thông tin khách điền form báo giá từ Frontend lập tức đẩy thẳng về App CRM Backend với trạng thái *"Cần xử lý gấp trong 15 phút"*.
