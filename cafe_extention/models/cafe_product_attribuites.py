from odoo import fields,models

class CafeProductAttribuites(models.Model):
    _name = 'cafe.product.attribuites'
    _description = 'model.technical.name'

    attribuite=fields.Many2one('cafe.product.attribuite',string="Attribuite")
    attribuite_values=fields.Many2many('cafe.product.attribuite.values',string="Attribuite Values")
    product_id = fields.Many2one('cafe.product',string="Product")

    