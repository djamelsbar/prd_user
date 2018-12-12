
from flask import Flask, render_template, request, flash,url_for,redirect,session
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate
import os
from forms import *

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'admin.db')
app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from model import *


@app.route('/login/', methods=['GET', 'POST'])
def login():
        form = UserForm()

        if request.method == 'POST':
            if form.validate():
                if form.username.data == user.username and form.password.data == user.password :
                    session['user'] = form.username
                    return render_template('affiche.html')
        return render_template('login.html', form=form)


@app.route('/product/', methods=['GET', 'POST'])
def product():
    form = ProductForm()
    product = Product()
    if form.validate_on_submit():
        product.name = form.name.data
        product.description = form.description.data
        product.category = form.category.data
        product.user_id = 1
        db.session.add(product)
        db.session.commit()
        return render_template('affiche.html')
    return render_template('product.html', form=form)


@app.route('/category/', methods=['GET', 'POST'])
def category():
    form = CategoryForm()
    category = Category()
    if request.method == 'POST':
        if form.validate():
            category.name = form.name.data
            category.description = form.description.data
            db.session.add(category)
            db.session.commit()
            return render_template('affiche.html')
    return render_template('category.html', form=form)


@app.route('/getsession/')
def getsession():
    if 'user' in session:
        return session['user']
    return 'not logged in'