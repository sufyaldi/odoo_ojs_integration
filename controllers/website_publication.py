from odoo import http
from odoo.http import request

class WebsitePublication(http.Controller):

    @http.route('/publications', type='http', auth='public', website=True)
    def publications(self, **kwargs):
        publications = request.env['publication.module'].search([])
        return request.render('custom_ojs_integration.publication_kanban_template', {
            'publications': publications
        })