# -*- coding: utf-8 -*-

from odoo import models, fields, api

class crossoveredBudget(models.Model):
    _inherit = 'crossovered.budget'

    type = fields.Selection(
        string='Type',
        selection=[('expense', 'Expense'),
                   ('revenue', 'Revenue'), ],
        required=True,)


class crossoveredBudget(models.Model):
    _inherit = 'crossovered.budget.lines'


    @api.multi
    @api.depends('planned_amount','practical_amount','reserved_amount')
    def get_remaining(self):
        for rec in self:
            rec.remaining_amount = rec.planned_amount + rec.practical_amount - rec.reserved_amount

    account_id = fields.Many2one(
        comodel_name='account.account',
        string='Account',
        required=True)
    reserved_amount = fields.Float(
        string='Reserved Amount',
        required=False)
    remaining_amount = fields.Float(
        string='Remaining Amount',
        compute="get_remaining")
    type = fields.Selection(
        string='Type',
        selection=[('expense', 'Expense'),
                   ('revenue', 'Revenue'), ],
        related="crossovered_budget_id.type",store=True )
    lock = fields.Boolean(
        string='Locked')
