from services import find_users_by_id, find_users_by_name, find_users_by_username, find_users_by_email

class TestFindUser():

    #Test find user by id
    def test_find_user_by_id(self):
        #Call service find user which user is exist
        response = find_users_by_id('1')

        # Confirm that the API is called successfully
        assert response.status_code == 200

        #Confirm that user is found
        assert response != None

        #Parse to json
        user_json = response.json()

        #Confirm that the data result has one item
        assert len(user_json) == 1

        #Get last user
        first_user = user_json[0]

        # Confirm that user has some keys 'id', 'name', 'username', 'email', 'address', 'phone', 'website', 'company'
        assert first_user["id"] == 1
        assert first_user["name"] == "Leanne Graham"
        assert first_user["username"] == "Bret"
        assert first_user["email"] == "Sincere@april.biz"
        assert first_user["phone"] == "1-770-736-8031 x56442"
        assert first_user["website"] == "hildegard.org"
        assert first_user["address"] != None
        assert first_user["company"] != None

    #Test find user by name
    def test_find_user_by_name(self):
        # Call service find user which user is exist
        response = find_users_by_name('Leanne Graham')

        # Confirm that the API is called successfully
        assert response.status_code == 200

        # Confirm that user is found
        assert response != None

        # Parse to json object
        user_json = response.json()

        # Confirm that the data result has one item
        assert len(user_json) == 1

        # Get last user
        first_user = user_json[0]

        # Confirm values of user such as 'id', 'name', 'username', 'email', 'address', 'phone', 'website', 'company'
        assert first_user["name"] == "Leanne Graham"
        assert first_user["username"] == "Bret"
        assert first_user["email"] == "Sincere@april.biz"
        assert first_user["phone"] == "1-770-736-8031 x56442"
        assert first_user["website"] == "hildegard.org"
        assert first_user["address"] != None
        assert first_user["company"] != None

    #Test find user by username
    def test_find_user_by_username(self):
        # Call service find user which user is exist
        response = find_users_by_username("Bret")

        # Confirm that the API is called successfully
        assert response.status_code == 200

        # Confirm that user is found
        assert response != None

        # Parse to json
        user_json = response.json()

        # Confirm that the data result just has one item
        assert len(user_json) == 1

        # Get last user
        first_user = user_json[0]
        assert first_user["name"] == "Leanne Graham"
        assert first_user["username"] == "Bret"
        assert first_user["email"] == "Sincere@april.biz"
        assert first_user["phone"] == "1-770-736-8031 x56442"
        assert first_user["website"] == "hildegard.org"
        assert first_user["address"] != None
        assert first_user["company"] != None

    #Test find user by email
    def test_find_user_by_email(self):
        # Call service find user which user is exist
        response = find_users_by_email("Sincere@april.biz")

        # Confirm that the API is called successfully
        assert response.status_code == 200

        # Confirm that user is found
        assert response != None

        # Parse to json
        user_json = response.json()

        # Confirm that the data result just has one item
        assert len(user_json) == 1

        # Get last user
        first_user = user_json[0]
        assert first_user["name"] == "Leanne Graham"
        assert first_user["username"] == "Bret"
        assert first_user["email"] == "Sincere@april.biz"
        assert first_user["phone"] == "1-770-736-8031 x56442"
        assert first_user["website"] == "hildegard.org"
        assert first_user["address"] != None
        assert first_user["company"] != None
