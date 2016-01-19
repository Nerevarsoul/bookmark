from flask import g, jsonify, request, render_template
from flask.ext import restful

from server import api, app, db, flask_bcrypt, auth
from models import Category, User
from forms import CategoryForm, UserCreateForm
from serializers import user_schema


@app.route('/')
def index_view():
    return render_template('index.html')


@app.route('/category', methods=['GET', 'POST'])
def add_category():

    error = None
    form = CategoryForm()
    
    if request.method == 'POST':
        form = CategoryForm(request.form)
        if form.validate_on_submit():
            category = Category(name=form.name.data)
            db.session.add(category)
            db.session.commit()
        else:
            error = 'Invalid username or password.'
        
    categories = Category.query.all()

    return render_template('category.html', form=form, categories=categories, error=error)