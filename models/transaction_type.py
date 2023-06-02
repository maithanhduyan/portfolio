# -*- coding: utf-8 -*-
from odoo import models, fields, api

class TransactionType(models.Model):
    _name = 'portfolio.transaction_type'
    _description = 'Transaction Type'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')