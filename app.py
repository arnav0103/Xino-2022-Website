import gspread
from oauth2client.service_account import ServiceAccountCredentials
from Tool import app, client, csrf
from Tool.forms import xino, schools
from flask import render_template, request, url_for, redirect, abort
from datetime import datetime
from gspread_formatting import *
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/', methods=['GET', 'POST'])
def index():
    return(render_template('index.htm'))


@app.route('/events', methods=['GET', 'POST'])
def events():
    return(render_template('events.htm'))


@app.route('/members', methods=['GET', 'POST'])
def members():
    return(render_template('members.htm'))


@app.route('/school', methods=['GET', 'POST'])
def school():
    form = schools()
    if form.validate_on_submit():
        sheet = client.open("Xino Registrations").worksheet('passwords')
        x = 0
        try:
            x = sheet.find(form.school_username.data, in_column=3)
        except gspread.exceptions.CellNotFound:
            abort(403)
        if x:
            y = sheet.cell(x.row, 4).value
            if(form.password.data == y):
                return redirect(url_for('register', school=form.school_username.data, hash=generate_password_hash(y)))

    return render_template('school.htm', form=form)


def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(2)))
    return str(len(str_list)+1)


@app.route('/register/<school>/<hash>', methods=['GET', 'POST'])
def register(school, hash):
    # checking hash password
    sheet = client.open("Xino Registrations").worksheet('passwords')
    y = sheet.cell(sheet.find(school, in_column=3).row, 4).value
    if not(check_password_hash(hash, y)):
        abort(403)
    ##############################################
    form = xino()
    # schecking school in excel
    sheet_events = client.open("Xino Registrations").worksheet('events')
    next_events_row = 1
    try:
        x = sheet_events.find(school, in_column=3)
        next_events_row = x.row
    except gspread.exceptions.CellNotFound:
        next_events_row = next_available_row(sheet_events)
        sheet_events.update_cell(next_events_row, 2, school)
# checking form
    print('start')
    print(form.validate_on_submit())
    if form.validate_on_submit():
        # GD
        sheet_events.update_cell(
            next_events_row, 3, form.participant_gd1_name.data)
        sheet_events.update_cell(
            next_events_row, 4, form.participant_gd1_email.data)
        sheet_events.update_cell(
            next_events_row, 5, form.participant_gd1_phone.data)


# SURP
        sheet_events.update_cell(
            next_events_row, 6, form.participant_su1_name.data)
        sheet_events.update_cell(
            next_events_row, 7, form.participant_su1_email.data)
        sheet_events.update_cell(
            next_events_row, 8, form.participant_su1_phone.data)

        sheet_events.update_cell(
            next_events_row, 9, form.participant_su2_name.data)
        sheet_events.update_cell(
            next_events_row, 10, form.participant_su2_email.data)
        sheet_events.update_cell(
            next_events_row, 11, form.participant_su2_phone.data)


# creative
        sheet_events.update_cell(
            next_events_row, 12, form.participant_cr1_name.data)
        sheet_events.update_cell(
            next_events_row, 13, form.participant_cr1_email.data)
        sheet_events.update_cell(
            next_events_row, 14, form.participant_cr1_phone.data)

        sheet_events.update_cell(
            next_events_row, 15, form.participant_cr2_name.data)
        sheet_events.update_cell(
            next_events_row, 16, form.participant_cr2_email.data)
        sheet_events.update_cell(
            next_events_row, 17, form.participant_cr2_phone.data)

        sheet_events.update_cell(
            next_events_row, 18, form.participant_cr3_name.data)
        sheet_events.update_cell(
            next_events_row, 19, form.participant_cr3_email.data)
        sheet_events.update_cell(
            next_events_row, 20, form.participant_cr3_phone.data)

        sheet_events.update_cell(
            next_events_row, 21, form.participant_cr4_name.data)
        sheet_events.update_cell(
            next_events_row, 22, form.participant_cr4_email.data)
        sheet_events.update_cell(
            next_events_row, 23, form.participant_cr4_phone.data)

        sheet_events.update_cell(
            next_events_row, 24, form.participant_cr5_name.data)
        sheet_events.update_cell(
            next_events_row, 25, form.participant_cr5_email.data)
        sheet_events.update_cell(
            next_events_row, 26, form.participant_cr5_phone.data)


# crossword
        sheet_events.update_cell(
            next_events_row, 27, form.participant_cw1_name.data)
        sheet_events.update_cell(
            next_events_row, 28, form.participant_cw1_email.data)
        sheet_events.update_cell(
            next_events_row, 29, form.participant_cw1_phone.data)

        sheet_events.update_cell(
            next_events_row, 30, form.participant_cw2_name.data)
        sheet_events.update_cell(
            next_events_row, 31, form.participant_cw2_email.data)
        sheet_events.update_cell(
            next_events_row, 32, form.participant_cw2_phone.data)

# prog
        sheet_events.update_cell(
            next_events_row, 33, form.participant_pg1_name.data)
        sheet_events.update_cell(
            next_events_row, 34, form.participant_pg1_email.data)
        sheet_events.update_cell(
            next_events_row, 35, form.participant_pg1_phone.data)

        sheet_events.update_cell(
            next_events_row, 36, form.participant_pg2_name.data)
        sheet_events.update_cell(
            next_events_row, 37, form.participant_pg2_email.data)
        sheet_events.update_cell(
            next_events_row, 38, form.participant_pg2_phone.data)

# hardware
        sheet_events.update_cell(
            next_events_row, 39, form.participant_hr1_name.data)
        sheet_events.update_cell(
            next_events_row, 40, form.participant_hr1_email.data)
        sheet_events.update_cell(
            next_events_row, 41, form.participant_hr1_phone.data)

        sheet_events.update_cell(
            next_events_row, 42, form.participant_hr2_name.data)
        sheet_events.update_cell(
            next_events_row, 43, form.participant_hr2_email.data)
        sheet_events.update_cell(
            next_events_row, 44, form.participant_hr2_phone.data)

        sheet_events.update_cell(
            next_events_row, 45, form.participant_hr3_name.data)
        sheet_events.update_cell(
            next_events_row, 46, form.participant_hr3_email.data)
        sheet_events.update_cell(
            next_events_row, 47, form.participant_hr3_phone.data)


# game dev
        sheet_events.update_cell(
            next_events_row, 48, form.participant_gm1_name.data)
        sheet_events.update_cell(
            next_events_row, 49, form.participant_gm1_email.data)
        sheet_events.update_cell(
            next_events_row, 50, form.participant_gm1_phone.data)

        sheet_events.update_cell(
            next_events_row, 51, form.participant_gm2_name.data)
        sheet_events.update_cell(
            next_events_row, 52, form.participant_gm2_email.data)
        sheet_events.update_cell(
            next_events_row, 53, form.participant_gm2_phone.data)

        sheet_events.update_cell(
            next_events_row, 54, form.participant_gm3_name.data)
        sheet_events.update_cell(
            next_events_row, 55, form.participant_gm3_email.data)
        sheet_events.update_cell(
            next_events_row, 56, form.participant_gm3_phone.data)

# musical shutter
        sheet_events.update_cell(
            next_events_row, 57, form.participant_ms1_name.data)
        sheet_events.update_cell(
            next_events_row, 58, form.participant_ms1_email.data)
        sheet_events.update_cell(
            next_events_row, 59, form.participant_ms1_phone.data)

# camcord
        sheet_events.update_cell(
            next_events_row, 60, form.participant_cc1_name.data)
        sheet_events.update_cell(
            next_events_row, 61, form.participant_cc1_email.data)
        sheet_events.update_cell(
            next_events_row, 62, form.participant_cc1_phone.data)

    return render_template('register.htm', form=form, sheet_events=sheet_events, next_events_row=next_events_row)


if __name__ == '__main__':
    app.run(debug=True)
