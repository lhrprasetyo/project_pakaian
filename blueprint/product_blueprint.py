import os 
from flask import Blueprint,render_template,redirect,request,flash,url_for
from extension import SQLAlchemy,db,datetime 

product_blueprint = Blueprint('product_blueprint',(__name__))

@product_blueprint.route('/product')
def product():
    return render_template('product.html')