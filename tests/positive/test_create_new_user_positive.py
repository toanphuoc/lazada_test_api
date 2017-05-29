from services import create_user

class TestCreateUser():

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

        #Verify that the http code should be 201
        assert response.status_code == 201

        #Parse to json
        json_response = response.json()

        #Confirm that user is created via all information are correct
        assert json_response["id"] == 11, "The actual new user id is " + json_response["id"]
        assert json_response["name"] == data["name"], "The actual new user name is " + json_response["name"]
        assert json_response["username"] == data["username"], "The actual new username is " + json_response["username"]
        assert json_response["email"] == data["email"], "The actual new email is " + json_response["email"]
        assert json_response["phone"] ==data["phone"], "The actual new phone is " + json_response["phone"]
        assert json_response["website"] == data["website"], "The actual new website is " + json_response["website"]