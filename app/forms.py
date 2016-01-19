from flask.ext.wtf import Form

from wtforms_alchemy import model_form_factory

from server import db
from models import Bookmate, Category, User


BaseModelForm = model_form_factory(Form)

class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session


class UserCreateForm(ModelForm):
    class Meta:
        model = User


class BookmateForm(ModelForm):
    class Meta:
        model = Bookmate


class CategoryForm(ModelForm):
	class Meta:
		model = Category
