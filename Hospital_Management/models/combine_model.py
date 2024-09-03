from odoo import fields,models

class Combinemodel(models.Model):
    _name = 'combine.model'
    _inherit=['hospital.patient','hospital.appointment']
    _description = 'Combine model'

    state=fields.Selection([('default','Default'),('completed','Completed')])
    
    
