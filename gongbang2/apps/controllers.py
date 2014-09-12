# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, flash, g, session
from werkzeug.security import generate_password_hash, \
     check_password_hash
from sqlalchemy import desc
from apps import app, db
from apps.forms import JoinForm, LoginForm
from apps.models import (
    User
)

#
#@before request
#
@app.before_request
def befor_request():
    g.user_name = None

    if 'user_id' in session:
        g.user_id = session['user_name']
        g.user_password = session['user_password']


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

#
# @Join controllers
#
@app.route('/join', methods=['GET', 'POST'])
def user_join():
    form = JoinForm()

    if request.method == 'POST':
        if form.validate_on_submit():

        id = request.form['id']
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']

        user = User(
            email=email,
            password=generate_password_hash(password),
            name=name
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('index'))
    #if GET
    return render_template('join.html')


#
# @Login controllers
#
@app.route('/login', methods=['GET','POST'])
def log_in():
    form = LoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():

            id = request.form["id"]
            password = request.form["password"]

            user = User.query.get(id)

            #message = None

            if user is None:
                flash (u'user가 존재하지 않습니다', 'danger')
            elif not check_password_hash(user.password, password):
               flash(u'password가 잘못되었습니다.','danger')

            else:
                session.permanent = True
                session['user_id'] = user.email
                session['user_name'] = user.name

                flash(u'로그인 완료', 'success')

                return redirect(url_for('main'))
                
    #if GET
    return render_template('index.html', form = form, active_tab = 'log_in')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/logout')
def log_out():
    session.clear()
    #if GET
    return redirect(url_for('index'))