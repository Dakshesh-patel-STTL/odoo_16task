# -*- coding: utf-8 -*-
# from odoo import http


from odoo import http
from odoo.http import request

class CafeSalesController(http.Controller):

    @http.route('/cafe/sales/view', auth='public', website=True)
    def view_sales(self, **kwargs):
        return request.render('extendedwebsite.cafe_sales_view_new')



class ProductEnquiryController(http.Controller):

    @http.route('/product/enquiry', type='http', auth='public', website=True)
    def product_enquiry_form(self, **kw):                       
        return request.render('extendedwebsite.product_enquiry_form')


class ProductEnquiryController(http.Controller):

    @http.route('/product/enquiry/submit', type='http', auth='public', methods=['POST'], website=True)
    def product_enquiry_submit(self, **post):
     
        name = post.get('name')
        email = post.get('email')
        contact = post.get('contact')
        message = post.get('message')
        product_id = post.get('product_id')

        print(name,email,'(***************************************************************************)')
     
        return request.render('extendedwebsite.product_enquiry_thank_you')