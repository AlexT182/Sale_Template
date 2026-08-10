from odoo import models


class IrUiView(models.Model):
    _inherit = "ir.ui.view"

    def save_embedded_field(self, el):
        """Fix Odoo 19 html_editor bug: prevent TypeError when data-oe-type is None."""
        if el is not None and hasattr(el, "get"):
            if el.get("data-oe-model") and not el.get("data-oe-type"):
                el.set("data-oe-type", "char")
        return super().save_embedded_field(el)
