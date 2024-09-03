from odoo import fields, models, api

class DelegateSales(models.Model):
    _name = 'cafe.extended.delegate.sales'
    _description = 'Extended Sales with Product Variants'
    _inherits = {'cafe.sales': 'sales_id'}  

    sales_id = fields.Many2one('cafe.sales', ondelete="cascade", string="Related Sales Order")
    order_lines_ids = fields.One2many('cafe.extended.delegate.orderline', 'extended_sale_id', string='Order Lines')
     
     
     