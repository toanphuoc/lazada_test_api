import unittest
from services import create_user

class TestCreateUser(unittest.TestCase):

    def test_create_user(self):

        #Post data with keys 'name', 'username', 'email', 'phone', 'website'
        data = {
            "name": "lazada",
            "username": "lazada",
            "email": "contact@lazada.com",
            "phone": "021321321",
            "website": "abc.com.vn"
        }

        #Call API create new user
        response = create_user(data);

        #Parse to json
        json_response = response.json()

        #Confirm that user is created via all information are correct
        self.assertEquals(json_response["id"], 11)
        self.assertEquals(json_response["name"], data["name"])
        self.assertEquals(json_response["username"], data["username"])
        self.assertEquals(json_response["email"], data["email"])
        self.assertEquals(json_response["phone"], data["phone"])
        self.assertEquals(json_response["website"], data["website"])