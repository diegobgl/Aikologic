# Copyright 2022 Vida ERP
# @author: Dmytro Pavlov (<dmitriy.paulov@gmail.com>)
# License OPL-1 (https://www.odoo.com/documentation/15.0/legal/licenses.html).
{
    'name' : 'VidaERP UoM',
    'summary': 'Adds units of measure required for all VidaERP modules',
    'version': '15.0',
    'category': 'Extra Tools',
    'author': 'Dmytro Pavlov, VidaERP',
    'company': 'VidaERP',
    'maintainer': 'VidaERP',
    'depends' : [
        'uom',
    ],
    'data': [
        'data/uom_data.xml',
    ],
    'images': [
        'static/description/banner.png',
        'static/description/icon.png',
    ],
    'installable': True,
    'application': False,
    'license': 'OPL-1',
}
