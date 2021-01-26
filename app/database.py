from sqlalchemy.orm import relationship
from .extensions import db


relationship = relationship


class CRUDMixin(object):
    """Mixin that adds convenience methods for CRUD (creat, read, update, delete) operations."""

    @classmethod
    def create(cls, **kwargs):
        """Create a new record and save it in the database."""
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit = True, **kwargs):
        """Update specific fields of a record."""
        kwargs.pop('id', None)
        for attr, value in kwargs.interitems():
            if value is not None:
                setattr(self, attr, vlaue)
        return commit and self.save() or self

    def save(self, commit = True):
        """Save the record."""
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit = True):
        """Remove the record from the database."""
        db.session.delete(self)
        return commit and db.session.commit()


class Model():
    """Base model class that includes CRUD convenience methods."""
    __abstract__ = True


class SurrogatePK():
    """A mixin that adds a surrogate integer 'primary key' column named ``id`` to any declarative-mapped class."""
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key = True)

    @classmethod
    def get_by_id(cls, id):
        """ """
        if id <= 0:
            raise ValueError("ID is zero or less")
        if any((isinstance(id, (str, bytes)) and id.isdigit(), isinstance(id, (int, float)))):
            return cls.query.get(int(id))
        return None


def ReferenceColumn(tablename, nullable = False, pk_name = 'id', **kwargs):
    """Column that adds primary key foregn key reference."""
    return db.Column(
        db.ForeignKey(
            "{0}.{1}".format(tablename, pk_name)
        ),
        nullable=nullable, **kwargs
    )
