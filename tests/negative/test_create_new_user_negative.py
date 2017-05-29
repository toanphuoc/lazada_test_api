from services import create_user

class TestCreateUserNegative():

    # Test create new user which payload is none
    def test_create_user_with_payload_is_none(self):
        data = {

        }

        #Call the API create user
        response = create_user(data)

        result_json = response.json()

        #Verify that the response http code is 404
        assert response.status_code == 404, "Actual http code is " + str(response.status_code)

        assert result_json["id"] == None, "The actual user-id is created which is " + str(result_json["id"])


    # Test create new user which payload has invalid keys
    def test_create_user_which_payload_has_invalid_keys(self):
        data = {
            "key_invalid": 1,
        }

        # Call the API create user
        response = create_user(data)

        result_json = response.json()

        # Verify that the response http code is 404
        assert response.status_code == 404, "Actual http code is " + str(response.status_code)

        assert result_json["id"] == None, "The actual user-id is created which is " + str(result_json["id"])
        assert result_json["key_invalid"] == None, "The actual invalid key is created which is " + result_json["key_invalid"]

    # Test create new user which payload has duplicate keys
    def test_create_user_which_payload_has_duplicate_keys(self):
        data = {
            "name" : "lazada_one",
            "name" : "lazada_two"
        }

        # Call the API create user
        response = create_user(data)

        result_json = response.json()

        # Verify that the response http code is 404
        assert response.status_code == 404, "Actual http code is " + str(response.status_code)

        assert result_json["id"] == None, "The actual user-id is created which is " + str(result_json["id"])
        assert result_json["name"] == None, "The actual invalid key is created which is " + result_json["key_invalid"]