from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError
from legos_app.models import LegoSet, LegoBrick

class LegoBrickForm(FlaskForm):
  ''' Form to create a Lego Brick '''
  name = StringField('Brick Name', validators=[DataRequired(), Length(min=3, max=80)])
  brick_id = StringField('Brick ID', validators=[DataRequired()])
  quantity = IntegerField('Quantity', validators=[DataRequired()])
  photo_url = StringField('Photo URL', validators=[DataRequired()])
  submit = SubmitField('Submit')

class LegoSetForm(FlaskForm):
  ''' Form to create a Lego Set '''
  name = StringField('Set Name', validators=[DataRequired(), Length(min=3, max=80)])
  set_id = StringField('Set ID', validators=[DataRequired()])
  photo_url = StringField('Photo URL', validators=[DataRequired()])
  submit = SubmitField('Submit')
