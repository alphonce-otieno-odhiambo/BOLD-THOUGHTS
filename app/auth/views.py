
from flask import render_template, redirect, request, url_for, flash
from flask_login.utils import login_required, login_user, logout_user
from . import auth
from .forms import RegistrationForm, LoginForm
from ..models import User
from .. import db


@auth.route('/register', methods = ['GET', 'POST'])
def register():
    regis = RegistrationForm()
    if regis.validate_on_submit():
        user = User(email = regis.email.data, username = regis.username.data,password = regis.password.data)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('auth.login'))
    #title = 'Create account'
    return render_template('auth/register.html', register = regis)


@auth.route('/login', methods = ["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and User.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(url_for('main.index'))

        flash('invalid email or password')

    return render_template('auth/login.html', login_form = login_form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been successfully loged out')
    return redirect(url_for('main.index'))