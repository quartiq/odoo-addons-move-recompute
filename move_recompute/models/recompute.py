
from odoo import api, models


class MoveRecompute(models.Model):
    _inherit = 'account.move'

    def recompute_dynamic_lines(self, recompute_all_taxes=False,
                                recompute_tax_base_amount=False):
        super(MoveRecompute, self)._recompute_dynamic_lines(recompute_all_taxes, recompute_tax_base_amount)
        return True
