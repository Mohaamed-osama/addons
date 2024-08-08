from odoo import models, fields


class TrainingProgram(models.Model):
    _name = "training_program"
    _description = "Training Program"

    name = fields.Char(required=True)
    description = fields.Text()
    employee_id = fields.Many2one('employee')
    attendance_ids = fields.One2many('training_attendance', 'program_id')

  #  name(Char): اسم
   # البرنامج
   # التدريبي(مطلوب)
   # description(Text): وصف
    #البرنامج
   # التدريبي
 #   employee_id(Many2one): الموظف
  #  المرتبط
   # بالبرنامج
   # التدريبي
    #attendance_ids(One2many): سجل
  #  الحضور
  #  للبرنامج
   # التدريبي