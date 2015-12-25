from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from server import app, db
from models import User, Post

# Flask-Admin
admin = Admin(app, name='bookmate', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))