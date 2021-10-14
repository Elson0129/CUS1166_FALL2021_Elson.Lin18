import re
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, flash, redirect, url_for, render_template, request, session
from faunadb import query as q
from faunadb.client import FaunaClient
from faunadb.objects import Ref
from faunadb.errors import BadRequest, NotFound
from dotenv import load_dotenv
import os, secrets

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY']=os.getenv('SECRET_KEY')
client = FaunaClient(secret=os.getenv('FAUNA_SECRET_KEY'))

@app.route('/')
def index():
    if session.get('user_id'):
        flash('You are already logged in! ', 'warning')
        return redirect(url_for('dashboard'))

    return render_template('index.html')

@app.route('/sign_in', methods=['POST','GET'])
def sign_in():
    if session.get('user_id'):
        flash('You are already logged in!', 'warning')
        return redirect(url_for('dashboard'))


    if request.method =='POST':
        email = request.form['email']
        password = request.form['password']

        try:
            user = client.query(
                    q.get(q.match(q.index('user_by_email'), email)))

        except NotFound:
            flash('Invalid email or password', category='warning')

        else:
            if check_password_hash(user['data']['password'], password):
                session['user_id'] = user['ref'].id()
                flash('Signed in successfully', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid email or password', 'warning')

    return render_template('sign_in.html')

@app.route('/sign_up', methods=['POST','GET'])
def sign_up():
    if session.get('user_id'):
        flash('You are already logged in!', 'warning')
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        email_regex = '^[a-z0-9]+[._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if not re.search(email_regex, email) or not 6 < len(password) < 20:
            flash('Invalid email or password!, password needs to be between 6 and 20 characters', 'warning')
            return render_template('sign_up.html')

        if password != request.form['confirm_password']:
            flash('Passwords must match!', 'warning')
            return render_template('sign_up.html')

        password = generate_password_hash(password)
        user = {'name': name, 'email': email, 'password': password}

        try:

            new_user = client.query(q.create(
				q.collection('User'),
				{'data': user}
			))

        except BadRequest:
            flash('Email already exists')

        else:
            session['user_id'] = new_user['ref'].id()
            flash('Account created successfully!', 'success')
            return redirect(url_for('dashboard'))

    return render_template('sign_up.html')

@app.route('/dashboard')
def dashboard():
	if not session.get('user_id'):
			flash('You need to be logged in to view this page!', 'warning')
			return redirect(url_for('signin'))
	user = client.query(
		q.get(q.ref(q.collection("User"), session['user_id']))
	)['data']
	return render_template('dashboard.html', current_user=user)

@app.route('/sign_out')
def sign_out():
    if not session.get('user_id'):
        flash('You need to be logged in first!', 'warning')
    else:
        session.pop('user_id', None)
        flash('Signed out sucessfully', 'success')
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()
