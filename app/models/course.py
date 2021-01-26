from ..database import db, Model
from .deck import Deck

class Course(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique = True)
    description = db.Column(db.String)
    decks = db.relationship('Deck', backref='deck', lazy = 'dynamic')

    # Constructor
    def __init__(self, **kwargs):
        self.name = name
        self.description = description
