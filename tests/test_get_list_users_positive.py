from services import get_users
import unittest

class TestGetUsers(unittest.TestCase):

    def test_get_list_users_with_response_is_ok(self):

        user = {
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
        }

        # Call the service get list users
        response = get_users()

        #Confirm that the API is called successfully
        self.assertEquals(response.status_code, 200)
        users_json = response.json()

        # If the request is sent successfully, then I expect a response to be returned
        self.assertEquals(len(users_json), 10)

        #Get last user
        last_user = users_json.pop()

        # Verification that "name", "username, "email" is not None
        self.assertIsNotNone(last_user["name"])
        self.assertIsNotNone(last_user["username"])
        self.assertIsNotNone(last_user["email"])
        self.assertIsNotNone(last_user["address"])
        self.assertIsNotNone(last_user["phone"])
        self.assertIsNotNone(last_user["company"])