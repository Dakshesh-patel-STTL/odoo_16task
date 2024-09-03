# -*- coding: utf-8 -*-
from odoo import fields, models,api,exceptions
from odoo.exceptions import ValidationError

class CafeSales(models.Model):
    _name = 'cafe.sales'
    _description = 'Sales'
    _rec_name = 'name'

    name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,default=lambda self: ('New Order'))
    customer_id = fields.Many2one('res.partner', 'Customer', required=True)
    date = fields.Date(string='Date')
    state = fields.Selection(
        [('draft', 'Draft'), ('confirmed', 'Confirmed'), ('done', 'Done'), ('canceled', 'Canceled')],
        default='draft',
    )
    active=fields.Boolean(string='Status',default=True)
    color = fields.Integer(string='Color Index')
    order_lines_ids = fields.One2many('cafe.orderline','sale_id',string='Order Line')
    tax_lines_ids = fields.One2many('cafe.taxline','sale_id',string='Tax Lines',compute="_taxlinecreation",store=True)
    untaxed_amount = fields.Float('Untaxed Amount' , compute='_compute_untaxed_amount', store=True)
    tax_amount = fields.Float('Taxed_Amount',compute="_compute_tax_amount",store=True)
    total_amount = fields.Float('Total Amount',compute="_compute_total_amount",store=True)


    @api.constrains('order_lines_ids')
    def _check_orderlines(self):        
        for rec in self:
            if len(rec.order_lines_ids)==0:
                raise ValidationError('Please enter orderlines to save this sale')   
                    
    @api.constrains('date')
    def _check_date(self):
        for record in self:
            if record.date and record.date < fields.date.today():
                raise ValidationError('Order date cannot be past date')
    
    def default_get(self, fields_list):
        res = super(CafeSales, self).default_get(fields_list)
        res.update({
            'date': fields.Date.context_today(self)
        })
        return res

    @api.depends('order_lines_ids.sub_total')
    def _compute_untaxed_amount(self): 
        for record in self:
            record.untaxed_amount = sum(line.sub_total for line in record.order_lines_ids)

    @api.depends('order_lines_ids.tax_amount')
    def _compute_tax_amount(self):
        for record in self:
            record.tax_amount = sum(line.tax_amount for line in record.order_lines_ids)

    @api.depends('untaxed_amount', 'tax_amount')
    def _compute_total_amount(self):
        for record in self:
            record.total_amount = record.untaxed_amount + record.tax_amount

    def action_confirm(self):
        for record in self:
            if record.state != 'draft':
                raise exceptions.UserError("Only draft orders can be confirmed.")
            

    def action_cancel(self):
        for record in self:
            record.state = 'canceled'

    def action_set_to_draft(self):
        for record in self:
            record.state = 'draft'

    @api.depends('order_lines_ids')
    def _taxlinecreation(self):  
     for rec in self:    
        tax_details = {}
        rec.tax_lines_ids = [(5, 0, 0)]  
        list_taxlines = []
        for line in rec.order_lines_ids:
            for tax in line.tax_id:
                if tax.id not in tax_details:
                    tax_details[tax.id]={
                        'sub_total':line.sub_total,
                        'tax_id':tax.id,
                        'tax_percentage':tax.tax_percentage,
                        'tax_amount':(line.sub_total*tax.tax_percentage)/100
                    }
                else:
                    tax_details[tax.id]['sub_total']+=line.sub_total
                    tax_details[tax.id]['tax_amount']+=(line.sub_total*tax.tax_percentage)/100
        print(tax_details,'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        tax_lines = []  
        rec.tax_lines_ids = [(5, 0, 0)]
        for tax_id, data in tax_details.items():           
            tax_lines.append((0, 0, {
                'sale_id': rec.id,
                'tax_id': data['tax_id'],
                'base_price': data['sub_total'],
                'percentage': data['tax_percentage'],
                'tax_amount': round(data['tax_amount']),
            }))
        print(tax_lines,'Tax_lines here ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
               
        rec.tax_lines_ids = tax_lines
    
    def unlink(self):
       for rec in self:
           if rec.state=='confirmed':
               raise ValidationError('You cannot delete confirmed sales')
       return super(CafeSales,self).unlink()