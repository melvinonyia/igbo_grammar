from flask import abort, g
from flask_restful import Resource, reqparse, fields, marshal_with
from flask_login import login_required
from .. import api, meta_fields
from ..auth import self_only, admin_required, permission_required
from app.models.deck import Deck

# Marshaled field definitions for deck objects
deck_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
}

# Marshaled field definitions for collections of deck objects
deck_collection_fields = {
    'items': fields.List(fields.Nested(deck_fields)),
    'meta': fields.Nested(meta_fields),
}

class DeckResource(Resource):

    decorators = [
        self_only,
        login_required,
    ]

    def __init__(self):
        self.deck_parser = reqparse.RequestParser()
        self.deck_parser.add_argument('name', type = str, location = 'json')
        self.deck_parser.add_argument('description', type = str, location = 'json')
        super(Deck, self).__init__()

    @marshal_with(deck_fields)
    def get(self, deck_id = 0):
        """GET resourse handler to get a deck"""
        deck = Deck.get_by_id(deck_id)
        if not deck:
            abort(404)
        return deck

    @marshal_with(deck_fields)
    def post(self, deck_id = 0):
        """POST resourse handler to edit deck"""
        deck = Deck.get_by_id(deck_id)
        if not deck:
            abort(404)
        deck.update(**deck_parser.parse_args())
        return deck

    def delete(self, deck_id = 0):
        """DELETE resourse handler to delete deck"""
        deck = Deck.get_by_id(deck_id)
        if not deck:
            abort(404)
        deck.delete()
        return 204


class DeckCollectionResource(Resource):

    decorators = [
        self_only,
        login_required,
    ]

    @marshal_with(deck_collection_fields)
    #@paginate()
    def get(self):
        """GET resourse handler to get all decks"""
        decks = Deck.query
        return decks

    @marshal_with(deck_fields)
    def post(self):
        """POST resourse handler to create a new deck"""
        deck = Deck.create(**deck_parser.parse_args())
        return deck, 201

api.add_resource(DeckResource, '/decks/<deck_id>')
api.add_resource(DeckCollectionResource, '/decks')
