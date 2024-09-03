from odoo import fields,api,models

class InheritedProductSale(models.Model):
    _inherit="cafe.sales"
    
    
    def action_confirm(self):
        for record in self:
            record.state = 'confirmed'
            if record.name == 'New Order':
                record.name = self.env['ir.sequence'].next_by_code('cafe.sales')                    