"""
"""
import os
import base64
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin
from ..database import db, Model

class User(UserMixin, Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(24), unique = True, index = True)
    first_name = db.Column(db.String(128), nullable=True)
    last_name = db.Column(db.String(128), nullable=True)
    password_hash = db.Column(db.String(128))
    session_token = db.Column(db.String(32), unique = True, index = True)
    session_token_expiration = db.Column(db.DateTime)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    #created_at = db.Column(db.DateTime, server_default=func.now())
    #updated_at = db.Column(db.DateTime, server_default=func.now())

    # Constructor
    def __init__(self, **kwargs):
        self.username = username
        self.password = password

        super(User, self).__init__(**kwargs)
        if self.role is None:
            if self.username == current_app.config['ADMIN']:
                self.role = Role.query.filter_by(permissions = 0xff).first()
            if self.role is None:
                self.role = Role.query.filter_by(default = True).first()

    # Password
    @property
    def password(self):
        """Error"""
        #raise AttributeError('password is not a readable attribute')
        return None

    @password.setter
    def password(self, password):
        """Create password"""
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """Check if password matches"""
        return check_password_hash(self.password_hash, password)

    # Session Token
    def get_token(self, expires_in = 3600):
        """Get token"""
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds = 60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds = expires_in)
        db.session.add(self)
        return self.token

    def revoke_token(self):
        """Revoke token"""
        self.token_expiration = datetime.utcnow() - timedelta(seconds = 1)

    @staticmethod
    def check_token(token):
        """Check if user token has expired"""
        user = User.query.filter_by(token = token).first()
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user

    # Permissions
    def can(self, permissions):
        return self.role is not None and (self.role.permissions & permissions) == permissions

    def is_administrator(self):
        return self.can(Permission.ADMINISTER)

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def __repr__(self):
        """String for debugging and testing"""
        return '<User %r>' % self.username


class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False

    def is_administrator(self):
        return False
