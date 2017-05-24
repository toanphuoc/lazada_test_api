from services import find_users_by_id, find_users_by_name, find_users_by_username, find_users_by_email

class TestFindUserNegative():

    # Test user by id which user-id is none
    def test_find_user_by_id_which_id_is_none(self):
        # Call the api find user
        response = find_users_by_id('')

        # Compare length of array json which is returned
        assert len(response.json()) == 0

    #Find user by id which id is not exist
    def test_find_user_by_id_which_id_is_not_exist(self):

        #Call the api find user
        response = find_users_by_id('11')

        #Compare length of array json which is returned
        assert len(response.json()) == 0

    #Find user by name which name is none
    def test_find_user_by_name_which_name_is_none(self):
        # Call the api find user
        response = find_users_by_name("")

        # Compare length of array json which is returned
        assert len(response.json()) == 0

    #Find user by name which name is not exist
    def test_find_user_by_name_which_name_is_not_exist(self):
        #Call the api find user
        response = find_users_by_name("testabc")

        # Compare length of array json which is returned
        assert len(response.json()) == 0

    #Find user by username which username is none
    def test_find_user_by_username_which_username_is_none(self):
        # Call the api find user
        response = find_users_by_username("")

        # Compare length of array json which is returned
        assert len(response.json()) == 0

    # Find user by username which username is not exist
    def test_find_user_by_username_which_username_is_not_exist(self):
        # Call the api find user
        response = find_users_by_username("testabc")

        # Compare length of array json which is returned
        assert len(response.json()) == 0

    #Find user by email which email is none
    def test_find_user_by_email_which_email_is_none(self):
        # Call the API find user
        response = find_users_by_email("")

        # Compare length of array json which is returned
        assert len(response.json()) == 0


    #Find user by email which email is not exist
    def test_find_user_by_email_which_email_is_not_exist(self):
        #Call the API find user
        response = find_users_by_email("test@lazada")

        # Compare length of array json which is returned
        assert len(response.json()) == 0
