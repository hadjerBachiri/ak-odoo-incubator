# -*- coding: utf-8 -*-
# © <2016> <chafique.delli@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Sale Team Multicompany",
    "summary": "Add companies in sales team and "
    "filter the sales team from the company",
    "version": "8.0.0.1.0",
    "category": "Sales Management",
    "website": "http://akretion.com",
    "author": "Akretion",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        'sales_team',
    ],
    "data": [
        'security/ir.rule.csv',
    ],
    "demo": [
    ],
    "qweb": [
    ]
}
