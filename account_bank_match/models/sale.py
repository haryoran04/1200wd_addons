# -*- coding: utf-8 -*-
##############################################################################
#
#    Account Bank Match
#    Copyright (C) 2016 October
#    1200 Web Development
#    http://1200wd.com/
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

# from openerp import models, fields

# FIXME: Disabled add index for now, as this code also cause problems with the compute function not being called
# class SaleOrder(models.Model):
#     _inherit = 'sale.order'
#
#     amount_total = fields.Float(
#         string='Total',
#         compute='_amount_all_wrapper',
#         index=True,
#     )