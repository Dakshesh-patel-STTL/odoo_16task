# -*- coding: utf-8 -*-
from odoo import fields, models, api


class TaxLines(models.Model):
    _name = 'cafe.taxline'
    _description = 'Tax Lines'
    _rec_name = 'id'
    sale_id = fields.Many2one('cafe.sales', 'Sale Id')
    tax_id = fields.Many2one('product.taxes', 'Tax', required=True)
    base_price = fields.Float('Base Price', required=True)
    percentage = fields.Float('Percentage')
    tax_amount = fields.Float('Tax Amount')

    @api.depends('base_price', 'percentage')
    def _compute_tax_amount(self):
        for record in self:
            record.tax_amount = (record.base_price * record.percentage) / 100
