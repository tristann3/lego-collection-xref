''' Import packages and modules '''
from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user

from legos_app.models import User, LegoBrick, LegoSet
from legos_app.main.forms import LegoBrickForm, LegoSetForm
from legos_app import bcrypt

# Import app and db from events_app package so that we can run app
from legos_app import app, db

main = Blueprint("main", __name__)


############################################################
# MAIN ROUTES
############################################################

@main.route('/about')
def about():
  return render_template('about.html')

@main.route('/')
def homepage():
    '''Homepage route'''
    return render_template('index.html')

@main.route('/sets')
@login_required
def sets():
  return render_template('sets.html')

@main.route('/bricks')
@login_required
def bricks():
  form = LegoBrickForm()
  brick_list = LegoBrick.query.all()
  return render_template('bricks.html', brick_list=brick_list, form=form)

############################################################
# DATABASE ROUTES (currently only modifies bricks-list)
############################################################

@main.route('/bricks/add', methods=['GET', 'POST'])
@login_required
def add():
    """Route to create and add a LEGO brick to the user's collection"""
    form = LegoBrickForm()
    
    # if form was submitted and contained no errors
    if form.validate_on_submit():
        new_brick = LegoBrick(
          name=form.name.data,
          brick_id=form.brick_id.data,
          quantity=form.quantity.data,
          photo_url=form.photo_url.data,
        )
        db.session.add(new_brick)
        db.session.commit()

        # redirects to bricks.html (our user's database)
        return redirect(url_for("main.bricks", lego_id=new_brick.id))
    # returns add-brick form
    return render_template('add.html', form=form)

@main.route('/bricks/delete/<lego_id>', methods=['POST'])
@login_required
def delete(lego_id):
    """ Deletes lego """

    item = LegoBrick.query.get(lego_id)
    db.session.delete(item)
    db.session.commit()
    # redirects to bricks.html (our user's database)
    return redirect(url_for("main.bricks"))

@main.route('/bricks/update/<lego_id>', methods=['POST'])
@login_required
def update(lego_id):
  """ Updates lego """

  # currently only updates one lego brick at a time (for if we want individual update buttons)
  item = LegoBrick.query.get(lego_id)
  form = LegoBrickForm(obj=item)
  
  form.populate_obj(item)
  db.session.add(item)
  db.session.commit()

  # redirects to bricks.html (our user's database)
  return redirect(url_for("main.bricks"))

if __name__ == '__main__':
  app.run(debug=True)
