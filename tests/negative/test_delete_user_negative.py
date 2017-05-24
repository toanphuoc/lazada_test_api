from services import delete_user
import unittest

class TestDeleteUserNegative(unittest.TestCase):

    # Test delete user which user-id is none
    def test_delete_user_which_user_id_is_none(self):
        # Call the API delete user
        response = delete_user("")
        assert response == None

    # Test delete user which user-id is not exist
    def test_delete_user_which_user_id_is_not_exist(self):
        # Call the API delete user
        response = delete_user("11")
        assert response == None
