
from odoo import api, models


class MoveRecompute(models.Model):
    _inherit = 'account.move'

    def recompute_dynamic_lines(self):
        super(MoveRecompute, self)._recompute_dynamic_lines()
        return True
