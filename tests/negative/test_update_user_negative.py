from services import update_user
import unittest

class TestUpdateUserNegative(unittest.TestCase):

    # Test update user which user-id is none
    def test_update_user_which_user_id_is_none(self):
        data = {
            "name" : "lazada"
        }

        # Call the API update data
        response = update_user("", data)

        # The http code should be 404
        assert response.status_code == 404, "The actual status code is " + str(response.status_code)


    # Test update user which user-id is not exist
    def test_update_user_which_user_id_is_not_exist(self):
        data = {
            "name" : "lazada"
        }

        # Call the API update user
        response = update_user("11", data)

        # Confirm that the API is called successfully
        assert response.status_code == 200, "The actual status code is " + str(response.status_code)

        #Confirm that data result shoule be have content such as an alert meessage
        assert response.json() != None

    # Test update user which payload is none
    def test_update_user_which_payload_is_none(self):
        data = {

        }

        # Call the API update user
        response = update_user("1", data)

        # The http code should be 404
        assert response.status_code == 404, "The actual status code is " + str(response.status_code)

    # Test update user which paypload contains invalidly key
    def test_update_user_which_paylaod_contains_invalid_key(self):
        data = {
            "invalid_key" : "lazada"
        }

        # Call the API update user
        response = update_user("1", data)

        # The http code should be 404
        assert response.status_code == 404, "The actual status code is " + str(response.status_code)

    def test_update_user_which_payload_contains_incorrect_value_type(self):
        data = {
            "name": 1
        }

        # Call the API update user
        response = update_user("1", data)

        # The http code should be 404
        assert response.status_code == 404, "The actual status code is " + str(response.status_code)
