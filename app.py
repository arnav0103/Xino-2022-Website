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

def row_cells(worksheet, row):
    """Returns a range of cells in a `worksheet`'s column `col`."""
    start_cell = gspread.utils.rowcol_to_a1(row,3)
    end_cell = gspread.utils.rowcol_to_a1(row,62)
    return worksheet.range('%s:%s' % (start_cell, end_cell))

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
        x = sheet_events.find(school, in_column=2)
        next_events_row = x.row
    except gspread.exceptions.CellNotFound:
        next_events_row = next_available_row(sheet_events)
        sheet_events.update_cell(next_events_row, 2, school)
    values = sheet_events.row_values(next_events_row)[2:-1]
    all = row_cells(sheet_events,next_events_row)
    if form.validate_on_submit():
        # GD
        all_response = [form.participant_gd1_name.data, form.participant_gd1_email.data, form.participant_gd1_phone.data, form.participant_su1_name.data, form.participant_su1_email.data, form.participant_su1_phone.data, form.participant_su2_name.data, form.participant_su2_email.data, form.participant_su2_phone.data, form.participant_cr1_name.data, form.participant_cr1_email.data, form.participant_cr1_phone.data, form.participant_cr2_name.data, form.participant_cr2_email.data, form.participant_cr2_phone.data, form.participant_cr3_name.data, form.participant_cr3_email.data, form.participant_cr3_phone.data, form.participant_cr4_name.data, form.participant_cr4_email.data, form.participant_cr4_phone.data, form.participant_cr5_name.data, form.participant_cr5_email.data, form.participant_cr5_phone.data, form.participant_cw1_name.data, form.participant_cw1_email.data, form.participant_cw1_phone.data, form.participant_cw2_name.data, form.participant_cw2_email.data, form.participant_cw2_phone.data, form.participant_pg1_name.data, form.participant_pg1_email.data, form.participant_pg1_phone.data, form.participant_pg2_name.data, form.participant_pg2_email.data, form.participant_pg2_phone.data, form.participant_hr1_name.data, form.participant_hr1_email.data, form.participant_hr1_phone.data, form.participant_hr2_name.data, form.participant_hr2_email.data, form.participant_hr2_phone.data, form.participant_hr3_name.data, form.participant_hr3_email.data, form.participant_hr3_phone.data, form.participant_gm1_name.data, form.participant_gm1_email.data, form.participant_gm1_phone.data, form.participant_gm2_name.data, form.participant_gm2_email.data, form.participant_gm2_phone.data, form.participant_gm3_name.data, form.participant_gm3_email.data, form.participant_gm3_phone.data, form.participant_ms1_name.data, form.participant_ms1_email.data, form.participant_ms1_phone.data, form.participant_cc1_name.data, form.participant_cc1_email.data, form.participant_cc1_phone.data]
        update = [all[0]]
        for i in range(len(all_response)):
            if all_response[i] != values[i]:
                all[i].value = all_response[i]
                update.append(all[i])
        sheet_events.update_cells(update)
    return render_template('register.htm', form=form, sheet_events=sheet_events, next_events_row=next_events_row,values=values)

if __name__ == '__main__':
    app.run(debug=True)
