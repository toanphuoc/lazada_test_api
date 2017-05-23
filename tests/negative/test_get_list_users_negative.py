import unittest
from services import get_user_by_id

class TestGetUserNegative(unittest.TestCase):

    #Test get user by id which user is not exist
    def test_get_user_by_id_with_user_is_not_exist(self):

        response = get_user_by_id('11')

        self.assertIsNone(response)
