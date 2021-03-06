
from flask_graphql import GraphQLView
from .graphql.schema import schema
from .job.model_job import JobModel
from .candidate.model_candidate import CandidateModel
import json
from flask_cors import CORS


def populate_db():
    with open('./public/mock_db.json', encoding='utf-8') as f:
        data = json.load(f)
        jobs = data['jobs']
        for job in jobs:
            JobModel(**job).save()
        candidates = data['candidates']
        for candidate in candidates:
            CandidateModel(**candidate).save()


def init_app(app):
    app.add_url_rule(
        '/graphqli',
        view_func=GraphQLView.as_view('graphqli', schema=schema, graphiql=True)
    )
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view('graphql', schema=schema, batch=True)
    )

    CORS(app)
    populate_db()
