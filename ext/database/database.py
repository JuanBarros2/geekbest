from mongoengine import connect

# You can connect to a real mongo server instance by your own.
connect('graphene-mongo-example', host='mongomock://localhost', alias='default')


def init_db():
    pass
