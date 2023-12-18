import os
from flask import Flask 
from extension import *
from blueprint import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=\
    'mysql+pymysql://localhost:password@localhost/data_pakaian'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY'] = 'freya'
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

db.init_app(app)

app.register_blueprint(home_blueprint)
app.register_blueprint(product_blueprint)
app.register_blueprint(team_blueprint)
app.register_blueprint(contact_blueprint)

if __name__ == "__main__":
    app.run(debug =True)