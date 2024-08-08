from odoo import models, fields, api


class EmployeeInherit(models.Model):
    _inherit = "employee"

    training_date = fields.Date()
    status = fields.Selection([
        ('planned', 'Planned'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    ], default='planned')

    @api.model
    def update_status(self):
        for record in self:
            if record.training_date and record.training_date < fields.Date.today():
                record.status = 'completed'
            else:
                record.status = 'ongoing'
