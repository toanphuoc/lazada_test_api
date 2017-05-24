from services import update_user

class TestUpdateUser():

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
        assert json_response["id"] == 1
        assert json_response["name"] == data["name"]
        assert json_response["username"] == data["username"]
        assert json_response["email"] == data["email"]
        assert json_response["phone"] == data["phone"]
        assert json_response["website"] == data["website"]

