''' Create database models to represent tables '''
from legos_app import db
from flask_login import UserMixin

class LegoBrick(db.Model):
  '''Lego Brick Model '''
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(200), nullable=False)
  brick_id = db.Column(db.String(80), nullable=False)
  quantity = db.Column(db.Integer, nullable=False)
  photo_url = db.Column(db.Integer, nullable=False)

class LegoSet(db.Model):
  '''Lego Set Model '''
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(200), nullable=False)
  set_id = db.Column(db.String(80), nullable=False)
  photo_url = db.Column(db.Integer, nullable=False)

class User(UserMixin, db.Model):
    ''' User Model '''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<User: {self.username}>'