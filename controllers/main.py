from odoo import http
from odoo.http import request
import json

class OJSIntegrationController(http.Controller):

    @http.route('/ojs/integration', type='json', auth='public', methods=['POST'], csrf=False)
    def receive_ojs_data(self, **post):
        data = json.loads(request.httprequest.data)
        PublicationModule = request.env['publication.module']
        PublicationModule.create({
            'title': data.get('title'),
            'abstract': data.get('abstract'),
            'authors': data.get('authors'),
            'publication_date': data.get('publication_date'),
        })
        return {'status': 'success', 'message': 'Data received successfully'}