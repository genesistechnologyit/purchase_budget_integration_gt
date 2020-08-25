# -*- coding: utf-8 -*-
from odoo import models, fields, api

class productCategory(models.Model):
    _inherit = 'product.category'

    budget_control = fields.Boolean(
        string='Budget Controlled',
        default=False)