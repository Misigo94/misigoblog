from . import main
from flask_wtf import FlaskForm
from wtforms import SubmitField,TextAreaField,StringField,SelectField
from wtforms.validators import InputRequired
from ..models import Post,Comment

class PostForm(FlaskForm):
    posttitle = TextAreaField('Post Title', validators=[InputRequired()])
    postdescription = TextAreaField('Post Description', validators=[InputRequired()])
    # postcategory = SelectField('Post Category', choices = [('Marketing', 'Business'),('Agriculture','Life'),('Any other')], validators=[InputRequired()])
    postcategory = TextAreaField('Post Category', validators=[InputRequired()])
    # postauthor = SelectField('post Author',validators=[InputRequired()])
    submit = SubmitField('Submit post')

class CommentForm(FlaskForm):
    commentdescription = TextAreaField('Post Description', validators=[InputRequired()])
    submit = SubmitField('Submit Comment')
