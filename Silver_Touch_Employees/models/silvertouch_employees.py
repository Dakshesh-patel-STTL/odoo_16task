from odoo import fields, models, api
import datetime
from odoo.exceptions import ValidationError

class Silvertouchemployees(models.Model):
    _name = 'silvertouch.employees'
    _description = 'Contains info of Silvertouch employees'
    _inherit = ['mail.thread', 'mail.activity.mixin'] 

    fname = fields.Char(string='First Name', required=True, track_visibility='onchange')
    lname = fields.Char(string="Last Name", required=True, track_visibility='onchange')
    address = fields.Text(string="Address", track_visibility='onchange')
    total_years = fields.Integer(string='Years in STTL', readonly=True, track_visibility='onchange')
    status = fields.Char(string='Employee Status', readonly=True, track_visibility='onchange')
    joining_date = fields.Date(string='Joining Date', required=True, track_visibility='onchange')

    @api.onchange('joining_date')
    def _calculate_totalyears(self):
        for rec in self:
            if rec.joining_date:
                rec.total_years = datetime.date.today().year - rec.joining_date.year

    @api.constrains('fname', 'lname')
    def _check_length(self):
        for rec in self:
            if len(rec.fname) < 2:
                raise ValidationError('Length of first name must be greater than 2')

