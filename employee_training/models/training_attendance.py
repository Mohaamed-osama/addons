from odoo import models, fields


class TrainingAttendance(models.Model):
    _name = "training_attendance"
    _description = "Training Attendance"

    employee_id = fields.Many2one('employee', required=True)
    program_id = fields.Many2one('training_program', required=True)
    date = fields.Date(required=True)
    status = fields.Selection([
        ('present', 'Present'),
        ('absent', 'Absent'),
    ], default='present')


#    employee_id (Many2one): الموظف (مطلوب)
#    program_id (Many2one): البرنامج التدريبي (مطلوب)
#    date (Date): تاريخ الحضور (مطلوب)
#    status (Selection): حالة الحضور (حاضر/غائب)
