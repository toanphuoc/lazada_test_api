from services import delete_user

class TestDeleteUserNegative():

    # Test delete user which user-id is none
    def test_delete_user_which_user_id_is_none(self):
        # Call the API delete user
        response = delete_user("")

        # The http code should be 404
        assert response.status_code == 404

    # Test delete user which user-id is not exist
    def test_delete_user_which_user_id_is_not_exist(self):
        # Call the API delete user
        response = delete_user("11")

        # Confirm that the API is called successfully
        assert response.status_code == 200, "The actual status code is " + str(response.status_code)

        # Confirm that the API returns an alert message
        assert response.json() != None, "There are no any alert message is returned."
