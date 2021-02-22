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

@app.route('/about')
def about():
  return render_template('about.html')

@main.route('/')
def homepage():
    '''Homepage route'''
    return render_template('index.html')

@app.route('/account')
def account():

  # returns every lego brick in our collection
  legos_to_show = lego_collection.find({})

  context = {
    'legos': legos_to_show,
    "loggedIn": True
  }

  # renders account.html (our user's database)
  return render_template('account.html', **context)

@app.route('/sets')
def sets():
  return render_template('sets.html')

@app.route('/bricks')
def bricks():
  return render_template('bricks.html')

############################################################
# DATABASE ROUTES (currently only modifies bricks-list)
############################################################

@app.route('/add', methods=['GET', 'POST'])
def add():
    """Display the lego add page & process data from the add form."""

    if request.method == 'POST':
        new_lego = {
            'name': request.form.get('lego_name'),
            'model_number': request.form.get('model_number'),
            'model_name': request.form.get('model_name'),
            'photo_url': request.form.get('photo'),
            'quantity': request.form.get('quantity')
        }
        returned_obj = lego_collection.insert_one(new_lego)

        return redirect(url_for('account', lego_id=returned_obj.inserted_id))

    else:
        # redirects to account.html (our user's database)
        return render_template('account.html')

@app.route('/delete/<lego_id>', methods=['POST'])
def delete(lego_id):
    """ Deletes lego """

    lego_collection.delete_one({'_id': ObjectId(lego_id)})

    # redirects to account.html (our user's database)
    return redirect(url_for('account'))

@app.route('/update/<lego_id>', methods=['POST'])
def update(lego_id):
  """ Updates lego """

  # currently only updates one lego brick at a time (for if we want individual update buttons)
  lego_collection.update_one({'_id': ObjectId(lego_id)}),{'$set': {
    'quantity': request.form.get('quantity')
    }}

  # redirects to account.html (our user's database)
  return redirect(url_for('account'))

if __name__ == '__main__':
  app.run(debug=True)
