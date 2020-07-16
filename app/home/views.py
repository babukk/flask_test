
from flask import render_template
from flask_login import login_required, current_user

from . import home


@home.route('/')
def homepage():
    if current_user.is_authenticated:
        print('----------->>> is_authenticated <<<----------------------')
    else:
        print('----------->>> ANONYNOUS <<<----------------------')
    return render_template('home/index.html', title="Добро пожаловать")


@home.route('/dashboard')
@login_required
def dashboard():
    if current_user.is_authenticated:
        print('----------->>> is_authenticated <<<----------------------')
    else:
        print('----------->>> ANONYNOUS <<<----------------------')
    return render_template('home/dashboard.html', title="Рабочая область")
