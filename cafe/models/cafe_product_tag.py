from odoo import fields,api,models

class ProductTags(models.Model):
    _name = 'cafe.product.tags'
    _description = 'contains info of product tags'
    _rec_name = 'name'

    name=fields.Char(string='Tag Name',required=True)
    color = fields.Integer('Color', help='Color in HEX format', required=True)