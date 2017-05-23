import unittest

from services import find_users_by_id, find_users_by_name, find_users_by_email

class TestFindUser(unittest.TestCase):

    def test_find_user_by_id(self):
        #Call service find user which user is exist
        response = find_users_by_id('1')

        # Confirm that the API is called successfully
        self.assertEquals(response.status_code, 200)

        #Confirm that user is found
        self.assertIsNotNone(response)

        #Parse to json
        user_json = response.json()

        #Confirm that the data result has one item
        self.assertEquals(len(user_json), 1)

        #Get last user
        first_user = user_json[0]

        # Confirm that user has some keys 'id', 'name', 'username', 'email', 'address', 'phone', 'website', 'company'
        self.assertEquals(first_user["id"], 1)
        self.assertEquals(first_user["name"], "Leanne Graham")
        self.assertEquals(first_user["username"], "Bret")
        self.assertEquals(first_user["email"], "Sincere@april.biz")
        self.assertEquals(first_user["phone"], "1-770-736-8031 x56442")
        self.assertEquals(first_user["website"], "hildegard.org")
        self.assertIsNotNone(first_user["address"])
        self.assertIsNotNone(first_user["company"])

    def test_find_user_by_name(self):
        # Call service find user which user is exist
        response = find_users_by_name('Leanne Graham')

        # Confirm that the API is called successfully
        self.assertEquals(response.status_code, 200)

        # Confirm that user is found
        self.assertIsNotNone(response)

        # Parse to json
        user_json = response.json()

        # Get last user
        first_user = user_json[0]

        # Confirm that user has some keys 'id', 'name', 'username', 'email', 'address', 'phone', 'website', 'company'
        self.assertEquals(first_user["name"], "Leanne Graham")
        self.assertEquals(first_user["username"], "Bret")
        self.assertEquals(first_user["email"], "Sincere@april.biz")
        self.assertEquals(first_user["phone"], "1-770-736-8031 x56442")
        self.assertEquals(first_user["website"], "hildegard.org")
        self.assertIsNotNone(first_user["address"])
        self.assertIsNotNone(first_user["company"])
