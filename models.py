"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def connect_db(app):
    """Connect this database to provided Flask app.
    """
    app.app_context().push()
    db.app = app
    db.init_app(app)

DEFAULT_IMAGE_URL = "https://tinyurl.com/demo-cupcake"

class Cupcake(db.Model):
    """Model for Cupcake resource"""

    __tablename_ = "cupcakes"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True)

    flavor = db.Column(
        db.String(50),
        nullable=False,
    )

    size = db.Column(
        db.String(15),
        nullable=False
    )

    rating = db.Column(
        db.Integer,
        nullable=False
    )


    image_url = db.Column(
        db.String(500),
        nullable=False,
        default=DEFAULT_IMAGE_URL
    )
