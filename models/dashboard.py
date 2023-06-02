# -*- coding: utf-8 -*-
from odoo import models, fields

class Dashborad(models.Model):
    _name = 'portfolio.dashboard'
    _description = 'Dashborad'

    name = fields.Char(string='Name', required=True)
    total = fields.Float(string='Total')
    description = fields.Text(string='Description')