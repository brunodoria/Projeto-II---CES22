from flask import render_template, flash, redirect, url_for, Flask
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'MORENO'}
    return render_template('index.html', title='Home', user=user)

"""
@app.route('/login', methods=["GET", "POST"])
def login():
    # error = ''
    try:

        if request.method == "POST":

            attempted_username = request.form['username']
            attempted_password = request.form['password']

            # flash(attempted_username)
            # flash(attempted_password)

            if attempted_username == "admin" and attempted_password == "password":
                return redirect(url_for('index'))


            else:
                error = "Invalid credentials. Try Again."

        eturn
        render_template('login.html', title='Sign In', form=form)

    except Exception as e:
        # flash(e)
        eturn
        render_template('login.html', title='Sign In', form=form)

"""
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('cadastro.html', title='Register', form=form)