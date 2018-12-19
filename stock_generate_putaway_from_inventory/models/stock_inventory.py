# -*- coding: utf-8 -*-
# © 2018 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models
from odoo.exceptions import UserError


def _get_putaway_strategy(loc):
    if loc.putaway_strategy_id:
        return loc.putaway_strategy_id
    elif loc.location_id:
        return _get_putaway_strategy(loc.location_id)


class StockInventory(models.Model):
    _inherit = "stock.inventory"

    def generate_putaway_strategy_multi(self):
        for inventory in self:
            inventory._generate_putaway_strategy()

    def _generate_putaway_strategy(self):
        putaway_locations = {}
        if self.state != 'done':
            raise UserError('Please, validate the stock adjustment before')
        strategy = _get_putaway_strategy(self.location_id)
        if not strategy:
            raise UserError('Please, specify a Putaway Strategy '
                            'on the inventory\'s location (or a parent one)')
        for line in self.line_ids:
            if not line.product_id.product_putaway_ids:

                if (line.product_id.id not in putaway_locations
                        or line.product_qty >
                        putaway_locations[line.product_id.id]['qty']):

                    putaway_locations[line.product_id.id] = {
                        'qty': line.product_qty,
                        'product_product_id': line.product_id.id,
                        'product_tmpl_id': line.product_id.product_tmpl_id.id,
                        'fixed_location_id': line.location_id.id,
                        'putaway_id': strategy.id
                        }

        for putaway_location in putaway_locations.values():
            putaway_location.pop('qty')
            self.env['stock.product.putaway.strategy'].create(putaway_location)