from nose.tools import assert_is_not_none, assert_list_equal, assert_equal, assert_not_equals, assert_is_none
from unittest.mock import Mock, patch
from services import get_users, find_users
import json

class TestUsers(object):

    @classmethod
    def setup_class(cls):
        cls.mock_get_patcher = patch('services.requests.get')
        cls.mock_get = cls.mock_get_patcher.start()

    @classmethod
    def teardown_class(cls):
        cls.mock_get_patcher.stop()

    def test_get_list_users_with_response_is_ok(self):

        users = [{
            "id": 1,
            "name": "Leanne Graham",
            "username": "Bret",
            "email": "Sincere@april.biz",
            "address": {
                "street": "Kulas Light",
                "suite": "Apt. 556",
                "city": "Gwenborough",
                "zipcode": "92998-3874",
                "geo": {
                    "lat": "-37.3159",
                    "lng": "81.1496"
                }
            },
            "phone": "1-770-736-8031 x56442",
            "website": "hildegard.org",
            "company": {
                "name": "Romaguera-Crona",
                "catchPhrase": "Multi-layered client-server neural-net",
                "bs": "harness real-time e-markets"
            }
        }]

        # Configure the mock to return a response with an OK  status code
        self.mock_get.return_value = Mock(ok=True)
        self.mock_get.return_value.json.return_value = users

        # Call the service get list users
        users_response = get_users()
        # If the request is sent successfully, then I expect a response to be returned
        assert_list_equal(users_response, users)

    def test_getting_users_with_response_is_none(self):
        # Configure the mock to not return a response with an OK status code.
        self.mock_get.return_value.ok = False

        # Call the service, which will send a request to the server.
        users_response = get_users()

        assert_is_none(users_response)