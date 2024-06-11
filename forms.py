from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

#----Register Form----#
class RegisterForm(FlaskForm):
    name = StringField("Name")
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Sign Up")
#----Login Form----#
class LogInForm(FlaskForm):
    email = StringField("")
    password = PasswordField("Password")
    submit = SubmitField("Log In")
#----Create Post Form----#
class CreateBlogForm(FlaskForm):
    title = StringField("Blog Title", validators=[DataRequired()])
    subtitle = StringField("Blog Subtitle", validators=[DataRequired()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Blog")
#----Create Comment Form----#
class CreatCommentForm(FlaskForm):
    body = StringField("Comment", validators=[DataRequired()])
    submit = SubmitField("Comment")