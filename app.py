from flask import Flask, request, redirect, render_template, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from pymongo import MongoClient
import pymongo

""" Modeled after Web1.1 plant database assignment """
############################################################
# SETUP
############################################################

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/legosDatabase"
mongo = PyMongo(app)

lego_collection = mongo.db.legos

############################################################
# MAIN ROUTES
############################################################

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/account')
def account():

  context = {
    "loggedIn": True
  }
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

# This route might eventually replace our current account route
@app.route('/update/<lego_id>', methods=['GET', 'POST'])
def update(lego_id):
  """ Updates lego """

  if request.method == 'POST':
    # currently only updates one lego brick at a time (for if we want individual update buttons)
    lego_collection.update_one({'_id': ObjectId(lego_id)}),{'$set': {
      'quantity': request.form.get('quantity')
      }}

  # redirects to account.html (our user's database)
    return redirect(url_for('account'))
  else:
    # returns every lego brick in our collection
    legos_to_show = lego_collection.find({})

    context = {
      'legos': legos_to_show,
      "loggedIn": True
    }

    # redirects to account.html (our user's database)
    return render_template('account.html', **context)

if __name__ == '__main__':
  app.run(debug=True)