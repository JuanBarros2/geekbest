import pytest
from ext.api.graphql.schema import schema
from ext.api.job.model_job import JobModel


@pytest.fixture
def jobs():
    jobs = [{
        "id": 33922,
        "city": "São Paulo - SP",
        "technologies": ["Vue", "Node"],
        "experience": "2-4 years"
    },
        {
        "id": 33916,
        "city": "Rio de Janeiro - RJ",
        "technologies": ["Java", "C"],
        "experience": "0-2 years"
    }]
    for job in jobs:
        JobModel(**job).save()
        del job['id']
    return jobs


def test_should_job_list_be_empty(graphql):
    executed = graphql.execute('''{ job { city } }''')
    assert executed == {
        'data': {
            'job': []
        }
    }


def test_should_job_list_be_returned(graphql, jobs):
    executed = graphql.execute(
        '''{ job { city, experience, technologies } }''')
    assert executed == {
        'data': {
            'job': jobs
        }
    }


def test_should_filter_jobs_to_technologies(graphql, jobs):
    executed = graphql.execute(
        '''{ job(technologies:["Vue"]) {
             city, experience, technologies }
             }''')
    assert executed == {
        'data': {
            'job': [{
                    "city": "São Paulo - SP",
                    "technologies": ["Vue", "Node"],
                    "experience": "2-4 years"}]
        }
    }


def test_should_filter_jobs_to_cities(graphql, jobs):
    executed = graphql.execute(
        '''{ job(city:["São Paulo - SP"]) {
             city, experience, technologies }
             }''')
    assert executed == {
        'data': {
            'job': [{
                    "city": "São Paulo - SP",
                    "technologies": ["Vue", "Node"],
                    "experience": "2-4 years"}]
        }
    }

def test_should_filter_jobs_that_dont_match(graphql, jobs):
    executed = graphql.execute(
        '''{ job(city:["São Paulo - SP"], technologies:["C"]) {
             city, experience, technologies }
             }''')
    assert executed == {
        'data': {
            'job': []
        }
    }
