#!/usr/bin/env python
"""
Manage
- Launches the application
- Other application tasks
"""

import os
from flask_script import Manager, Shell, Server
from flask_migrate import MigrateCommand
from app import create_app
from app.models.user import User
from app.models.role import Role

app = create_app('default')
manager = Manager(app)

def _make_context():
    """Return context dict for a shell session so you can access
    app, db, and the User model by default.
    """
    return {'app': app, 'db': db, 'User': User, 'Role': Role}

manager.add_command('server', Server())
manager.add_command("shell", Shell(make_context = _make_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
