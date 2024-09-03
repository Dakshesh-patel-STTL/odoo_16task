from odoo import fields, models, api
from odoo.exceptions import ValidationError

class ExtendedOrderLine(models.Model):
    _name = 'cafe.extended.delegate.orderline'
    _description = 'Extended Order Line with Product Variants'

    extended_sale_id = fields.Many2one('cafe.extended.delegate.sales', string='Sales Order')
    product_variant_id = fields.Many2one('cafe.product.variants', 'Product Variant', required=True)
    quantity = fields.Float('Quantity', required=True)
    price = fields.Float('Price', related='product_variant_id.price', required=True)
    sub_total = fields.Float('Sub Total', compute='_compute_sub_total', store=True)
    tax_id = fields.Many2many('product.taxes', 'extended_orderline_tax_rel', 'orderline_id', 'tax_id', 'Taxes')
    tax_amount = fields.Float('Tax Amount', compute='_compute_tax_amount', store=True)
    total = fields.Float('Total After Tax', compute='_compute_total', store=True)

    @api.constrains('quantity')
    def _check_quantity(self):
        for record in self:
            if record.quantity <= 0:
                raise ValidationError('Quantity must be greater than 0')

    @api.depends('quantity', 'price')
    def _compute_sub_total(self):
        for record in self:
            record.sub_total = record.quantity * record.price

    @api.depends('sub_total', 'tax_id')
    def _compute_tax_amount(self):
        for record in self:
            total_tax_amount = 0.0
            for tax in record.tax_id:
                total_tax_amount += (record.sub_total * tax.tax_percentage) / 100
            record.tax_amount = total_tax_amount

    @api.depends('sub_total', 'tax_amount')
    def _compute_total(self):
        for record in self:
            record.total = record.sub_total + record.tax_amount
