from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, StringField , DateField, PasswordField
from wtforms.validators import DataRequired , Email

class schools(FlaskForm):
    school_username = StringField('username bhardo pls', validators=[DataRequired()])
    password = PasswordField('Password :smirk:' , validators=[DataRequired()])
    submit = SubmitField('Submit')

class xino(FlaskForm):
    participant_gd_name=StringField('Participant 1 Name')
    participant_gd_email=StringField('Participant 1 Email')
    participant_gd_phone=StringField('Participant 1 Phone')
#########################
    participant_su_name=StringField('Participant 1 Name')
    participant_su_email=StringField('Participant 1 Email')
    participant_su_phone=StringField('Participant 1 Phone')

    participant_su2_name=StringField('Participant 2 Name')
    participant_su2_email=StringField('Participant 2 Email')
    participant_su2_phone=StringField('Participant 2 Phone')
###########################

    submit = SubmitField('Submit')
