from services import get_user_by_id

class TestGetUserNegative():

    #Test get user by id which user is not exist
    def test_get_user_by_id_with_user_is_not_exist(self):

        response = get_user_by_id('11')

        # Confirm that the API is called successfully
        assert response.status_code == 200, "The actual status code is " + str(response.status_code)

        # Compare length of array json which is returned
        assert len(response.json()) == 0, "The actual length of result is " + len(response.json())
