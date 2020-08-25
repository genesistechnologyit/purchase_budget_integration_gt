# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class purchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.multi
    def button_confirm(self):
        for rec in self:
            for line in rec.order_line:
                if line.account_analytic_id and line.product_id.categ_id.budget_control:
                    account_analytic = line.account_analytic_id.id
                    if line.product_id.property_account_expense_id:
                        account = line.product_id.property_account_expense_id.id
                    else:
                        account = line.product_id.categ_id.property_account_expense_categ_id.id
                    for budget_line in self.env['crossovered.budget.lines'].sudo().search([
                        ('account_id','=',account),('analytic_account_id','=',account_analytic),
                        ('date_from','<=',rec.date_order),('date_to','>=',rec.date_order)
                        ,('type','=','expense'),('crossovered_budget_state','=','done')], limit=1):
                        if budget_line.remaining_amount >= line.price_subtotal:
                            budget_line.write({'reserved_amount': line.price_subtotal + budget_line.reserved_amount })
                        else:
                            raise UserError (_("Product '%s' Exceeded Budget '%s' for Account '%s' and Analytic Account '%s'"%(line.product_id.name,budget_line.crossovered_budget_id.name,
                                                                                                                       budget_line.account_id.name,budget_line.analytic_account_id.name)))
            super(purchaseOrder,self).button_confirm()


class purchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    budget_control = fields.Boolean(
        string='Budget Controlled', related="product_id.categ_id.budget_control", store=True)