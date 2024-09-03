from odoo import fields,models

class Inheritedorderlines(models.Model):
    _inherit='cafe.orderline'
    _name='cafe.orderline'
    _description='inherited cafe orderline'

    discount_amount=fields.Integer(string='Discount')
    