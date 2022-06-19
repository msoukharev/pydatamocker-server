import json
from pydatamocker_server import app


req = {
    "Users": {
        "size": 1000,
        "fields": [
            {
                "name": "FirstName",
                "value": {
                    "dataset": {
                        "name": "first_name"
                    }
                }
            },
            {
                "name": "LastName",
                "value": {
                    "dataset": {
                        "name": "last_name"
                    }
                }
            }
        ]
    }
}


def test_post_schema():
    response = app.test_client().post('/schema', data=json.dumps(req), content_type='application/json')
    assert response.status_code == 200
    assert response.data
