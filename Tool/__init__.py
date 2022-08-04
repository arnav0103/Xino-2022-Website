import os
from flask import Flask
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask_wtf.csrf import CSRFProtect
################
app = Flask(__name__)

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
app.config['SECRET_KEY'] = '$h1tz3c0'
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
creds1 = ServiceAccountCredentials.from_json_keyfile_name("creds1.json", scope)
csrf = CSRFProtect(app)
client = gspread.authorize(creds)
client1 = gspread.authorize(creds)
