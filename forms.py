from wtforms.fields.core import FloatField, StringField
from wtforms.validators import AnyOf, NumberRange, URL
from flask_wtf import FlaskForm


class AddCupcake(FlaskForm):

    flavor = StringField('flavor')

    size = StringField('size', validators=[AnyOf(
        values=['Small', 'Medium', 'Large'], message='Enter a valid size')])

    rating = FloatField('rating', validators=[NumberRange(
        min=0, max=10, message='Rating must be 0-10')])

    image = StringField('image URL', validators=[URL(message='Invalid URL')])
