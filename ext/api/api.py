
from flask_graphql import GraphQLView
from .graphql.schema import schema
from .job.model_job import JobModel
import json


def populate_db():
    with open('./public/mock_db.json') as f:
        data = json.load(f)
        jobs = data['jobs']
        for job in jobs:
            JobModel(**job).save()


def init_app(app):
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
    )
    populate_db()
