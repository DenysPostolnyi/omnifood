import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
                 b'\xd5xB\x92\xf5\xa7\x1dP\xa2\x8f\xb8oi\xb4\x00\x1c'

    with open('db_host.txt') as f:
        host = f.read().strip()

    MONGODB_SETTINGS = {'db': 'Cluster0',
                        'host': host
                        }
