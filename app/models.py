from wtforms.validators import Email

from server import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False, info={'validators': Email()})
    password = db.Column(db.String(80), nullable=False)

    # def __init__(self, email, password):
    # self.email = email
    # self.password = flask_bcrypt.generate_password_hash(password)

    def __repr__(self):
        return '<User %r>' % self.email
        
tags = db.Table('tags',
                db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
                db.Column('bookmate_id', db.Integer, db.ForeignKey('bookmate.id'))
                )


class Bookmate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    url = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    tags = db.relationship('Tag', secondary=tags,
                           backref=db.backref('bookmates', lazy='dynamic'))

    def __repr__(self):
        return self.title
    
    
class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __repr__(self):
        return self.title
    
    
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    tags = db.relationship('Tag', backref='category', lazy='dynamic')

    def __repr__(self):
        return self.name
