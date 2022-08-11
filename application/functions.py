from flask import session

from application.models import Request


def make_request(form):
    user_id = Request.objects.count() + 1
    email = form.get('email')
    name = form.get('full_name')
    here = form.get('here')
    email_from_db = Request.objects.filter(email=email)
    if email_from_db:
        name_from_db = Request.objects.filter(full_name=name, email=email)
        if name_from_db:
            session['is_active'] = Request.objects(email=email).first()['is_active']
            # session['is_active'] = Request.objects(email=email_from_db).first()['is_active']
            return 'User founded'
        return 'Email is already existed'
    req = Request(user_id=user_id, full_name=name, email=email, here=here, is_active=True)
    req.save()
    session['is_active'] = req['is_active']
    return 'User saved'
