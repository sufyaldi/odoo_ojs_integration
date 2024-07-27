from odoo import models, fields

class Publication(models.Model):
    _name = 'publication.module'
    _description = 'Publication Module'

    title = fields.Char(string='Title', required=True)
    abstract = fields.Text(string='Abstract')
    authors = fields.Char(string='Authors')
    publication_date = fields.Date(string='Publication Date')
    journal_url = fields.Char(string='Journal URL')
    author_photo = fields.Binary(string='Author Photo')