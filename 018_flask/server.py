from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
import hashlib
from datetime import timedelta, datetime


app = Flask(__name__)

app.secret_key = '''pTq%J£{*<$G>lr*12b77wB-{(',;5wBI'''
app.permanent_session_lifetime = timedelta(hours=5)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost/flask_python_eng'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    _id = db.Column('id', db.Integer, primary_key=True)
    login = db.Column('login', db.String(20))
    password = db.Column('password', db.String(32))
    email = db.Column('email', db.String(50))

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

class Post(db.Model):
    _id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String(50))
    content = db.Column('content', db.String(1000))
    date_added = db.Column('date_added', db.DateTime())
    owner = db.Column('owner', db.String(20))

    def __init__(self, title, content, owner):
        self.title = title
        self.content = content
        self.date_added = datetime.now()
        self.owner = owner

@app.route('/')
def home():
    posts = Post.query.order_by(desc('date_added')).all()
    return render_template('home.html', posts=posts)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user_login = request.form['user-name']
        user_password = hashlib.md5(request.form['user-pass'].encode()).hexdigest()
        user_in_db = User.query.filter_by(login=user_login).first()
        if user_in_db:
            # CHECK FOR USER PASSWORD
            if user_password == user_in_db.password:
                session['login'] = user_login
                session['email'] = user_in_db.email
                flash('Logged in successfully', 'success')
                return redirect(url_for('user'))
            else:
                flash('Password is incorrect', 'danger')
                return redirect(url_for('login'))
        else:
            new_user = User(user_login, user_password, '')
            db.session.add(new_user)
            db.session.commit()
            session['login'] = user_login
            session['email'] = ''
            flash(f'User "{user_login}" was created', 'success')
            return redirect(url_for('user'))
    else:
        if 'login' in session:
            flash('Already logged in', 'info')
            return redirect(url_for('user'))
        return render_template('login.html')

@app.route('/logout/')
def logout():
    session.pop('login', None)
    session.pop('email', None)
    flash('Logged out successfully', 'success')
    return redirect(url_for('login'))

@app.route('/user/', methods=['GET', 'POST'])
def user():
    if 'login' in session:
        login = session['login']
        if request.method == 'POST':
            user_email = request.form['user-email']
            user_in_db = User.query.filter_by(login=login).first()
            user_in_db.email = user_email
            db.session.commit()
            session['email'] = user_email
            flash('Email was saved successfully', 'success')
        return render_template('user.html', user_email=session['email'])
    else:
        flash('You are not logged in', 'danger')
        return redirect(url_for('login'))

@app.route('/post/', methods=['GET', 'POST'])
def post():
    if 'login' in session:
        if request.method == 'POST':
            title = request.form['post-title']
            content = request.form['post-content']
            owner = session['login']
            new_post = Post(title, content, owner)
            db.session.add(new_post)
            db.session.commit()
            flash('Post saved', 'success')
            return redirect(url_for('post'))
        else:
            return render_template('post.html')
    else:
        flash('You are not logged in', 'danger')
        return redirect(url_for('login'))


@app.route('/del_post/<post_id>')
def del_post(post_id):
    the_post = Post.query.filter_by(_id=post_id).first()
    if the_post.owner == session['login']:
        Post.query.filter_by(_id=post_id).delete()
        db.session.commit()
        flash('Post deleted', 'success')
    else:
        flash('You can not delete other users posts', 'warning')
    return redirect(url_for('home'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
