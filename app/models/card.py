from ..database import db, Model


class Card(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    question = db.Column(db.String)
    answer = db.Column(db.String)
    deck_id = db.Column(db.Integer, db.ForeignKey('deck.id'))

    # Constructor
    def __init__(self, **kwargs):
        self.question = question
        self.answer = answer
