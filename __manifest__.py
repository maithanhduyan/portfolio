{
    'name': 'Portfolio',
    'description': """This module gives you a quick view of your portfolio""",
    'version': '1.0',
    'summary': 'Manage portfolio assets',
    'sequence': 1,
    'author': 'Mai Thành Duy An',
    'category': 'Portfolio',
    'depends': ['base'],
    'data': [
        'data/asset_data.xml',
        'data/transaction_type_data.xml',
        'security/ir.model.access.csv',
        'views/portfolio.xml',
        'views/asset.xml',
        'views/dashboard.xml',
        'views/transaction.xml',
        'views/transactions_type.xml',
        'views/menu.xml',
    ],
    'qweb': [
        'static/src/xml/dashboard.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
