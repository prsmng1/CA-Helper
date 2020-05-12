from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_mail import *
app=Flask(__name__,static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:@localhost/chartacct"
db=SQLAlchemy(app)
app.secret_key="2#@$*&HGGFHg"
