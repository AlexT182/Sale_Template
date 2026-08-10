from odoo import models
import logging

_logger = logging.getLogger(__name__)


class IrUiView(models.Model):
    _inherit = "ir.ui.view"

    def save(self, value, xpath=None):
        """Fix Odoo 19 html_editor XML syntax error when saving snippet icon / text edits."""
        if isinstance(value, str):
            value_stripped = value.strip()
            if value_stripped and not value_stripped.startswith("<"):
                value = f"<div>{value_stripped}</div>"
        return super().save(value, xpath=xpath)

    def save_embedded_field(self, el):
        """Fix Odoo 19 html_editor bug: prevent TypeError when data-oe-type is None."""
        if el is not None and hasattr(el, "get"):
            if el.get("data-oe-model") and not el.get("data-oe-type"):
                el.set("data-oe-type", "char")
        return super().save_embedded_field(el)
