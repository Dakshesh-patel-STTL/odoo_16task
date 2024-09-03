from odoo import fields, models,api
import datetime
class SilvertouchEmployee(models.Model):
    _name = 'silvertouch.employee'
    _description = 'Silvertouch Employee'
    _inherits = {'silvertouch.employees': 'template_id'}

    template_id = fields.Many2one('silvertouch.employees', required=True, ondelete='cascade')
       
    department = fields.Char(string='Department')
    job_position = fields.Char(string='Job Position')


