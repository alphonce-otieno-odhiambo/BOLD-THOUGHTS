from flask_wtf import FlaskForm
from flask_wtf.recaptcha import widgets
from wtforms import  StringField,  SubmitField, TextAreaField
from wtforms.validators import  Required
from wtforms.widgets import TextArea


class PostForm(FlaskForm):
    
    title = StringField('write your blogg title',validators=[Required(message =('Title please'))])
    content = TextAreaField('place your blogg', validators=[Required],widgets=TextArea())
    submit = SubmitField('Post')

