from odoo import fields,models,api
from odoo.exceptions import ValidationError,UserError

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital appointment'
    _inherit =['mail.thread']
    _rec_name='patient_id'

    sequence_id=fields.Char(string="Reference Id", default=lambda self: self._get_default_sequence(),readonly=True)
    patient_id=fields.Many2one('hospital.patient',string='Patient')
    date_appointment=fields.Date(string='Appointment',required=True)
    end_date_appointment=fields.Date(string='End date',required=True)
    note=fields.Text(string='Note')
    note_checkbox=fields.Boolean(string="Is Note",default=False, readonly=True)
    note_book=fields.Char(string="Note Book",readonly=True)


    @api.model
    def _get_default_sequence(self):
        return self.env['ir.sequence'].next_by_code('hospital.appointment')
    
    @api.constrains('note')
    def _constrainonnote(self):
       if self.note:
        if len(self.note.strip())>10:
            raise ValidationError("Length of the note should not be greater than 10")
    
    @api.onchange('note')
    def _onchange_of_note(self):
     if not self.patient_id and self.note:
            raise UserError('Please select a patient before proceeding.')
     if self.note:
        if len(self.note.strip())>0:
            self.note_checkbox=True
            self.note_book="Has Values"
     else:        
            self.note_checkbox=False
            self.note_book=""            
    
    
    def write(self,vals):
        for rec in self:
            print(rec.end_date_appointment,'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        return super(HospitalAppointment,self).write(vals)
