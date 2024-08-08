{
    "name": "Real Estate",
    "author": "Mohamed Osama",
    "summary": 'Manage properties, owners, and sales in Odoo',
    "description": """
        This module allows you to manage real estate properties, owners, and sales within Odoo. 
        It includes features for property listing, sales orders, accounting integration, and reporting.
    """,
    "category": "sales",
    "version": "17.0.0.1.0",
    "depends": ['base', 'sale_management', 'account', 'mail', 'web', 'sale', 'board'
                ],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "views/base_menu.xml",
        "views/property_view.xml",
        "views/owner_view.xml",
        "views/tag_view.xml",
        "views/sale_order_view.xml",
        "views/building_view.xml",
        "views/property_history_view.xml",
        "views/account_move_view.xml",
        "wizard/change_state_wizard_view.xml",
        "reports/property_report.xml",
    ],
    'license': 'LGPL-3',
    'assets': {
        'web.assets_backend': ['real_estate/static/src/css/property.css'],
        'web.report_assets_common': ['real_estate/static/src/css/font.css']
    },
    "application": True,
}
