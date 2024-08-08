{
    'name': 'employee_training',
    'version': '17.0.0.1.0',
    'author': 'Mohamed Osama',
    'summary': 'Manage employee training programs and attendance efficiently.',
    'description': """
        This module enables efficient management of employee training programs and attendance in Odoo.
        Key features include:
        - Creation and management of training programs.
        - Tracking employee attendance and progress in training sessions.
        - Integration with Odoo's security model for access control.
        
        By installing this module, businesses can streamline their employee development processes,
        ensuring that training initiatives are well-organized and monitored effectively.
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/employee_view.xml',
        'views/training_program_view.xml',
        'views/training_attendance_view.xml',
    ],
    'application': True,
}
