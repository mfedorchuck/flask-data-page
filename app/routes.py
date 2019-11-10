from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, RecordForm, PostForm, MultiPostForm
from app.models import Post, User
from app.worker_local import UserData
from app.worker_s3 import DataFile


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


@app.route('/show_data', methods=['GET', 'POST'])
def show_data():
    form = PostForm()
    user = "guest"

    if form.validate_on_submit():
        data = UserData()
        storage_respond = data.data_record(data=form.post.data, user=user)
        flash(storage_respond)

        return redirect(url_for('show_data'))

    return render_template('show_data.html', title='Leave the data', form=form)


@app.route('/multidata', methods=['GET', 'POST'])
def multidata():
    form = MultiPostForm()

    if form.validate_on_submit():
        data = DataFile()
        data.data_record(
            title=form.title.data,
            categoty=form.category.data,
            user_case=form.userCase.data,
            text=form.text.data
        )

        return redirect(url_for('multidata'))

    return render_template('multidata.html', title='Explore', form=form)


@app.route('/more')
def more():
    return render_template('more.html')
