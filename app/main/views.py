from app import db
from . import main
from flask import render_template, request, redirect, url_for, flash, make_response, session, current_app
from flask_login import login_required, login_user,current_user, logout_user
from app.models import User
from .forms import LoginForm
# from .utils import send_mail

@main.route('/')
def index():
    return render_template('index.html', name='Jerry')


@main.route('/user/<int:user_id>/')
def user_profile(user_id):
    return "Profile page of user #{}".format(user_id)


@main.route('/books/<genre>/')
def books(genre):
    return "All Books in {} category".format(genre)


@main.route('/login/', methods=['post', 'get'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('.admin'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.query(User).filter(
            User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('.admin'))

        flash("Invalid username/password", 'error')
        return redirect(url_for('.login'))
    return render_template('login.html', form=form)


@main.route('/logout/')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('.login'))


@main.route('/cookie/')
def cookie():
    if not request.cookies.get('foo'):
        res = make_response("Setting a cookie")
        res.set_cookie('foo', 'bar', max_age=60*60*24*365*2)
    else:
        res = make_response("Value of cookie foo is {}".format(
            request.cookies.get('foo')))
    return res


@main.route('/delete-cookie/')
def delete_cookie():
    res = make_response("Cookie Removed")
    res.set_cookie('foo', 'bar', max_age=0)
    return res


@main.route('/article/', methods=['POST',  'GET'])
def article():
    if request.method == 'POST':
        print(request.form)
        res = make_response("")
        res.set_cookie("font", request.form.get('font'), 60*60*24*15)
        res.headers['location'] = url_for('.article')
        return res, 302

    return render_template('article.html')


@main.route('/visits-counter/')
def visits():
    if 'visits' in session:
        # чтение и обновление данных сессии yeeeshka
        session['visits'] = session.get('visits') + 1
    else:
        session['visits'] = 1  # настройка данных сессии
    return "Total visits: {}".format(session.get('visits'))


@main.route('/session/')
def updating_session():
    res = str(session.items())

    cart_item = {'pineapples': '10', 'apples': '20', 'mangoes': '30'}
    if 'cart_item' in session:
        session['cart_item']['pineapples'] = '100'
        session.modified = True
    else:
        session['cart_item'] = cart_item

    return res


@main.route('/delete-visits/')
def delete_visits():
    session.pop('cart_item', None)  # удаление данных о посещениях
    return 'Visits deleted'


@main.route('/admin/')
@login_required
def admin():
    return render_template('admin.html')