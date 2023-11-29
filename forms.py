from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import InputRequired, Optional

class AddPetForm(FlaskForm):
    name = StringField('Name:', validators=[InputRequired()])
    species = StringField('Species:', validators=[InputRequired()])
    photo_url = StringField('Photo link:')
    age = IntegerField('Age:')
    notes = StringField('Notes:')

class EditPetForm(FlaskForm):
    photo_url = StringField('Photo link:')
    notes = StringField('Notes:')
    available = BooleanField('Available:')