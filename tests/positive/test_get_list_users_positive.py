from services import get_list_of_users, get_user_by_id

class TestGetUsers():

    #Test get list of user
    def test_get_list_users_with_response_is_ok(self):

        # Call the service get list users
        response = get_list_of_users()

        #Confirm that the API is called successfully
        assert response.status_code == 200, "The actual status code is " + str(response.status_code)

        #Parse response to json object
        users_json = response.json()

        # If the request is sent successfully, then I expect a response to be returned
        assert len(users_json) == 10, "The actual length of user is " + str(len(users_json))

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
        assert response.status_code == 200, "The actual status code is " + str(response.status_code)

        # Parse response to json object
        user_json = response.json()

        # Confirm that the data result just has one item
        assert isinstance(user_json, list) == False, "The result of get user by id is a list type."

        # Verification that "name", "username, "email" is not None
        assert user_json["id"] == 1
        assert user_json["name"] != None
        assert user_json["username"] != None
        assert user_json["email"] != None
        assert user_json["address"] != None
        assert user_json["phone"] != None
        assert user_json["company"] != None
        assert user_json["website"] != None

