from odoo import models, fields

class Buyer(models.Model):
    _name = 'estate.buyer'
    _description = 'Contains buyers info'

    name = fields.Char(string='Buyer Name', required=True)
    property_ids = fields.One2many('estate.property', 'buyer_id', string='Properties')
