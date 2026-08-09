/** @odoo-module **/

import publicWidget from '@web/legacy/js/public/public_widget';

publicWidget.registry.SaleWebsiteInteractive = publicWidget.Widget.extend({
    selector: '.ew-homepage, .sale-site-header',
    
    start: function () {
        this._super.apply(this, arguments);
        this._initScrollToTop();
        this._initSalesToast();
        this._initFloatingContact();
    },

    _initScrollToTop: function () {
        const scrollTopBtn = document.querySelector('.js_sale_scroll_top');
        if (scrollTopBtn) {
            scrollTopBtn.addEventListener('click', function () {
                window.scrollTo({ top: 0, behavior: 'smooth' });
            });
        }
    },

    _initSalesToast: function () {
        if (document.querySelector('.sale-toast-notification')) return;

        const toasts = [
            { name: "Anh Minh (TP.HCM)", text: "vừa gửi yêu cầu báo giá 500kg Cà phê Robusta Honey", time: "2 phút trước" },
            { name: "Chị Thu Hà (Hà Nội)", text: "vừa đặt mua 100 hộp Xoài Sấy Dẻo Export", time: "5 phút trước" },
            { name: "Công ty Nông Sản Á Châu", text: "vừa đăng ký đại lý phân phối Hạt Điều Bội Thu", time: "12 phút trước" },
            { name: "Anh Hoàng (Bình Dương)", text: "vừa yêu cầu bảng giá sỉ Hạt Macca Úc B2B", time: "18 phút trước" }
        ];

        let index = 0;
        const toastContainer = document.createElement('div');
        toastContainer.className = 'sale-toast-notification d-none d-md-flex align-items-center gap-3';
        document.body.appendChild(toastContainer);

        const showToast = () => {
            const item = toasts[index];
            toastContainer.innerHTML = `
                <div class="toast-icon bg-primary bg-opacity-10 text-primary rounded-circle p-2 d-flex align-items-center justify-content-center" style="width: 42px; height: 42px; flex-shrink: 0;">
                    <i class="fa fa-shopping-bag fs-5"></i>
                </div>
                <div class="toast-body flex-grow-1">
                    <div class="d-flex justify-content-between align-items-center mb-1">
                        <strong class="fs-7 text-dark">${item.name}</strong>
                        <span class="badge bg-light text-secondary fs-8">${item.time}</span>
                    </div>
                    <p class="mb-0 fs-8 text-secondary lh-sm">${item.text}</p>
                </div>
                <button type="button" class="btn-close btn-close-toast fs-8 ms-1" aria-label="Close"></button>
            `;

            toastContainer.style.display = 'flex';
            toastContainer.style.opacity = '1';

            const closeBtn = toastContainer.querySelector('.btn-close-toast');
            if (closeBtn) {
                closeBtn.addEventListener('click', () => {
                    toastContainer.style.opacity = '0';
                    setTimeout(() => { toastContainer.style.display = 'none'; }, 400);
                });
            }

            index = (index + 1) % toasts.length;
        };

        // Delay initial toast display by 3s, then rotate every 10s
        setTimeout(showToast, 3000);
        setInterval(showToast, 10000);
    },

    _initFloatingContact: function () {
        if (document.querySelector('.sale-floating-contact')) return;

        const floatContainer = document.createElement('div');
        floatContainer.className = 'sale-floating-contact d-none d-sm-flex';
        floatContainer.innerHTML = `
            <a href="https://zalo.me" target="_blank" class="btn-floating btn-zalo" title="Chat Zalo ngay">
                <i class="fa fa-comments"></i>
            </a>
            <a href="tel:0901234567" class="btn-floating btn-phone" title="Gọi Hotline: 090 123 4567">
                <i class="fa fa-phone"></i>
            </a>
            <a href="/contactus" class="btn-floating btn-quote" title="Yêu cầu Báo Giá">
                <i class="fa fa-paper-plane"></i>
            </a>
        `;
        document.body.appendChild(floatContainer);
    }
});

export default publicWidget.registry.SaleWebsiteInteractive;
