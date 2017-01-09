# -*- coding: utf-8 -*-
# Copyright (C) 2017  Renato Lima - Akretion
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import models

class SaleMakeInvoice(models.TransientModel):
    _inherit = "sale.make.invoice"

    def make_invoices(self, cr, uid, ids, context=None):
        
        order_obj = self.pool.get('sale.order')
        if context is None:
            context = {}
        for order in order_obj.browse(cr, uid,
                                      context.get(('active_ids'), []),
                                      context=context):
            if order.fiscal_category_id:
                context.update({'fiscal_document_code': '55'})

        return super(SaleMakeInvoice, self).make_invoices(cr,
                                                          uid,
                                                          ids,
                                                          context)
