# -*- coding: utf-8 -*-
{
    'name': "Extendedwebsite",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'website',
    'version': '0.1',
    'depends': ['website'],
    'data': [
        'views/product_enquiry_thank_you_view.xml',
        'views/product_form.xml',
        'views/block_price_website.xml',
        'views/cafe_sales_view.xml',
        'views/views.xml',
        'views/templates.xml',        
    ],
}
