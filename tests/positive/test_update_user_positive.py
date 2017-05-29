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

        # Confirm that the API is called successfully
        assert response.status_code == 200, "The actual status code is " + str(response.status_code)

        # Parse response to json object
        json_response = response.json()

        # Confirm that user is updated which all informations are correct
        assert json_response["id"] == 1, "The actual user-id is " + str(json_response["id"])
        assert json_response["name"] == data["name"], "The actual name of user is " + json_response["name"]
        assert json_response["username"] == data["username"], "The actual username is " + json_response["username"]
        assert json_response["email"] == data["email"], "The actual email is " + json_response["email"]
        assert json_response["phone"] == data["phone"], "The actual phone is " + json_response["phone"]
        assert json_response["website"] == data["website"], "The actual website is " + json_response["website"]

