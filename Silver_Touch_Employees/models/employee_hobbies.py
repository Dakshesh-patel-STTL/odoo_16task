from odoo import fields,models

class Employeeshobbies(models.Model):
    _name = 'silvertouch.employees.hobbies'
    _description = 'contains silvertouch.employees.hobbies'
    
    employee_id=fields.Many2one('silvertouch.employees',ondelete='cascade')
    hobbies_name=fields.Char(string='Hobbies',required=True)