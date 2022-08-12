from flask import Flask, render_template, request, redirect, url_for, session, flash
from application import app, db
from application.models import Request
from application import functions


@app.route('/', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
def home():
    message = None
    if session.get('username'):
        return render_template('index.html')
    if request.method == 'POST':
        if functions.make_request(request.form) == 'User saved' or functions.make_request(request.form) == 'User founded':
            message = f"{request.form.get('full_name')}, wellcome"
            session['full_name'] = request.form.get('full_name')
            session['email'] = request.form.get('email')
        elif functions.make_request(request.form) == 'Email is already existed':
            message = 'Email is already existed'
    return render_template('index.html', text=message)


@app.route('/login', methods=['POST'])
def login():
    if session.get('username'):
        return redirect(url_for('home'))
    if request.method == 'POST':
        email = request.form.get('email')
        full_name = request.form.get('full_name').lower()
        user = Request.objects(email=email).first()
        if user and user['full_name'] == full_name:
            session['full_name'] = request.form.get('full_name')
            session['email'] = email
            session['is_active'] = user['is_active']
            return redirect(url_for("home"))
        else:
            flash('Enter is incorrect')
    return redirect(url_for("home"))


@app.route('/logout')
def logout():
    session.pop('full_name', None)
    session.pop('email', None)
    session.pop('is_active', None)
    return redirect(url_for('home'))


@app.route('/pause')
def pause():
    if session.get('email'):
        Request.objects(email=session['email']).update_one(is_active=False)
        session['is_active'] = False
        flash('Your plan paused')
    return redirect(url_for('home'))


@app.route('/start')
def start():
    if session.get('email'):
        Request.objects(email=session['email']).update_one(is_active=True)
        session['is_active'] = True
        flash('Your plan resumed')
    return redirect(url_for('home'))


@app.route('/cancel')
def cancel():
    return redirect(url_for('home'))
