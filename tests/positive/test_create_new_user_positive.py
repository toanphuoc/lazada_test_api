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

        #Parse to json
        json_response = response.json()

        #Confirm that user is created via all information are correct
        assert json_response["id"] == 11
        assert json_response["name"] == data["name"]
        assert json_response["username"] == data["username"]
        assert json_response["email"] == data["email"]
        assert json_response["phone"] ==data["phone"]
        assert json_response["website"] == data["website"]