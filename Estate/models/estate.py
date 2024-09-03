from odoo import models, fields

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    value = fields.Float(string='Value')
    selling_price = fields.Float(string='Selling Price')
    active = fields.Boolean(string='Active', default=True)
    image = fields.Binary(string='User Image')
    buyer_id = fields.Many2one('estate.buyer', string='Buyer')
