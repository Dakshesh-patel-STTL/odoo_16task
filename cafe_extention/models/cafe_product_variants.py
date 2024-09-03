from odoo import fields,api,models

class ProductVariant(models.Model):
    _name = 'cafe.product.variants'
    _description = 'cafe product variants'    
    _inherits={'cafe.product':'related_cafe_products'}

    related_cafe_products=fields.Many2one('cafe.product','Related to cafe product')
    attribuite_values=fields.Many2many('cafe.product.attribuite.values',string="Attribuite values")
    price = fields.Float(string="Variant Price", compute='_compute_variant_price', store=True)
    name = fields.Char(string="Variant Name", compute='_compute_variant_name', store=True)
    @api.depends('attribuite_values', 'related_cafe_products.sale_price')
    def _compute_variant_price(self):
        for variant in self:
            total_attribute_cost = sum(variant.attribuite_values.mapped('cost'))
            variant.price = variant.related_cafe_products.sale_price + total_attribute_cost

    @api.depends('attribuite_values', 'related_cafe_products.pro_name')
    def _compute_variant_name(self):
        for variant in self:
            attribute_names = ', '.join(variant.attribuite_values.mapped('name'))
            variant.name = f"{variant.related_cafe_products.pro_name} ({attribute_names})"