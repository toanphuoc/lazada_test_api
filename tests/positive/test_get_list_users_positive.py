from services import get_list_of_users, get_user_by_id

class TestGetUsers():

    #Test get list of user
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
        response = get_list_of_users()

        #Confirm that the API is called successfully
        assert response.status_code == 200

        #Parse response to json object
        users_json = response.json()

        # If the request is sent successfully, then I expect a response to be returned
        assert len(users_json) == 10

        #Get last user
        last_user = users_json.pop()

        # Verification that "name", "username, "email" is not None
        assert last_user["name"] != None
        assert last_user["username"] != None
        assert last_user["email"] != None
        assert last_user["address"] != None
        assert last_user["phone"] != None
        assert last_user["company"] != None

    #Test get user by id
    def test_get_user_id(self):
        response = get_user_by_id('1')

        # Confirm that the API is called successfully
        assert response.status_code == 200

        # Parse response to json object
        user_json = response.json()

        # Verification that "name", "username, "email" is not None
        assert user_json["id"] == 1
        assert user_json["name"] != None
        assert user_json["username"] != None
        assert user_json["email"] != None
        assert user_json["address"] != None
        assert user_json["phone"] != None
        assert user_json["company"] != None
        assert user_json["website"] != None

