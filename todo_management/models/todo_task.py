from odoo import models, fields, api


class TodoTask(models.Model):
    _name = "todo_task"
    _description = "To Do Record"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "task_name"

    task_name = fields.Char(default='New', required=True)
    assign_to = fields.Many2one('res.users', required=True)
    description = fields.Text()
    due_date = fields.Date(required=True)
    status = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('closed', 'Closed'),
    ], default='new')
    estimated_time = fields.Integer()
    total_time = fields.Integer(compute='_compute_total_time', store=True, readonly=True)
    line_ids = fields.One2many('todo_task.line', 'todo_task_id')
    active = fields.Boolean(default=True)
    is_late = fields.Boolean()

    _sql_constraints = [
        ('unique_name', 'UNIQUE(task_name)', 'This name already exists!'),
        ('check_estimated_time', 'CHECK(estimated_time >= total_time)',
         'Estimated time must be greater than or equal to total time.')
    ]

    @api.depends('line_ids.time')
    def _compute_total_time(self):
        for task in self:
            total = sum(line.time for line in task.line_ids)
            task.total_time = total

    def check_duo_date(self):
        todo_ids = self.search([])
        for rec in todo_ids:
            if rec.due_date and rec.due_date < fields.Date.today():
                rec.is_late = True

    def action_new(self):
        self.status = 'new'

    def action_progress(self):
        self.status = 'in_progress'

    def action_completed(self):
        self.status = 'completed'

    def action_closed(self):
        self.status = 'closed'


class TodoTaskLine(models.Model):
    _name = "todo_task.line"

    todo_task_id = fields.Many2one('todo_task')
    date = fields.Date()
    description = fields.Text()
    time = fields.Integer()
