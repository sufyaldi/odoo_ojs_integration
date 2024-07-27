{
    'name': 'Custom OJS Integration',
    'version': '1.0',
    'summary': 'Module to integrate PKP OJS with Odoo',
    'description': 'This module handles the integration of PKP OJS with Odoo by receiving and storing publication data.',
    'author': 'Your Name',
    'category': 'Integration',
    'depends': ['base', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/publication_views.xml',
        'views/website_publication_kanban_template.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'custom_ojs_integration/static/src/css/website_publication_kanban.css',
        ],
    },
    'installable': True,
    'application': True,
}