from flask import abort, g
from flask_restful import Resource, reqparse, fields, marshal_with
from flask_login import login_required
from .. import api, meta_fields
from ..auth import self_only, admin_required, permission_required
from app.models.course import Course


# Marshaled field definitions for course objects
course_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
}

# Marshaled field definitions for collections of course objects
course_collection_fields = {
    'items': fields.List(fields.Nested(course_fields)),
    'meta': fields.Nested(meta_fields),
}

class CourseResource(Resource):

    decorators = [
        self_only,
        login_required,
    ]

    def __init__(self):
        self.course_parser = reqparse.RequestParser()
        self.course_parser.add_argument('name', type = str, location = 'json')
        self.course_parser.add_argument('description', type = str, location = 'json')
        super(Course, self).__init__()

    @marshal_with(course_fields)
    def get(self, course_id = 0):
        """GET resourse handler to get a course"""
        course = Course.get_by_id(course_id)
        if not course:
            abort(404)
        return course

    @marshal_with(course_fields)
    def post(self, course_id = 0):
        """POST resourse handler to edit a course"""
        course = Course.get_by_id(course_id)
        if not course:
            abort(404)
        course.update(**course_parser.parse_args())
        return course

    def delete(self, course_id = 0):
        """DELETE resourse handler to delete course"""
        course = Course.get_by_id(course_id)
        if not course:
            abort(404)
        course.delete()
        return 204


class CourseCollectionResource(Resource):

    decorators = [
        self_only,
        login_required,
    ]

    @marshal_with(course_collection_fields)
    #@paginate()
    def get(self):
        """GET resourse handler to get all courses"""
        courses = Course.query
        return courses

    @marshal_with(course_fields)
    def post(self):
        """POST resourse handler to create a new course"""
        course = Course.create(**course_parser.parse_args())
        return course, 201

api.add_resource(CourseResource, '/courses/<course_id>')
api.add_resource(CourseCollectionResource, '/courses')
