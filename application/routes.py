from flask import Flask, render_template, request
from application import app


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        print(f"Full name {request.form.get('full_name')}")
        print(f"Email {request.form.get('email')}")
        print(f"Here {request.form.get('here')}")
    return render_template('index.html')
