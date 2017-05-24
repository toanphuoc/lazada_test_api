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
        assert response == None

    # Test update user which user-id is not exist
    def test_update_user_which_user_id_is_not_exist(self):
        data = {
            "name" : "lazada"
        }

        # Call the API update user
        response = update_user("11", data)
        assert response == None

    # Test update user which payload is none
    def test_update_user_which_payload_is_none(self):
        data = {

        }

        # Call the API update user
        response = update_user("1", data)

        assert response == None

    # Test update user which paypload contains invalidly key
    def test_update_user_which_paylaod_contains_invalid_key(self):
        data = {
            "invalid_key" : "lazada"
        }

        # Call the API update user
        response = update_user("1", data)
        assert response == None

    def test_update_user_which_payload_contains_incorrect_value_type(self):
        data = {
            "name": 1
        }

        # Call the API update user
        response = update_user("1", data)
        assert response == None
