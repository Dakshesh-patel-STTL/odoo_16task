{
    'name': 'Silver Touch Employees',
    'author': 'Dakshesh Patel',
    'application': True,   
     'depends': [
        'base',
        'hr', 
        'mail', 
    ],
    'data': [  
        'views/action.xml',
        'views/delegate_silvertouch_employees.xml',
        'views/silvertouch_employees.xml',
        'security/security.xml',     
        'views/menu.xml',
        'views/extended_action_employees.xml',
        'views/silvertouch_employees_hobbies.xml',
        'views/silvertouch_employees_inherited.xml',
        'security/ir.model.access.csv',
        
    ]
}

