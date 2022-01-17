# -*- coding: utf-8 -*-
{
    'name': "recetas",
    'summary': 'Módulo diseñado para enfatizar la creatividad y la iniciativa',
    'description': 'Este módulo está diseñado para todos aquellos fans de la cocina creativa',
    'author': "Adriá Foo",
    'website': "http://www.receweb.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list

    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True  
}
