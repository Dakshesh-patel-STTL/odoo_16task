# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductTax(models.Model):
    _name = 'product.taxes'
    _description = 'Taxes on Product'
    _rec_name = 'tax_name'
    tax_name = fields.Char('Tax Name', required=True)
    tax_code = fields.Char('Tax Code', required=True)
    tax_percentage = fields.Float('Tax Percentage', required=True)