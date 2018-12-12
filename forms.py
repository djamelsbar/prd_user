from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField, PasswordField, SelectField
from wtforms import validators
from wtforms.ext.sqlalchemy.fields import  QuerySelectMultipleField



class UserForm(FlaskForm):
    username = StringField("username", [validators.DataRequired("Please enter username.")])
    password = PasswordField("password", [validators.DataRequired("Repeat Password")])
    submit = SubmitField("Submit")

    def validate(self):
        from model import User
        if not super(UserForm,self).validate():
            return False

        user = User.query.filter_by(username=self.username.data).first()
        if user is None:
            self.username.errors.append('Unknown username')
            return False
        if user.check

def get_category():
    from app import Category
    return Category.query.all()


class ProductForm(FlaskForm):
    name = StringField("name", [validators.DataRequired("Please enter name.")])
    description = TextAreaField("description", [validators.DataRequired("Please enter description.")])
    category = QuerySelectMultipleField('Category', [validators.DataRequired(u'Please select a Category')],query_factory= get_category, get_label='name', allow_blank=True)
    submit = SubmitField("Submit")



class CategoryForm(FlaskForm):
    name = StringField("name", [validators.DataRequired("Please enter name.")])
    description = TextAreaField("description", [validators.DataRequired("Please enter description.")])
    submit = SubmitField("Submit")


