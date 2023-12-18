import os 
from flask import Blueprint,render_template,redirect,request,flash,url_for
from extension import SQLAlchemy,db,datetime 

contact_blueprint = Blueprint('contact_blueprint',(__name__))

@contact_blueprint.route('/contact')
def contact():
    return render_template('contact.html')