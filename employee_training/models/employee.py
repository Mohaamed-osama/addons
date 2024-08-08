from odoo import models, fields


class Employee(models.Model):
    _name = "employee"
    _description = "Employee"

    name = fields.Char(required=True)
    department = fields.Char()
    training_ids = fields.One2many('training_program', 'employee_id',)
#   name (Char): اسم الموظف (مطلوب)
#   department (Char): القسم
#   training_ids (One2many): البرامج التدريبية التي حضرها الموظف
