from flask import abort, g
from flask_restful import Resource, reqparse, fields, marshal_with
from flask_login import login_required
from .. import api, meta_fields
from ..auth import self_only, admin_required, permission_required
from app.models.user import User


# Marshaled field definitions for user objects
user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'password': fields.String,
    'first_name': fields.String,
    'last_name': fields.String,
}

# Marshaled field definitions for collections of user objects
user_collection_fields = {
    'items': fields.List(fields.Nested(user_fields)),
    'meta': fields.Nested(meta_fields),
}

class UserResource(Resource):

    def __init__(self):
        self.user_parser = reqparse.RequestParser()
        self.user_parser.add_argument('username', type=str, location='json', required=True)
        self.user_parser.add_argument('first_name', type=str, location='json')
        self.user_parser.add_argument('last_name', type=str, location='json')
        self.user_parser.add_argument('password', type=str, location='json')
        super(User, self).__init__()

    @marshal_with(user_fields)
    def get(self, user_id=None, username=None):
        """GET resourse handler to get a user"""
        user = None
        if username is not None:
            user = User.get_by_username(username)
        else:
            user = User.get_by_id(user_id)
        if not user:
            abort(404)
        return user

    @login_required
    @self_only
    @marshal_with(user_fields)
    def post(self, user_id = None, username = None):
        """PUT resourse handler to edit a user"""
        g.user.update(**user_parser.parse_args())
        return g.user

    @login_required
    @self_only
    def delete(self, user_id = None, username = None):
        """DELETE resourse handler to delete user"""
        g.user.delete()
        return 204


class UserCollectionResource(Resource):

    @login_required
    @admin_required
    @marshal_with(user_collection_fields)
    #@paginate()
    def get(self):
        """GET resourse handler to get all users"""
        users = User.query
        return users

    @marshal_with(user_fields)
    def post(self):
        """POST resourse handler to create a new user"""
        user = User.create(**user_parser.parse_args())
        return user, 201

api.add_resource(UserResource, '/users/<user_id>', '/users/<username>')
api.add_resource(UserCollectionResource, '/users')
