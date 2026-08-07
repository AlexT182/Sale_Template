from odoo import http, _
from odoo.http import request


class ElyWorldWebsiteController(http.Controller):
    """Public website endpoints used by the ElyWorld homepage."""

    @http.route(
        "/elyworld/contact/submit",
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

        company_name = clean(post.get("company_name"), 160)
        contact_name = clean(post.get("contact_name"), 160)
        email = clean(post.get("email"), 254)
        phone = clean(post.get("phone"), 64)
        message = clean(post.get("message"), 4000)

        if not contact_name or not email or "@" not in email:
            return request.redirect("/?contact=invalid#contact")

        lead_name = _("ElyWorld website inquiry - %s") % (
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
        return request.redirect("/?contact=success#contact")
