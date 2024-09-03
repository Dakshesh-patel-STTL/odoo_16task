from odoo import fields,models

class ProductAttribuite(models.Model):
    _name = 'cafe.product.attribuite'
    _description = 'cafe product attribuite'

    name=fields.Char(string="Name", required=True)
    


    