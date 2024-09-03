from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    cafe_sales_customer = fields.Boolean(string='Customer in Cafe Sales', compute='_compute_cafe_sales_customer')

    def _compute_cafe_sales_customer(self):
        sales_customers = self.env['cafe.sales'].search([]).mapped('customer_id')
        for partner in self:
            partner.cafe_sales_customer = partner.id in sales_customers.ids
