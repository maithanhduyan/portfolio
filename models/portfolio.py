# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Portfolio(models.Model):
    _name = 'portfolio.portfolio'
    _description = 'Portfolio'

    name = fields.Char(string='Name', required=True)
    total = fields.Float(string='Total')
    description = fields.Text(string='Description')
    assets = fields.Many2many('portfolio.asset', string='Assets')

    @api.depends('transactions')
    def _compute_assets(self):
        for portfolio in self:
            portfolio.assets = portfolio.transactions.mapped('asset')