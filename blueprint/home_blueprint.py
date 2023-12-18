import os 
from flask import Blueprint,render_template,redirect,request,flash,url_for
from extension import SQLAlchemy,db,datetime 

home_blueprint = Blueprint('home_blueprint',(__name__))

@home_blueprint.route('/shop')
def shop():
    return render_template('home.html')