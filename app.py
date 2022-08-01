import gspread
from oauth2client.service_account import ServiceAccountCredentials
from Tool import app, client, csrf
from Tool.forms import xino, schools
from flask import render_template,request, url_for, redirect,abort
from datetime import datetime
from gspread_formatting import *
from werkzeug.security import generate_password_hash,check_password_hash

@app.route('/', methods = ['GET', 'POST'])
def index():
    return(render_template('index.htm'))

@app.route('/events', methods = ['GET', 'POST'])
def events():
    return(render_template('events.htm'))

@app.route('/members', methods = ['GET', 'POST'])
def members():
    return(render_template('members.htm'))
@app.route('/school', methods = ['GET','POST'])
def school():
    form=schools()
    if form.validate_on_submit():
        sheet = client.open("Xino Registrations").worksheet('passwords')
        x=0
        try:
            x=sheet.find(form.school_username.data, in_column=3)
        except gspread.exceptions.CellNotFound:
            abort(403)
        if x:
            y = sheet.cell(x.row,4).value
            if(form.password.data==y):
                return redirect(url_for('register',school=form.school_username.data,hash=generate_password_hash(y)))

    return render_template('school.htm', form=form)

def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(2)))
    return str(len(str_list)+1)

@app.route('/register/<school>/<hash>', methods = ['GET', 'POST'])
def register(school,hash):
    ###############################checking hash password
    sheet = client.open("Xino Registrations").worksheet('passwords')
    y = sheet.cell(sheet.find(school, in_column=3).row,4).value
    if not(check_password_hash(hash,y)):
        abort(403)
    ##############################################
    form=xino()
    ##############################################schecking school in excel
    sheet_events = client.open("Xino Registrations").worksheet('events')
    next_events_row=1
    try:
        x=sheet_events.find(school, in_column=3)
        next_events_row = x.row
    except gspread.exceptions.CellNotFound:
        next_events_row = next_available_row(sheet_events)
        sheet_events.update_cell(next_events_row,2,school)
    #################################################checking form
    print('start')
    print(form.validate_on_submit())
    if form.validate_on_submit():
############################## GD
        sheet_events.update_cell(next_events_row,3,form.participant_gd_name.data)
        sheet_events.update_cell(next_events_row,4,form.participant_gd_email.data)
        sheet_events.update_cell(next_events_row,5,form.participant_gd_phone.data)
################################################################################### SURP
        sheet_events.update_cell(next_events_row,6,form.participant_su_name.data)
        sheet_events.update_cell(next_events_row,7,form.participant_su_email.data)
        sheet_events.update_cell(next_events_row,8,form.participant_su_phone.data)

        sheet_events.update_cell(next_events_row,9,form.participant_su2_name.data)
        sheet_events.update_cell(next_events_row,10,form.participant_su2_email.data)
        sheet_events.update_cell(next_events_row,11,form.participant_su2_phone.data)



    return render_template('register.htm' , form=form, sheet_events=sheet_events, next_events_row=next_events_row)

if __name__ == '__main__':
    app.run(debug = True)
