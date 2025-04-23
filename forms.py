from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length, Regexp

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ConsumerForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    mobile = StringField('Mobile Number', validators=[
        DataRequired(),
        Length(min=10, max=10, message="Mobile number must be 10 digits"),
        Regexp('^[0-9]*$', message="Only numbers allowed")
    ])
    email = StringField('Email ID', validators=[DataRequired(), Email()])
    address = StringField('Address', validators=[DataRequired()])
    block = StringField('Block', validators=[DataRequired()])
    state = SelectField('State', validators=[DataRequired()])
    district = SelectField('District', validators=[DataRequired()])
    pin_code = StringField('PIN Code', validators=[
        DataRequired(),
        Length(min=6, max=6, message="PIN code must be 6 digits"),
        Regexp('^[0-9]*$', message="Only numbers allowed")
    ])
    ca_number = StringField('CA Number', validators=[DataRequired()])
    submit = SubmitField('Submit')