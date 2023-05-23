from flask_wtf import FlaskForm
from wtforms import StringField, FormField, FileField, IntegerField
from wtforms.validators import DataRequired, Regexp, Length

class LibraryForm(FlaskForm):
    title=StringField('Tytuł', validators=[DataRequired()])
    author=StringField('Autor', validators=[DataRequired()])
    publication=StringField('Rok wydania', validators=[DataRequired(), Length(max=4)])
    description=StringField('Opis', validators=[DataRequired(), Length(max=60)])
    # picture=FileField('picture', validators=[Regexp('^[^/\\]\.jpg$')])
    