from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import DataRequired
# from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    category = SelectField('Category', choices=[('Interview','Interview'),('Product','Product'),('Promotion','Promotion ')],validators=[DataRequired()])
    post = TextAreaField('Your Pitch', validators=[DataRequired()])
    submit = SubmitField('Pitch')

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[DataRequired()])
    submit = SubmitField('Comment')    

class UpvoteForm(FlaskForm):
    submit = SubmitField()


class Downvote(FlaskForm):
    submit = SubmitField()
