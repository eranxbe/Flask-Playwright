from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, RadioField, TextAreaField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, InputRequired, Email, NumberRange
from . import form_enums

class NamerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()], render_kw={'class': 'form-control', 'type': 'text'})
    submit = SubmitField('Submit', render_kw={'class': 'btn btn-primary'})

class UserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()], render_kw={'class': 'form-control', 'type': 'text'})
    email = StringField('Email', validators=[Email()], render_kw={'class': 'form-control', 'type': 'email'})
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=1, max=120)], render_kw={'class': 'form-control', 'type': 'number'})
    gender = RadioField('Gender', choices=[(gender.value, gender.name) for gender in form_enums.GenderEnum], validators=[DataRequired()], render_kw={'class': 'form-check', 'style': 'list-style-type: none;'})
    interests = SelectField('Interests', choices=[(i.value, i.name) for i in form_enums.InterestsEnum], render_kw={'class': 'form-select'})
    country = SelectField('Country', choices=[(country.value, country.name) for country in form_enums.CountryEnum], validators=[DataRequired()], render_kw={'class': 'form-control'})
    comments = TextAreaField('Comments', render_kw={'class': 'form-control'})
    submit = SubmitField('Submit', render_kw={'class': 'btn btn-primary'})

class TraderFormAPI(FlaskForm):
    api_key = StringField('API Key', validators=[DataRequired()], render_kw={'class': 'form-control', 'type': 'text'})
    secret_api = StringField('Secret API Key', validators=[DataRequired()], render_kw={'class': 'form-control', 'type': 'password'})
    submit = SubmitField('Submit', render_kw={'class': 'btn btn-primary'})