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
# ROUTES
############################################################

@app.route('/')

def homepage():
=======
def home():
    # renders landing page
    return render_template('index.html')

@app.route('/bricks')
def legos_list():

    """Display the lego parts list page."""

    # lego_data = lego_collection.find()

    # context = {
    #     'legos': lego_data,
    # }
    # for when we move our FEW into a template

    return render_template('index-template.html')

@app.route('/login')
def login():
  return render_template('login-template.html')

@app.route('/account')
def account():

  context = {
    "loggedIn": True
  }
  return render_template('account-template.html', **context)

@app.route('/sets')
def sets():
  return render_template('sets-template.html')

@app.route('/bricks')
def bricks():
  return render_template('bricks-template.html')
=======
    return render_template('bricks.html', **context)


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

        return redirect(url_for('detail', lego_id=returned_obj.inserted_id))

    else:
        # for when we move our FEW into a template
        return render_template('add.html')

@app.route('/delete/<lego_id>', methods=['POST'])
def delete(lego_id):
    """ Deletes lego """

    lego_collection.delete_one({'_id': ObjectId(lego_id)})

    # for when we move our FEW into a template
    return redirect(url_for('legos_list'))

if __name__ == '__main__':
  app.run(debug=True)