from main2 import app, index, user_profile

if __name__ == "__main__":
    print(app.url_map)






from app import db
from . import main
from flask import (render_template, request, redirect, url_for, flash,   make_response, session, current_app)
from flask_login import login_required, login_user, current_user, logout_user
from app.models import User, Feedback
from .forms import ContactForm, LoginForm

@main.route('/')def index():    return render_template('index.html', name='Jerry')@main.route('/user//')def user_profile(user_id):    return "Profile page of user #{}".format(user_id)@main.route('/books//')def books(genre):    return "All Books in {} category".format(genre)@main.route('/login/', methods=['post', 'get'])def login():    if current_user.is_authenticated:return redirect(url_for('.admin'))    form = LoginForm()    if form.validate_on_submit():user = db.session.query(User).filter(User.username == form.username.data).first()if user and user.check_password(form.password.data):    login_user(user, remember=form.remember.data)    return redirect(url_for('.admin'))flash("Invalid username/password", 'error')return redirect(url_for('.login'))    return render_template('login.html', form=form)@main.route('/logout/')@login_requireddef logout():    logout_user()    flash("You have been logged out.")    return redirect(url_for('.login'))@main.route('/contact/', methods=['get', 'post'])def contact():    form = ContactForm()    if form.validate_on_submit():name = form.name.dataemail = form.email.datamessage = form.message.data# логика БД здесьfeedback = Feedback(name=name, email=email, message=message)db.session.add(feedback)db.session.commit()send_mail("New Feedback", current_app.config['MAIL_DEFAULT_SENDER'], 'mail/feedback.html',  name=name, email=email)flash("Message Received", "success")return redirect(url_for('.contact'))    return render_template('contact.html', form=form)@main.route('/cookie/')def cookie():    if not request.cookies.get('foo'):res = make_response("Setting a cookie")res.set_cookie('foo', 'bar', max_age=60*60*24*365*2)    else:res = make_response("Value of cookie foo is {}".format(request.cookies.get('foo')))    return res@main.route('/delete-cookie/')def delete_cookie():    res = make_response("Cookie Removed")    res.set_cookie('foo', 'bar', max_age=0)    return res@main.route('/article', methods=['POST', 'GET'])def article():    if request.method == 'POST':res = make_response("")res.set_cookie("font", request.form.get('font'), 60*60*24*15)res.headers['location'] = url_for('.article')return res, 302    return render_template('article.html')@main.route('/visits-counter/')def visits():    if 'visits' in session:session['visits'] = session.get('visits') + 1    else:session['visits'] = 1    return "Total visits: {}".format(session.get('visits'))@main.route('/delete-visits/')def delete_visits():    session.pop('visits', None)  # удаление посещений    return 'Visits deleted'@main.route('/session/')def updating_session():    res = str(session.items())        cart_item = {'pineapples': '10', 'apples': '20', 'mangoes': '30'}    if 'cart_item' in session:session['cart_item']['pineapples'] = '100'session.modified = True    else:session['cart_item'] = cart_item    return res@main.route('/admin/')@login_requireddef admin():    return render_template('admin.html')


import os
from app import  db,  create_app
from app.models import User, Post, Tag, Category, Employee, Feedback
from flask_script import Manager, Shell
from flask_migrate import MigrateCommand
app = create_app(os.getenv('FLASK_ENV') or 'config.DevelopementConfig')
# manager = Manager(app)
# def make_shell_context():    
#     return dict(app=app, db=db, User=User, Post=Post, Tag=Tag, Category=Category,Employee=Employee, Feedback=Feedback)
# manager.add_command('shell', Shell(make_context=make_shell_context))
# manager.add_command('db', MigrateCommand)
if __name__ == '__main__':    
    manager.run()



#...# создать экземпляр приложения
# app = Flask(__name__)
# app.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopementConfig')
# # инициализирует расширения
# db = SQLAlchemy(app)
# mail = Mail(app)
# migrate = Migrate(app,  db)
# login_manager = LoginManager(app)
# login_manager.login_view = 'main.login'
# # регистрация blueprints
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)
#from .admin import main as admin_blueprint
#app.register_blueprint(admin_blueprint)

from app import app, db
from . import main
from flask import Flask, request, render_template, redirect, url_for, flash, make_response, session
from flask_login import login_required, login_user, current_user, logout_user
from app.models import User, Post, Category, Feedback, db
from .forms import ContactForm, LoginForm

@main.route('/')
def index():    
    return render_template('index.html', name='Jerry')

@main.route('/user//')
def user_profile(user_id):    
    return "Profile page of user #{}".format(user_id)

@main.route('/books//')
def books(genre):    
    return "All Books in {} category".format(genre)

@main.route('/login/', methods=['post', 'get'])
def login():    
    if current_user.is_authenticated:
        return redirect(url_for('.admin'))    
    form = LoginForm()    
    if form.validate_on_submit():
        user = db.session.query(User).filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):    
            login_user(user, remember=form.remember.data)    
            return redirect(url_for('.admin'))
        flash("Invalid username/password", 'error')
        return redirect(url_for('.login'))    
    return render_template('login.html',  form=form)

@main.route('/logout/')@login_requireddef logout():    logout_user()    flash("You have been logged out.")    return redirect(url_for('.login'))@main.route('/contact/', methods=['get', 'post'])def contact():    form = ContactForm()    if form.validate_on_submit():name = form.name.dataemail = form.email.datamessage = form.message.dataprint(name)print(email)print(message)# здесь логика БД feedback = Feedback(name=name, email=email, message=message)db.session.add(feedback)db.session.commit()send_mail("New Feedback", app.config['MAIL_DEFAULT_SENDER'], 'mail/feedback.html',  name=name, email=email)print("\nData received. Now redirecting ...")flash("Message Received", "success")return redirect(url_for('.contact'))    return render_template('contact.html',  form=form)@main.route('/cookie/')def cookie():    if not request.cookies.get('foo'):res = make_response("Setting a cookie")res.set_cookie('foo', 'bar', max_age=60*60*24*365*2)    else:res = make_response("Value of cookie foo is {}".format(request.cookies.get('foo')))    return res@main.route('/delete-cookie/')def delete_cookie():    res = make_response("Cookie Removed")    res.set_cookie('foo', 'bar', max_age=0)    return res@main.route('/article/', methods=['POST', 'GET'])def article():    if request.method == 'POST':print(request.form)res = make_response("")res.set_cookie("font", request.form.get('font'), 60*60*24*15)res.headers['location'] = url_for('.article')return res, 302    return render_template('article.html')@main.route('/visits-counter/')def visits():    if 'visits' in session:session['visits'] = session.get('visits') + 1  # чтение и обновление данных сессии    else:session['visits'] = 1  # настройка данных сессии    return "Total visits: {}".format(session.get('visits'))@main.route('/delete-visits/')def delete_visits():    session.pop('visits', None)  # удаление посещений    return 'Visits deleted'@main.route('/session/')def updating_session():    res = str(session.items())        cart_item = {'pineapples': '10', 'apples': '20', 'mangoes': '30'}    if 'cart_item' in session:session['cart_item']['pineapples'] = '100'session.modified = True    else:session['cart_item'] = cart_item    return res@main.route('/admin/')@login_requireddef admin():    return render_template('admin.html')