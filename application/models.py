from application import db


class Request(db.Document):
    user_id = db.IntField(unique=True)
    full_name = db.StringField(max_length=100)
    email = db.StringField(max_length=30, unique=True)
    here = db.StringField(max_length=20)
    plan = db.StringField(max_length=20)
    is_active = db.BooleanField()
