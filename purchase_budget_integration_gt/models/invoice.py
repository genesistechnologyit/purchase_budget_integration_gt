# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class accountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def action_invoice_open(self):
        for rec in self:
            if rec.type == 'in_invoice':
                for line in rec.invoice_line_ids:
                    if line.account_analytic_id and line.product_id.categ_id.budget_control:
                        account_analytic = line.account_analytic_id.id
                        account = line.account_id.id
                        for budget_line in self.env['crossovered.budget.lines'].sudo().search([
                            ('account_id','=',account),('analytic_account_id','=',account_analytic)
                            ,('type','=','expense'),('crossovered_budget_state','=','done')], limit=1):
                                budget_line.write({'reserved_amount': budget_line.reserved_amount - line.price_subtotal,
                                                   'practical_amount':budget_line.practical_amount + line.price_subtotal})
            super(accountInvoice,self).action_invoice_open()