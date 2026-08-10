from odoo import http, _
from odoo.http import request


class SaleWebsiteController(http.Controller):
    """Public website endpoints used by the Sale Website homepage."""

    @http.route(
        "/sale/contact/submit",
        type="http",
        auth="public",
        website=True,
        methods=["POST"],
        csrf=True,
    )
    def submit_contact(self, **post):
        # Honeypot: normal visitors never fill this field.
        if (post.get("website_url") or "").strip():
            return request.redirect("/?contact=success#contact")

        def clean(value, max_length):
            return (value or "").strip()[:max_length]

        company_name = clean(post.get("company_name") or post.get("name"), 160)
        contact_name = clean(post.get("contact_name") or post.get("name"), 160)
        email = clean(post.get("email"), 254)
        phone = clean(post.get("phone"), 64)
        message = clean(post.get("message") or post.get("description"), 4000)

        if not contact_name or not phone:
            return request.redirect("/contactus?contact=invalid")

        lead_name = _("Sale website B2B inquiry - %s") % (
            company_name or contact_name
        )

        request.env["crm.lead"].sudo().create(
            {
                "name": lead_name,
                "type": "lead",
                "partner_name": company_name,
                "contact_name": contact_name,
                "email_from": email,
                "phone": phone,
                "description": message,
                "website": request.httprequest.host_url,
            }
        )
        return request.redirect("/contactus-thank-you")

    @http.route(
        "/sale/get_toasts",
        type="json",
        auth="public",
        website=True,
        methods=["POST"],
        csrf=False,
    )
    def get_sales_toasts(self):
        """Dynamic JSON endpoint returning sales toast notifications configured from Odoo Backend UI."""
        toast_recs = request.env["sale.toast.notification"].sudo().search(
            [("active", "=", True)], order="sequence asc, id desc", limit=20
        )

        products = request.env["product.template"].sudo().search(
            [("website_published", "=", True)], limit=10
        )

        results = []
        if toast_recs:
            for idx, t in enumerate(toast_recs):
                prod = t.product_id or (products[idx % len(products)] if products else None)
                prod_name = prod.name if prod else "Sản Phẩm CCVI Export"
                img_url = f"/web/image/product.template/{prod.id}/image_128" if prod else "/logo.png"
                results.append({
                    "name": t.name,
                    "text": f"{t.action_text} <strong>{prod_name}</strong>",
                    "time": t.time_text,
                    "image": img_url,
                })
        elif products:
            buyers = [
                ("Anh Minh (TP.HCM)", "vừa gửi yêu cầu báo giá sỉ", "2 phút trước"),
                ("Chị Thu Hà (Hà Nội)", "vừa đặt mua 100 thùng", "5 phút trước"),
                ("Công ty Nông Sản Á Châu", "vừa đăng ký đại lý phân phối", "12 phút trước"),
                ("Anh Hoàng (Bình Dương)", "vừa ký hợp đồng cung ứng B2B", "18 phút trước"),
                ("Chị Thanh Vân (Đà Nẵng)", "vừa yêu cầu bảng giá xuất khẩu", "25 phút trước"),
            ]
            for idx, p in enumerate(products):
                buyer_name, buyer_action, buyer_time = buyers[idx % len(buyers)]
                img_url = f"/web/image/product.template/{p.id}/image_128"
                results.append({
                    "name": buyer_name,
                    "text": f"{buyer_action} <strong>{p.name}</strong>",
                    "time": buyer_time,
                    "image": img_url,
                })
        else:
            results = [
                {"name": "Anh Minh (TP.HCM)", "text": "vừa gửi yêu cầu báo giá sỉ <strong>Cà Phê Robusta</strong>", "time": "2 phút trước", "image": "/logo.png"},
                {"name": "Chị Thu Hà (Hà Nội)", "text": "vừa đặt mua 100 thùng <strong>Xoài Sấy Dẻo Export</strong>", "time": "5 phút trước", "image": "/logo.png"},
            ]

        return results
