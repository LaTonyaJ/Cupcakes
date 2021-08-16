from wtforms.fields.core import FloatField, StringField
from wtforms.validators import AnyOf, DataRequired, NumberRange, URL
from flask_wtf import FlaskForm


class AddCupcake(FlaskForm):

    flavor = StringField('flavor', validators=[
                         DataRequired(message='Must enter a flavor')])

    size = StringField('size', validators=[AnyOf(
        values=['Small', 'Medium', 'Large'], message='Enter a valid size'), DataRequired(message='Must enter a size')])

    rating = FloatField('rating', validators=[NumberRange(
        min=0, max=10, message='Rating must be 0-10'), DataRequired(message='Must enter a rating')])

    image = StringField('image URL', validators=[
                        URL(message='Invalid URL')])
