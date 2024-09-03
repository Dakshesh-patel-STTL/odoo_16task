from odoo import fields,models

class ProductAttribuiteValues(models.Model):
    _name = 'cafe.product.attribuite.values'
    _description = 'cafe product attribuite values'

    name=fields.Char(string="Name",required=True)
    cost=fields.Float(string="Cost",required=True)