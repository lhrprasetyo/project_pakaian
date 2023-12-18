import os
from flask import Flask,request,jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
migrate=Migrate()