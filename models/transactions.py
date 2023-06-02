# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Transactions(models.Model):
    _name = 'portfolio.transactions'
    _description = 'Transactions'

    portfolio = fields.Many2one('portfolio.portfolio', string='Portfolio', required=True)
    datetime = fields.Datetime(string='Date and Time', default=fields.Datetime.now)
    asset = fields.Many2one('portfolio.asset', string='Asset', required=True)
    transaction_type = fields.Many2one('portfolio.transaction_type', string='Transaction Type', required=True)
    amount = fields.Float(string='Amount', required=True)
    total = fields.Float(string='Total')
    fee = fields.Float(string='Fee')
    note = fields.Text(string='Note')
