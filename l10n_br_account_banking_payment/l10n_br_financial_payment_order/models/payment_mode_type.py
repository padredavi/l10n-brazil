# -*- coding: utf-8 -*-
# Copyright 2017 KMEE INFORMATICA LTDA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from __future__ import division, print_function, unicode_literals

from openerp import api, fields, models, _


class PaymentModeType(models.Model):

    _inherit = 'payment.mode.type'

    payment_order_type = fields.Selection(
        selection_add=[
            ('cobranca', u'Cobrança'),
        ])
