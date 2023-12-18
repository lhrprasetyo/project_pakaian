import os 
from flask import Blueprint,render_template,redirect,request,flash,url_for
from extension import SQLAlchemy,db,datetime 

team_blueprint = Blueprint('team_blueprint',(__name__))

@team_blueprint.route('/team')
def team():
    return render_template('team.html')