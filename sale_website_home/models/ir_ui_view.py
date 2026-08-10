from odoo import models
import logging

_logger = logging.getLogger(__name__)


class IrUiView(models.Model):
    _inherit = "ir.ui.view"

    def save_embedded_field(self, el):
        """Fix Odoo 19 html_editor bug: prevent KeyError: None and TypeError when data-oe-model or data-oe-type is missing."""
        if el is not None and hasattr(el, "get"):
            model_name = el.get("data-oe-model")
            if model_name and model_name in self.env:
                if not el.get("data-oe-type"):
                    el.set("data-oe-type", "char")
                return super().save_embedded_field(el)
            elif el.get("data-oe-field"):
                return True
        return super().save_embedded_field(el)
