from odoo import fields, models

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    aadhar_no = fields.Char(string='Aadhar No')
