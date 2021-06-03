import pytest
from ext.api.graphql.schema import schema
from ext.api.candidate.model_candidate import CandidateModel


@pytest.fixture
def candidates():
    candidates = [{
        "id": 31562,
        "city": "Rio de Janeiro - RJ",
        "experience": "12+ years",
        "technologies": [
            {"name": "Java", "is_main_tech": True},
            {"name": "Spring", "is_main_tech": False}
        ]
    },
        {
        "id": 111734,
        "city": "Recife - PE",
        "experience": "4-5 years",
        "technologies": [
            {"name": "React", "is_main_tech": True},
            {"name": "AngularJS", "is_main_tech": False}
        ]
    },
        {
        "id": 104458,
        "city": "Curitiba - PR",
        "experience": "5-6 years",
        "technologies": [
            {"name": "C#", "is_main_tech": True},
            {"name": "Actionscript", "is_main_tech": False}
        ]
    }]
    for candidate in candidates:
        CandidateModel(**candidate).save()
        del candidate['id']
    return candidates


def test_should_candidate_list_be_empty(graphql):
    executed = graphql.execute('''{ candidate { city } }''')
    assert executed == {
        'data': {
            'candidate': []
        }
    }


def test_should_candidate_list_be_returned(graphql, candidates):
    executed = graphql.execute(
        '''{ candidate { id, city, experience } }''')
    returned_candidates = executed['data']['candidate']
    assert len(returned_candidates) == len(candidates)


def test_should_filter_candidate_to_experience(graphql, candidates):
    executed = graphql.execute(
        '''{ candidate(experience:["12+ years"]) {
             city, experience, technologies { name, isMainTech } }
             }''')
    assert executed['data']['candidate'] == [{
        "city": "Rio de Janeiro - RJ",
        "experience": "12+ years",
        "technologies": [
            {"name": "Java", "isMainTech": True},
            {"name": "Spring", "isMainTech": False}
        ]}]


def test_should_filter_candidate_to_cities(graphql, candidates):
    executed = graphql.execute(
        '''{ candidate(city:["Curitiba - PR"]) {
             city, experience,technologies{ name, isMainTech } }
             }''')
    assert executed == {
        'data': {
            'candidate': [{
                "city": "Curitiba - PR",
                "experience": "5-6 years",
                "technologies": [
                    {"name": "C#", "isMainTech": True},
                    {"name": "Actionscript", "isMainTech": False}
                ]}]
        }
    }


def test_should_filter_candidate_that_dont_match(graphql, candidates):
    executed = graphql.execute(
        '''{ candidate(city:["Campina Grande - PB"]) {
             city, experience }
             }''')
    assert executed == {
        'data': {
            'candidate': []
        }
    }

def test_should_list_filters(graphql, candidates):
    executed = graphql.execute(
        '''{ filters {
             city, experience, technologies }
             }''')
    filters = executed['data']['filters']
    def assert_all(atual_list, expected_list):
        diff = set(atual_list) ^ set(expected_list)
        assert not diff
    
    assert_all(filters['city'], ['Rio de Janeiro - RJ', 'Recife - PE', 'Curitiba - PR'])
    assert_all(filters['experience'],  ['12+ years', '4-5 years', '5-6 years'])
    assert_all(filters['technologies'],  ['Java', 'Spring', 'React', 'AngularJS', 'C#', 'Actionscript'])