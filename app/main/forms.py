from flask_wtf import FlaskForm
from wtforms import  StringField,  SubmitField, TextAreaField
from wtforms.validators import  Required



class PostForm(FlaskForm):
    
    title = StringField('write your blogg title',validators=[Required(message =('Title please'))])
    content = TextAreaField('place your blogg', validators=[Required()])
    submit = SubmitField('Post')

