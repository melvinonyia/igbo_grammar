#!/usr/bin/env python

from flask import Blueprint
from flask_restful import Api, fields


api_blueprint = Blueprint('api', __name__, url_prefix = '/api')
api = Api(api_blueprint)

# Marshaled fields for links in meta section
link_fields = {
    'prev': fields.String,
    'next': fields.String,
    'first': fields.String,
    'last': fields.String,
}

# Marshaled fields for meta section
meta_fields = {
    'page': fields.Integer,
    'per_page': fields.Integer,
    'total': fields.Integer,
    'pages': fields.Integer,
    'links': fields.Nested(link_fields)
}

# Import resources to add routes to blueprint before app is initialized
from . import resources
from . import auth
