import os
from flask import Flask
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import dns
from flask_migrate import Migrate
################
login_manager = LoginManager()
app = Flask(__name__)

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
app.config['SECRET_KEY'] = '$h1tz3c0'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SERVER_NAME'] = "localhost:5000"

db = SQLAlchemy(app)
Migrate(app,db)

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
creds1 = ServiceAccountCredentials.from_json_keyfile_name("creds1.json", scope)
csrf = CSRFProtect(app)
client = gspread.authorize(creds)
client1 = gspread.authorize(creds)

login_manager.init_app(app)
login_manager.login_view = 'login'
