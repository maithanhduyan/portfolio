# -*- coding: utf-8 -*-

import csv
import io
import base64


from odoo import http
from odoo.http import request


class PortfolioController(http.Controller):

    @http.route('/portfolio/import_assets', auth='user', type='http', methods=['POST'])
    def import_assets(self, **kwargs):
        csv_file = kwargs.get('csv_file')
        if csv_file:
            file_content = base64.b64decode(csv_file)
            file_data = io.StringIO(file_content.decode('utf-8'))
            reader = csv.DictReader(file_data)
            asset_obj = request.env['portfolio.asset']
            for row in reader:
                name = row.get('name')
                code = row.get('code')
                image = row.get('image')
                website = row.get('website')
                asset_obj.create({
                    'name': name,
                    'code': code,
                    'image': image,
                    'website': website,
                })
        return request.redirect('/portfolio')
