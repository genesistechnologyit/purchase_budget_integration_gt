# -*- coding: utf-8 -*-
{
    'name': "Purchase Order Integration with Budget",

    'summary': """
        This module used to integrate odoo budget with purchase order and Supplier Invoice.""",

    'description': """
       This module used to integrate odoo budget with purchase order and Supplier Invoice
    """,

    'author': "Genesis Technology",
    'website': "genesistechnologyit@gmail.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account_accountant','account_budget','purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/budget.xml',
        'views/purchase.xml',
        'views/product.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}