from ..database import db, Model
from .user import User


class Permission:
    ENROLL = 0x01
    WRITE_COURSES = 0x04
    ADMINISTER = 0x80


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)
    default = db.Column(db.Boolean, default = False)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy = 'dynamic')

    # Create roles in the database
    @staticmethod
    def insert_roles():
        roles = {
            'Guest': (0x00),
            'Student': (Permission.ENROLL, True),
            'Teacher': (Permission.WRITE_COURSES, False),
            'Administrator': (0xff, False)
        }

        for role in roles:
            role = Role.query.filter_by(name = role).first()
            if role is None:
                role = Role(name = role)
            role.permissions = roles[role][0]
            role.default = roles[role][1]
            db.session.add(role)
        db.session.commit()
