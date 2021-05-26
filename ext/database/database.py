from mongoengine import connect


def init_app():
    connect('bestgeek',
            host='mongomock://localhost', alias='default')
