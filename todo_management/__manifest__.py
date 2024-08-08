{
    'name': 'todo task',
    'version': '17.0.0.1.0',
    'summary': 'Manage your to-do tasks',
    'description': """
        This module allows you to manage to-do tasks efficiently.
        It includes features such as task creation, editing, and tracking.
    """,
    'author': 'Mohamed Osama',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/todo_view.xml',
        "reports/todo_report.xml",
    ],    'assets': {
        'web.assets_backend': ['todo_management/static/src/css/todo.css']
    },
    'application': True,
}
