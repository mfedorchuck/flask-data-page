from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, RecordForm, PostForm, MultiPostForm
from app.models import Post
from app.worker_local import UserData


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    user = {'username': 'guest'}
    form = PostForm()

    if form.validate_on_submit():
        data = UserData()
        data.savedata(form.post.data)

        flash('You data has been properly recorded locally')
        return redirect(url_for('index'))

    permissions = [
        {
            "username": "guest",
            "body": "read and send data",
            "id": 1
        },
        {
            "username": "admin",
            "body": "read, collect by api, send and modify data",
            "id": 2
        }
    ]
    return render_template('index.html', title='Home', user=user, permissions=permissions, form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',  title='Sign In', form=form)


@app.route('/datasender', methods=['GET', 'POST'])
def datasender():
    form = PostForm()
    user = "guest"

    if form.validate_on_submit():
        data = UserData()
        storage_respond = data.data_record(data=form.post.data, user=user)

        flash(storage_respond)
        return redirect(url_for('datasender'))

    return render_template('datasender.html', title='Leave the data', form=form)


@app.route('/multidata', methods=['GET', 'POST'])
def multidata():
    form = MultiPostForm()

    if form.validate_on_submit():
        data = UserData()
        storage_respond = data.data_record(data=form.title.data, user='user')

        flash(storage_respond)
        return redirect(url_for('multidata'))


    return render_template('multidata.html', title='Explore', form=form)
