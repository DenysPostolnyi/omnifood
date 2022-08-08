from application.models import Request


def make_request(form):
    user_id = Request.objects.count() + 1
    email = form.get('email')
    name = form.get('full_name')
    here = form.get('here')
    email_from_db = Request.objects.filter(email=email)
    if email_from_db:
        name_from_db = Request.objects.filter(full_name=name)
        if name_from_db:
            return 'User founded'
        return 'Email is already existed'
    req = Request(user_id=user_id, full_name=name, email=email, here=here, is_active=True)
    req.save()
    return 'User saved'