from odoo import fields,models,api

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'stores data of hospital patient'
    _inherit =['mail.thread'] 
    # _rec_name="name"
 
    additional_info = fields.Char(string='Additional Info')  
    name=fields.Char(string='Name',tracking=True)
    date_of_birth=fields.Date(string='DOB',required=True)
    gender=fields.Selection([('Male','male'),('Female','female'),('Others','others')],string='Gender',required=True)

    _sql_constraints = [      
        ('unique_name_dob', 'UNIQUE(name, date_of_birth)', 'The combination of name and date of birth must be unique.'),


        ('check_gender_value', 'CHECK(gender IN (\'Male\', \'Female\', \'Others\'))', 'Gender must be either Male, Female, or Others.')
    ]
    def name_get(self):
        result=[]
        for patient in self:
            display_name=f'[{patient.name}] {patient.date_of_birth}'
            result.append((patient.id,display_name))
        return result
    

    @api.model
    def name_create(self, name):        
        if '|' in name:
            name, additional_info = name.split('|', 1)
        else:
            name, additional_info = name, '' 
        new_record = self.create({
            'name': name,
            'additional_info': additional_info,
            'date_of_birth': fields.Date.today(),         
        })
        return new_record.id, new_record.name_get()[0][1]
    
    @api.model
    def default_get(self, fields_list):        
        defaults = super(HospitalPatient, self).default_get(fields_list)        
        defaults['gender'] = 'Male'
        return defaults