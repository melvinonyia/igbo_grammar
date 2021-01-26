from ..database import db, Model
from .card import Card


class Deck(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique = True)
    description = db.Column(db.String)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    cards = db.relationship('Card', backref='card', lazy = 'dynamic')

    # Constructor
    def __init__(self, **kwargs):
        self.name = name
        self.description = description
