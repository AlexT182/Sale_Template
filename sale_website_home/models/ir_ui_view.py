from odoo import models
import logging

_logger = logging.getLogger(__name__)


class IrUiView(models.Model):
    _inherit = "ir.ui.view"

    def save(self, value, xpath=None):
        """Fix Odoo 19 html_editor XML syntax error when saving snippet image / icon / text edits."""
        if isinstance(value, str):
            value_stripped = value.strip()
            if value_stripped and not value_stripped.startswith("<"):
                if value_stripped.startswith(("http", "/web/image", "/web/static", "data:image", "blob:")):
                    value = f'<img src="{value_stripped}" class="img-fluid hero-media-img"/>'
                else:
                    value = f"<div>{value_stripped}</div>"
        try:
            return super().save(value, xpath=xpath)
        except Exception as e:
            err_msg = str(e)
            if "Start tag expected" in err_msg or "<string>" in err_msg:
                _logger.warning("Caught XMLSyntaxError in view save, retrying with wrapped payload: %s", e)
                try:
                    return super().save(f"<div>{value}</div>", xpath=xpath)
                except Exception:
                    return super().save(f"<div>{value}</div>")
            raise

    def save_embedded_field(self, el):
        """Fix Odoo 19 html_editor bug: prevent TypeError when data-oe-type is None."""
        if el is not None and hasattr(el, "get"):
            if el.get("data-oe-model") and not el.get("data-oe-type"):
                el.set("data-oe-type", "char")
        return super().save_embedded_field(el)
