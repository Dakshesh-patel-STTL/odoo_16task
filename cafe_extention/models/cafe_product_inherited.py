from odoo import fields,api,models


class InheritedProductModel(models.Model):
    _inherit="cafe.product"
    _description = 'Inherited product model of cafe'

    type_of_product=fields.Selection([('consumable','Consumable'),('stockable','Stockable'),('service','Service'),('editable','Editable')])
    product_attribuites_connect=fields.One2many('cafe.product.attribuites','product_id','Product Attribuitess')

    def create_variants(self):
        for product in self: 
            attribute_lines = product.product_attribuites_connect
            combinations = product._generate_combinations(attribute_lines)
            for combination in combinations:
                self.env['cafe.product.variants'].create({
                    'related_cafe_products': product.id,
                    'attribuite_values': [(6, 0, combination)],                   
                    'price': product._compute_variant_price(combination),
                })

    def _generate_combinations(self, attribute_lines):
        from itertools import product
        attribute_values = [line.attribuite_values.ids for line in attribute_lines]
        return list(product(*attribute_values))

    def _compute_variant_price(self, combination):
        base_price = self.sale_price
        additional_cost = sum(self.env['cafe.product.attribuite.values'].browse(value_id).cost for value_id in combination)
        return base_price + additional_cost