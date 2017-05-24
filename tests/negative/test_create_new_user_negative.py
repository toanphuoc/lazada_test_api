from services import create_user

class TestCreateUserNegative():

    # Test create new user which payload is none
    def test_create_user_with_payload_is_none(self):
        data = {

        }

        #Call the API create user
        response = create_user(data)
        assert response == None

    # Test create new user which payload has invalid keys
    def test_create_user_which_payload_has_invalid_keys(self):
        data = {
            "key_invalid": 1,
        }

        # Call the API create user
        response = create_user(data)

        assert response == None

    # Test create new user which payload has duplicate keys
    def test_create_user_which_payload_has_duplicate_keys(self):
        data = {
            "name" : "lazada_one",
            "name" : "lazada_two"
        }

        # Call the API create user
        response = create_user(data)

        assert response == None