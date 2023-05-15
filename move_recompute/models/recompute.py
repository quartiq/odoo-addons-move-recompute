
from odoo import api, models


class MoveRecompute(models.Model):
    _inherit = 'account.move'

    def recompute_dynamic_lines(self, **kwargs):
        super(MoveRecompute, self)._recompute_dynamic_lines(**kwargs)
        return True
