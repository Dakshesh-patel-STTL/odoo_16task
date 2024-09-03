from odoo import fields,models,api

class Silvertouchdepartment(models.Model):
    _name = 'silvertouch.departments'
    _description = 'contains departments info'    

    dep_name=fields.Char(string='Department Name',required=True)
    dep_head=fields.Char(string='Departement Head',required=True)
    
    
    def name_get(self):
        result=[]
        for rec in self:
            new_name=f'{rec.dep_name} {rec.dep_head}'
            result.append((rec.id,new_name))
        return result
    
    @api.model
    def name_create(self, name):
        if name:
            new_values=name.split(' ')
            print(name.split(' '),'&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')

            record=self.create({
                "dep_name":new_values[0],
                "dep_head":new_values[1]
            })
            return record.name_get()[0]