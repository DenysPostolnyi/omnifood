from flask import Flask, render_template, request
from application import app, db
from application.models import Request


@app.route('/', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
def home():
    message = None
    if request.method == 'POST':
        message = make_request(request.form)
    return render_template('index.html', text=message)


def make_request(form):
    user_id = Request.objects.count() + 1
    email = form.get('email')
    email_from_db = Request.objects.filter(email=email)
    if email_from_db:
        return "email exist"
    name = form.get('full_name')
    plan = form.get('plan')
    here = form.get('here')

    req = Request(user_id=user_id, full_name=name, email=email, plan=plan, here=here)
    return 'success'
