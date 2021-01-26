from flask import abort, g
from flask_restful import Resource, reqparse, fields, marshal_with
from flask_login import login_required
from .. import api, meta_fields
from ..auth import self_only, admin_required, permission_required
from app.models.card import Card

# Marshaled field definitions for card objects
card_fields = {
    'id': fields.Integer,
    'question': fields.String,
    'answer': fields.String,
}

# Marshaled field definitions for collections of card objects
card_collection_fields = {
    'items': fields.List(fields.Nested(card_fields)),
    'meta': fields.Nested(meta_fields),
}

class CardResource(Resource):

    decorators = [
        self_only,
        login_required,
    ]

    def __init__(self):
        self.card_parser = reqparse.RequestParser()
        self.card_parser.add_argument('question', type = str, location = 'json')
        self.card_parser.add_argument('answer', type = str, location = 'json')
        super(Card, self).__init__()

    @marshal_with(card_fields)
    def get(self, card_id = 0):
        """GET resourse handler to get a card"""
        card = Card.get_by_id(card_id)
        if not card:
            abort(404)
        return card

    @marshal_with(card_fields)
    def post(self, card_id = 0):
        """POST resourse handler to edit card"""
        card = Card.get_by_id(card_id)
        if not card:
            abort(404)
        card.update(**card_parser.parse_args())
        return card

    def delete(self, card_id = 0):
        """DELETE resourse handler to delete card"""
        card = Card.get_by_id(card_id)
        if not card:
            abort(404)
        card.delete()
        return 204


class CardCollectionResource(Resource):

    decorators = [
        self_only,
        login_required,
    ]

    @marshal_with(card_collection_fields)
    #@paginate()
    def get(self):
        """GET resourse handler to get all cards"""
        cards = Card.query
        return cards

    @marshal_with(card_fields)
    def post(self):
        """POST resourse handler to create a new card"""
        card = Card.create(**card_parser.parse_args())
        return card, 201

api.add_resource(CardResource, '/cards/<card_id>')
api.add_resource(CardCollectionResource, '/cards')
