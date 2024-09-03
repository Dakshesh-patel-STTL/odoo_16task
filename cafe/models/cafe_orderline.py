# -*- coding: utf-8 -*-
from odoo import fields, models, api
from odoo.exceptions import ValidationError

class OrderLine(models.Model):

    _name = 'cafe.orderline'
    _description = 'Order Line'
    _rec_name = "id"
    sale_id = fields.Many2one('cafe.sales', 'Id',ondelete='cascade')
    product = fields.Many2one('cafe.product', 'Products', required=True)
    quantity = fields.Float('Quantity', required=True)
    price = fields.Float('Price', related='product.sale_price', required=True)
    sub_total = fields.Float('Sub Total', compute='_compute_sub_total', store=True)
    tax_id = fields.Many2many('product.taxes', 'orderline_tax_rel', 'orderline_id', 'tax_id', 'Taxes')
    tax_amount = fields.Float('Tax Amount', compute='_compute_tax_amount', store=True)
    total = fields.Float('Total After Tax', compute='_compute_total', store=True)

    @api.constrains('quantity')
    def _quantity_constrain(self):
        for rec in self:
            if rec.quantity>20:
             raise ValidationError('Quantity must be less than 20')

    @api.constrains('quantity')
    def _check_quantity(self):
        for record in self:
            if record.quantity<=0:
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


    @api.depends('product.sale_price')
    def _compute_price(self):
        for record in self:
            record.price = record.product.sale_price
