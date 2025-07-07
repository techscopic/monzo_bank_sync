# -*- coding: utf-8 -*-
{
    'name': 'Monzo Bank Sync (Unofficial)',
    'version': '1.0',
    'summary': 'Sync Monzo Business transactions into Odoo',
    'description': """
Unofficial module to securely sync Monzo Business transactions into Odoo.
✅ Manual + Auto sync
✅ OAuth2 Monzo integration
✅ Daily bank statements
✅ Settled transactions only
✅ No duplicates, accurate balances
Contact: odoo@techscopic.co.uk
    """,
    'category': 'Accounting/Banking',
    'author': 'Techscopic Ltd',
    'website': 'https://github.com/techscopic/monzo_bank_sync',
    'license': 'OPL-1',
    'depends': ['account'],
    'data': [],
    'images': [
        'static/description/icon.png',
        'static/description/screenshot1.png',
        'static/description/screenshot2.png'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
