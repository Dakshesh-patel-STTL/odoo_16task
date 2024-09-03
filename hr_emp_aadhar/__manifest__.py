{
    'name': 'HR Employee Aadhar',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Add Aadhar No to Employee Form and Tree views',
    'description': """
        This module adds an Aadhar No field to the Employee form and tree views in Odoo.
    """,
    'depends': ['hr'],
    'data': [
        'views/hr_employee_views.xml',
    ],
    'installable': True,
    'application': False,
}
