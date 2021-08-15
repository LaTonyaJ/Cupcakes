from flask_sqlalchemy import SQLAlchemy

Default_IMG = 'https://tinyurl.com/demo-cupcake'

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class Cupcake(db.Model):
    """Cupcake table"""

    __tablename__ = 'cupcakes'

    id = db.Column(db.Integer, primary_key=True)

    flavor = db.Column(db.Text, nullable=False)

    size = db.Column(db.Text, nullable=False)

    rating = db.Column(db.Float, nullable=False)

    image = db.Column(db.Text, default=Default_IMG, nullable=False)
