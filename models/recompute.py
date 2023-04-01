
from odoo import api, models


class MoveRecompute(models.Model):
    _inherit = 'account.move'

    def recompute_dynamic_lines(self):
        return super(MoveRecompute, self)._recompute_dynamic_lines()
