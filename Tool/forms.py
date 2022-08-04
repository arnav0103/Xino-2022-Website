from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, StringField, DateField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Email


class schools(FlaskForm):
    school_username = StringField(
        'username bhardo pls', validators=[DataRequired()])
    password = PasswordField('Password :smirk:', validators=[DataRequired()])
    submit = SubmitField('Submit')


class xino(FlaskForm):
    # GD
    participant_gd1_name = StringField('Participant 1 Name')
    participant_gd1_email = StringField('Participant 1 Email')
    participant_gd1_phone = StringField('Participant 1 Phone')
# SURP
    participant_su1_name = StringField('Participant 1 Name')
    participant_su1_email = StringField('Participant 1 Email')
    participant_su1_phone = StringField('Participant 1 Phone')

    participant_su2_name = StringField('Participant 2 Name')
    participant_su2_email = StringField('Participant 2 Email')
    participant_su2_phone = StringField('Participant 2 Phone')
# CREATIVE
    participant_cr1_name = StringField('Participant 1 Name')
    participant_cr1_email = StringField('Participant 1 Email')
    participant_cr1_phone = StringField('Participant 1 Phone')

    participant_cr2_name = StringField('Participant 2 Name')
    participant_cr2_email = StringField('Participant 2 Email')
    participant_cr2_phone = StringField('Participant 2 Phone')

    participant_cr3_name = StringField('Participant 2 Name')
    participant_cr3_email = StringField('Participant 2 Email')
    participant_cr3_phone = StringField('Participant 2 Phone')

    participant_cr4_name = StringField('Participant 1 Name')
    participant_cr4_email = StringField('Participant 1 Email')
    participant_cr4_phone = StringField('Participant 1 Phone')

    participant_cr5_name = StringField('Participant 2 Name')
    participant_cr5_email = StringField('Participant 2 Email')
    participant_cr5_phone = StringField('Participant 2 Phone')
# CROSS
    participant_cw1_name = StringField('Participant 1 Name')
    participant_cw1_email = StringField('Participant 1 Email')
    participant_cw1_phone = StringField('Participant 1 Phone')

    participant_cw2_name = StringField('Participant 2 Name')
    participant_cw2_email = StringField('Participant 2 Email')
    participant_cw2_phone = StringField('Participant 2 Phone')
# PROG
    participant_pg1_name = StringField('Participant 1 Name')
    participant_pg1_email = StringField('Participant 1 Email')
    participant_pg1_phone = StringField('Participant 1 Phone')

    participant_pg2_name = StringField('Participant 2 Name')
    participant_pg2_email = StringField('Participant 2 Email')
    participant_pg2_phone = StringField('Participant 2 Phone')
# HARDWARE
    participant_hr1_name = StringField('Participant 1 Name')
    participant_hr1_email = StringField('Participant 1 Email')
    participant_hr1_phone = StringField('Participant 1 Phone')

    participant_hr2_name = StringField('Participant 2 Name')
    participant_hr2_email = StringField('Participant 2 Email')
    participant_hr2_phone = StringField('Participant 2 Phone')

    participant_hr3_name = StringField('Participant 2 Name')
    participant_hr3_email = StringField('Participant 2 Email')
    participant_hr3_phone = StringField('Participant 2 Phone')
# GAME DEV
    participant_gm1_name = StringField('Participant 1 Name')
    participant_gm1_email = StringField('Participant 1 Email')
    participant_gm1_phone = StringField('Participant 1 Phone')

    participant_gm2_name = StringField('Participant 2 Name')
    participant_gm2_email = StringField('Participant 2 Email')
    participant_gm2_phone = StringField('Participant 2 Phone')

    participant_gm3_name = StringField('Participant 2 Name')
    participant_gm3_email = StringField('Participant 2 Email')
    participant_gm3_phone = StringField('Participant 2 Phone')
# MUSICAL SHUTER
    participant_ms1_name = StringField('Participant 1 Name')
    participant_ms1_email = StringField('Participant 1 Email')
    participant_ms1_phone = StringField('Participant 1 Phone')
# CAMCORD
    participant_cc1_name = StringField('Participant 1 Name')
    participant_cc1_email = StringField('Participant 1 Email')
    participant_cc1_phone = StringField('Participant 1 Phone')

    participant_cc2_name = StringField('Participant 1 Name')
    participant_cc2_email = StringField('Participant 1 Email')
    participant_cc2_phone = StringField('Participant 1 Phone')

    submit = SubmitField('Submit')

class request_invite(FlaskForm):
    school_name = StringField('School Name' , validators=[DataRequired()])
    contact = IntegerField('Contact of Teacher Incharge', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    website = StringField('School Website', validators=[DataRequired()])

    submit = SubmitField('Submit')
