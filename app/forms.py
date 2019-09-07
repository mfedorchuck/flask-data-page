from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RecordForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    value = IntegerField('Value', validators=[DataRequired()])


class PostForm(FlaskForm):
    post = TextAreaField('Save your data (for now - locally)', validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Submit')


class MultiPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    userCase = StringField('User Case', validators=[DataRequired()])

    text = TextAreaField('', validators=[DataRequired(), Length(min=1, max=5000)])

    submit = SubmitField('Submit')
