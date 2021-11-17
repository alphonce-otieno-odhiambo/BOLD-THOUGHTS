from ..models import User
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, BooleanField, SubmitField, ValidationError
from wtforms.validators import EqualTo, Required, Length, Email



class RegistrationForm(FlaskForm):
    username = StringField('Enter username',validators=[Required()])
    email = StringField('Enater email',validators=[Required(),Email()])
    password = PasswordField('Password',validators = [Required(),Length(min = 8,max=16), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('SignUp')

    def validate_email(self, data_field):
        if User.query.filter_by(email =data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self, data_field):
        if User.query.filter_by(username =data_field.data).first():
            raise ValidationError('That user name is already taken')


class LoginForm(FlaskForm):
    email = email = StringField('Enater email',validators=[Required(),Email()])
    password = PasswordField('Confirm Passwords',validators = [Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('LogIn')



