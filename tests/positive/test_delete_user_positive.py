from services import delete_user

class TestDeleteUser():

    def test_delete_user(self):

        #Call API delete user
        response = delete_user('1')

        #Confirm that the api is called successully
        assert response.status_code == 200

        #parse response to json
        json_data = response.json()

        #Confirm data is returned
        assert json_data == {}
