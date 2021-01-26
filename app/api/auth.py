from flask import g, abort
from flask_httpauth import HTTPBasicAuth
from flask_login import current_user
from functools import wraps
from ..extensions import auth
from app.models.user import User
from app.models.role import Permission


@auth.verify_password
def verify_password(username, password):
    """ """
    if username == '':
        g.current_user = AnonymousUser()
        return True
    user = User.query.filter_by(username = username).first()
    if not user:
        return False
    g.current_user = user
    return user.verify_password(password)

    @auth.error_handler
    def auth_error():
        return unauthorized('Invalid credentials')

def self_only(func):
    """ """

# Custom decorators that check user permissions
def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not g.current_user.can(permission):
                return forbidden('Insufficient permissions')
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def admin_required(f):
    return permission_required(Permission.ADMINISTER)(f)
