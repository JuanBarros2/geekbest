from mongoengine import connect
from ..api.job.model_job import JobModel


def init_app():
    connect('bestgeek',
            host='mongomock://localhost', alias='default')
