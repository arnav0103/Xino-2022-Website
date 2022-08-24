import gspread
from oauth2client.service_account import ServiceAccountCredentials
from Tool import app, client, csrf , client1, db
from Tool.forms import xino, schools , request_invite , LoginForm,RegistrationForm,PlayForm
from flask import render_template, request, url_for, redirect, abort
from flask_login import login_user,login_required,logout_user,current_user
from datetime import datetime
from gspread_formatting import *
import flask
from Tool.models import User, Questions, Logs
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import desc , asc
username =''
application = app
# import csv
#
# filename='cs_answers.csv'

@app.route('/', methods=['GET', 'POST'])
def index():
    # with open(filename, 'r') as csvfile:
    #     datareader = csv.reader(csvfile)
    #     for row in datareader:
    #         try:
    #             user = Questions(question=row[0],
    #                         answer=row[1],
    #                         source=row[2])
    #             user.imgur=row[3]
    #             db.session.add(user)
    #         except:
    #             continue
    #     db.session.commit()


    # user = Questions(answer='test',
    #             question='test',
    #             source='hahaha')
    # db.session.add(user)
    # db.session.commit()
    return(render_template('index.htm'))


@app.route('/events', methods=['GET', 'POST'])
def events():
    return(render_template('events.htm'))


@app.route('/members', methods=['GET', 'POST'])
def members():
    return(render_template('members.htm'))

@app.route('/alumini', methods=['GET', 'POST'])
def alumini():
    return(render_template('alumni.htm'))


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
    start_cell = gspread.utils.rowcol_to_a1(row, 3)
    end_cell = gspread.utils.rowcol_to_a1(row, 65)
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
        if x:
            next_events_row = x.row
        else:
            next_events_row = next_available_row(sheet_events)
            sheet_events.update_cell(next_events_row, 2, school)
    except gspread.exceptions.CellNotFound:
        print('hahaha')
        next_events_row = next_available_row(sheet_events)
        sheet_events.update_cell(next_events_row, 2, school)
    all = row_cells(sheet_events, next_events_row)
    if form.validate_on_submit():
        # GD
        all_response = [form.participant_gd1_name.data, form.participant_gd1_email.data, form.participant_gd1_phone.data, form.participant_su1_name.data, form.participant_su1_email.data, form.participant_su1_phone.data, form.participant_su2_name.data, form.participant_su2_email.data, form.participant_su2_phone.data, form.participant_cr1_name.data, form.participant_cr1_email.data, form.participant_cr1_phone.data, form.participant_cr2_name.data, form.participant_cr2_email.data, form.participant_cr2_phone.data, form.participant_cr3_name.data, form.participant_cr3_email.data, form.participant_cr3_phone.data, form.participant_cr4_name.data, form.participant_cr4_email.data, form.participant_cr4_phone.data, form.participant_cr5_name.data, form.participant_cr5_email.data, form.participant_cr5_phone.data, form.participant_cw1_name.data, form.participant_cw1_email.data, form.participant_cw1_phone.data, form.participant_cw2_name.data, form.participant_cw2_email.data, form.participant_cw2_phone.data, form.participant_pg1_name.data,form.participant_pg1_email.data, form.participant_pg1_phone.data, form.participant_pg2_name.data, form.participant_pg2_email.data, form.participant_pg2_phone.data, form.participant_hr1_name.data, form.participant_hr1_email.data, form.participant_hr1_phone.data, form.participant_hr2_name.data, form.participant_hr2_email.data, form.participant_hr2_phone.data, form.participant_hr3_name.data, form.participant_hr3_email.data, form.participant_hr3_phone.data, form.participant_gm1_name.data, form.participant_gm1_email.data, form.participant_gm1_phone.data, form.participant_gm2_name.data, form.participant_gm2_email.data, form.participant_gm2_phone.data, form.participant_gm3_name.data, form.participant_gm3_email.data, form.participant_gm3_phone.data, form.participant_ms1_name.data, form.participant_ms1_email.data, form.participant_ms1_phone.data, form.participant_cc1_name.data, form.participant_cc1_email.data, form.participant_cc1_phone.data, form.participant_cc2_name.data, form.participant_cc2_email.data, form.participant_cc2_phone.data]
        update = [all[0]]
        print(len(all))
        print(len(all_response))
        for i in range(len(all_response)):
            if all_response[i] != all[i].value:
                all[i].value = all_response[i]
                update.append(all[i])
        sheet_events.update_cells(update)
        return redirect(url_for('success',school=school,hash=hash))
    return render_template('register.htm', form=form, sheet_events=sheet_events, next_events_row=next_events_row, all=all)

@app.route('/success/<school>/<hash>', methods=['GET','POST'])
def success(school,hash):
    return render_template('success.htm',school=school,hash=hash)

@app.route('/req_invite', methods=['GET', 'POST'])
def req_invite():
    form = request_invite()
    sheet_requests = client1.open("Xino Registrations").worksheet('requests')
    text = ''
    if form.validate_on_submit():
        scul_email = form.email.data
        try:
            x = sheet_requests.find(scul_email, in_column=4)
            if x:
                text = 'Already registered on this email'
            else:
                next_events_row = next_available_row(sheet_requests)
                sheet_requests.update_cell(next_events_row,2,form.school_name.data)
                sheet_requests.update_cell(next_events_row,3, form.contact.data)
                sheet_requests.update_cell(next_events_row,4, scul_email)
                sheet_requests.update_cell(next_events_row,5, form.website.data)
                text = 'Invite Requested you will recieve the invite on the mail registered'
        except gspread.exceptions.CellNotFound:
            next_events_row = next_available_row(sheet_requests)
            sheet_requests.update_cell(next_events_row,2,form.school_name.data)
            sheet_requests.update_cell(next_events_row,3, form.contact.data)
            sheet_requests.update_cell(next_events_row,4, scul_email)
            sheet_requests.update_cell(next_events_row,5, form.website.data)
            text = 'Invite Requested you will recieve the invite on the mail registered'
    return render_template('request.htm', form=form , text=text)


################################################
@app.route('/xquest' )
def home():
    return render_template('HomePage.html')

@app.route('/logout' )
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'] )
def login():
    mess = 'Please fill form to login'
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        try:
            if user.check_password(form.password.data) and user is not None:
                #Log in the user

                login_user(user)
                mess = 'Logged in successfully.'
                current_user = user
                next = request.args.get('next')
                if next == None or not next[0]=='/':
                    next = url_for('home')
                return redirect(next)
            else:
                mess = "Wrong Password"
        except AttributeError:
            mess = 'No such login.Pls contact admins '
    print(mess)
    return render_template('Login.html', form=form,mess=mess)

@app.route('/register',methods=['GET','POST'] )
def registera():
    mess = 'Register to play the most exciting cryptic hunts ever'
    try:
        form = RegistrationForm()
        username = form.username.data
        password = form.password.data
        school = form.school.data

        if form.validate_on_submit():
            user = User(username,password,1,school)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
    except :
        mess = 'username or email already been used'
    return render_template('Register.html',form = form,mess=mess)


@app.route('/play',methods=['GET','POST'] )
@login_required
def play():
    # current_user.ip = flask.request.remote_addr
    # db.session.commit()
    # if current_user.restricted=="Yes":
    #     abort(403)
    # form = PlayForm()
    # mess = ""
    # max = Questions.query.order_by(Questions.id.desc())
    # questions = current_user.question
    # user = User.query.get(current_user.id)
    # if user.question > max[0].id:
    #     return "Congratulations and celeberations! Admins gonna contact"
    # question = Questions.query.get(user.question)
    # answers = form.answer.data
    # if form.validate_on_submit():
    #     if answers is not None:
    #         log = Logs(answer = answers.lower(),answer_time = datetime.now(),question = user.question,userid = current_user.id)
    #         db.session.add(log)
    #         db.session.commit()
    #         if answers.lower() == question.answer.lower():
    #             user.question += 1
    #             user.answer_time= datetime.now()
    #             db.session.add(user)
    #             db.session.commit()
    #             mess = "correct"
    #             return redirect(url_for('play'))
    #         else:
    #             mess = "wrong"
    # return render_template('play.html',form=form,use=questions,question=question.question,mess=mess,source = question.source,imgur = question.imgur)
    return render_template('HomePage.html')

@app.route('/leaderboard' )
@login_required
def leaderboard():
    all_users = User.query.order_by(User.question.desc(),User.answer_time.asc()).all()
    rank = []
    all = []
    l = 0
    current_user.ip = flask.request.remote_addr
    db.session.commit()
    for users in all_users:
        if users.restricted == "Yes" or users.username == "Xino":
            pass
        else:
            all.append(users)
    n = len(all)
    for i in all:
        rank.append(n)
        n -= 1
    restricted = User.query.filter_by(restricted="Yes")
    return render_template('leaderboard.html',all_users=all,rank=rank,restricted=restricted)

@app.route('/admin_panel',methods=['GET','POST'] )
@login_required
def admin():
    if current_user.username != 'Xino':
        abort(403)
    else:
        all_logs = Logs.query.order_by(Logs.id.desc())
        return render_template("admin_panel.htm",all_logs=all_logs)

@app.route('/profile/<username>',methods = ['GET','POST'] )
@login_required
def profile(username):
    if current_user.username != 'Xino':
        abort(403)
    user = User.query.filter_by(id=username)
    logs = []
    if user:
        if user[0].logs:
            for i in user[0].logs:
                logs.append(i)
    logs.reverse()
    return render_template("profile.htm",user=user[0],logs=logs)

@app.route('/restrict/<username>',methods = ['GET','POST'] )
@login_required
def ban(username):
    if current_user.username != 'Xino':
        abort(403)
    all = User.query.filter_by(id = username)
    if all:
        all[0].restricted = "Yes"
        db.session.commit()
        return redirect(url_for('admin'))
    return abort(404)

@app.route('/unrestrict/<username>',methods = ['GET','POST'] )
@login_required
def unban(username):
    if current_user.username != 'Xino':
        abort(403)
    all = User.query.filter_by(id = username)
    if all:
        all[0].restricted = "No"
        db.session.commit()
        return redirect(url_for('admin'))
    return abort(404)

@app.errorhandler(404)
def page_not_found(e):
  return render_template('error_404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
