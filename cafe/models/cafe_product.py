# -*- coding: utf-8 -*-
from odoo import fields, models, api
from odoo.exceptions import ValidationError

class CafeProduct(models.Model):
    _name = 'cafe.product'
    _description = 'Product Of Cafe'
    _rec_name = 'pro_name'

    reference_id=fields.Char(string="Reference Number")
    pro_name = fields.Char('Product Name', required=True)
    pro_code = fields.Char('Product Code', required=True)
    pro_image = fields.Image('Image')
    cost_price = fields.Float('Cost Price', required=True)
    sale_price = fields.Float('Sale Price', required=True)
    gpm = fields.Float('GPM', compute='_compute_gpm', store=True)
    tags=fields.Many2many('cafe.product.tags',string='Product Tags')
    


    _sql_constraints = [
        ('unique_pro_code','unique("pro_code")','Code of the product should be unique')
    ]
   
    @api.model
    def create(self,vals):
        print(vals)
        vals['reference_id']=self.env['ir.sequence'].next_by_code('cafe.product')
        return super(CafeProduct,self).create(vals)


    @api.constrains('cost_price')
    def _check_cost_price(self):
        for record in self:
            if record.cost_price<=0:
                raise ValidationError("Product Cost price must be greater than 0")

    @api.constrains('sale_price')
    def _check_sale_price(self):
        for record in self:
            if record.sale_price<=0:
                raise ValidationError('Product Sale price must be greater than 0')

    @api.depends('sale_price', 'cost_price')
    def _compute_gpm(self):
        for record in self:
            record.gpm = record.sale_price - record.cost_price

    def name_get(self):
        result=[]
        for product in self:
            display_name=f'[{product.pro_name}] {product.pro_code}'
            result.append((product.id,display_name))
        return result

