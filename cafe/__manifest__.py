{
    'name': 'Cafe',
    'author': 'Dakshesh Patel',
    'application': True,
    'assets': {
        'web.assets_common': [
            'cafe/static/src/css/kanbanupdate.css',
        ],
    },
    'data': [
        'security/ir.model.access.csv',        
        'views/cafe_product_tags_view.xml',
        'reports/sales_template.xml',
        'reports/report.xml',
        'views/cafe_sales_customer.xml',
        'data/sales_sequence.xml',
        'data/product_sequence.xml',
        'views/cafe_sales_filter.xml',
        'views/cafe_action.xml',
        'views/cafe_product_view.xml',
        'views/cafe_sale_view.xml',
        'views/cafe_orderline_view.xml',
        'views/cafe_tax_view.xml',
        'views/cafe_taxline_view.xml',
        'views/menu.xml'
    ]
}
