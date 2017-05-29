from services import find_users_by_id, find_users_by_name, find_users_by_username, find_users_by_email

class TestFindUser():

    #Test find user by id
    def test_find_user_by_id(self):
        #Call service find user which user is exist
        response = find_users_by_id('1')

        # Confirm that the API is called successfully
        assert response.status_code == 200, "The actual status code is " + str(response.status_code)

        #Parse to json
        user_json = response.json()

        #Confirm that the data result has one item
        assert len(user_json) == 1, "The result of finding user by id shout be have one data. The number of actual data are " + str(len(user_json))

        #Get last user
        first_user = user_json[0]

        # Confirm that user has some keys 'id', 'name', 'username', 'email', 'address', 'phone', 'website', 'company'
        assert first_user["id"] == 1, "The actual user id is found which is " + str(first_user["id"])
        assert first_user["name"] != None
        assert first_user["username"] != None
        assert first_user["email"] != None
        assert first_user["phone"] != None
        assert first_user["website"] != None
        assert first_user["address"] != None
        assert first_user["company"] != None

    #Test find user by name
    def test_find_user_by_name(self):
        # Call service find user which user is exist
        response = find_users_by_name('Leanne Graham')

        # Confirm that the API is called successfully
        assert response.status_code == 200, "The actual status code is " + str(response.status_code)

        # Parse to json object
        user_json = response.json()

        # Get last user
        first_user = user_json[0]

        # Confirm values of user such as 'id', 'name', 'username', 'email', 'address', 'phone', 'website', 'company'
        assert first_user["name"] == "Leanne Graham", "The actual name is found which is " + first_user["name"]
        assert first_user["username"] != None
        assert first_user["email"] != None
        assert first_user["phone"] != None
        assert first_user["website"] != None
        assert first_user["address"] != None
        assert first_user["company"] != None

    #Test find user by username
    def test_find_user_by_username(self):
        # Call service find user which user is exist
        response = find_users_by_username("Bret")

        # Confirm that the API is called successfully
        assert response.status_code == 200, "The actual status code is " + str(response.status_code)

        # Parse to json
        user_json = response.json()

        # Confirm that the data result just has one item
        assert len(user_json) == 1, "The result of finding user by id shout be have one data. The number of actual data are " + str(len(user_json))

        # Get last user
        first_user = user_json[0]
        assert first_user["name"] != None
        assert first_user["username"] != None
        assert first_user["email"] == "Sincere@april.biz", "The actual email is found which is " + first_user["email"]
        assert first_user["phone"] != None
        assert first_user["website"] != None
        assert first_user["address"] != None
        assert first_user["company"] != None

    #Test find user by email
    def test_find_user_by_email(self):
        # Call service find user which user is exist
        response = find_users_by_email("Sincere@april.biz")

        # Confirm that the API is called successfully
        assert response.status_code == 200, "The actual status code is " + str(response.status_code)

        # Parse to json
        user_json = response.json()

        # Confirm that the data result just has one item
        assert len(user_json) == 1, "The result of finding user by id shout be have one data. The number of actual data are " + str(len(user_json))

        # Get last user
        first_user = user_json[0]
        assert first_user["name"]!= None
        assert first_user["username"] != None
        assert first_user["email"] == "Sincere@april.biz", "The actual email is found which is " + first_user["email"]
        assert first_user["phone"] != None
        assert first_user["website"] != None
        assert first_user["address"] != None
        assert first_user["company"] != None
