from flask import session

from application.models import Request


def make_request(form):
    user_id = last_id() + 1 if last_id() is not False else 0
    email = form.get('email')
    name = form.get('full_name').lower()
    here = form.get('here')
    email_from_db = Request.objects.filter(email=email)
    if email_from_db:
        name_from_db = Request.objects.filter(full_name=name, email=email)
        if name_from_db:
            session['plan'] = Request.objects(email=email).first()['plan']
            session['is_active'] = Request.objects(email=email).first()['is_active']
            return True
        return False
    req = Request(user_id=user_id, full_name=name, email=email, here=here, is_active=False, plan="")
    req.save()
    session['is_active'] = False
    session['plan'] = ""
    return True


def last_id():
    max_id = list(Request.objects.aggregate(*[
        {
            '$group': {
                '_id': '',
                'last': {
                    '$max': "$user_id"
                }
            }
        }
    ]))
    if len(max_id) == 0:
        return False
    else:
        return max_id[0]['last']
