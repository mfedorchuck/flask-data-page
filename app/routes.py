from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, RecordForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'guest'}
    permissions = [
        {
            "username": "guest",
            "body": "read, send"
        },
        {
            "username": "admin",
            "body": "read, collect by api, send, modify"
        }
    ]
    return render_template('index.html', title='Home', user=user, permissions=permissions)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',  title='Sign In', form=form)



@app.route('/datasender')
def datasender():
    form = RecordForm()
    return render_template('datasender.html', title='Leave the data', form=form)

