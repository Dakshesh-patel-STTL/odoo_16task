from odoo import fields,models,api
from odoo.exceptions import ValidationError

class Inheritedemployees(models.Model):
    _inherit='silvertouch.employees'
    _description='Inherited employees'

    address=fields.Text(string="Address",required=True)   
    birth_date=fields.Date(string='D.O.B',required=True)
    joining_date=fields.Date(string='Joining Date',required=True)
    department=fields.Many2one('silvertouch.departments',string='Department')
    hobbies=fields.One2many('silvertouch.employees.hobbies','employee_id',string='Hobbies')
    notes=fields.Text(string='Note')
    


    @api.onchange('joining_date')
    def _calculate_totalyears(self):
        super(Inheritedemployees,self)._calculate_totalyears()

        for rec in self:
            if rec.total_years>5:
                rec.status='Old employee'
            else:
                rec.status='Fresher'
    
    @api.constrains('fname','lname')
    def _check_length(self):
        for rec in self:
            if len(rec.fname)<=2 or len(rec.lname)<=2:
                raise ValidationError('length of first name and last name must be greater than 2')
            