from odoo import models, fields


class SaleToastNotification(models.Model):
    _name = "sale.toast.notification"
    _description = "Sales Toast Notification Popup"
    _order = "sequence asc, id desc"

    name = fields.Char(string="Tên Khách Hàng / Địa Phương", required=True, default="Chị Thu Hà (Hà Nội)")
    action_text = fields.Char(string="Hành Động Mua Hàng", required=True, default="vừa đặt mua 100 thùng")
    time_text = fields.Char(string="Thời Gian Hiển Thị", required=True, default="5 phút trước")
    product_id = fields.Many2one("product.template", string="Sản Phẩm Tương Ứng (Tùy Chọn)")
    sequence = fields.Integer(string="Thứ Tự", default=10)
    active = fields.Boolean(string="Kích Hoạt", default=True)
