from services import update_user
import unittest

class TestUpdateUser(unittest.TestCase):

    def test_update_user(self):

        #Preparation data need to update
        data = {
            "name": "test",
            "username": "lazada",
            "email": "test@lazada.com",
            "phone": "0321321321",
            "website": "abc.com.vn"
        }

        #Call API update user
        response = update_user('1', data)

        # Parse response to json object
        json_response = response.json()

        # Confirm that user is updated which all informations are correct
        self.assertEquals(json_response["id"], 1)
        self.assertEquals(json_response["name"], data["name"])
        self.assertEquals(json_response["username"], data["username"])
        self.assertEquals(json_response["email"], data["email"])
        self.assertEquals(json_response["phone"], data["phone"])
        self.assertEquals(json_response["website"], data["website"])

