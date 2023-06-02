# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Asset(models.Model):
    _name = 'portfolio.asset'
    _description = 'Portfolio Asset'

    name = fields.Char(string='Name')
    code = fields.Char(string='Code')
    image = fields.Binary(string='Image')
    website = fields.Char(string='Website')

    def _auto_init(self):
        # Tạo câu lệnh SQL tạo bảng "asset"
        self._cr.execute('''
            CREATE TABLE IF NOT EXISTS portfolio_asset (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255),
                code VARCHAR(255),
                image BYTEA,
                website VARCHAR(255)
            );
        ''')

        # Gọi phương thức _auto_init() của lớp cha
        super(Asset, self)._auto_init()