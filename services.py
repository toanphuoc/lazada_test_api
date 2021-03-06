from urllib.parse import urljoin
import requests

from constants import BASE_URL

# Get list of users
def get_list_of_users():
	GET_USER_URL = urljoin(BASE_URL, 'users')
	response = requests.get(GET_USER_URL)

	if(response.ok):
		return  response
	else:
		None

# Get user by id
def get_user_by_id(user_id):
	GET_USER_URL = urljoin(BASE_URL, 'users/' + user_id)
	response = requests.get(GET_USER_URL)

	if (response.ok):
		return response
	else:
		None

#Find user by id
def find_users_by_id(user_id):
	FIND_USER_URL = urljoin(BASE_URL, 'users?id=' + user_id)
	response = requests.get(FIND_USER_URL)

	if(response.ok):
		return response
	else:
		None

#Find user by name
def find_users_by_name(name):
	FIND_USER_URL = urljoin(BASE_URL, 'users?name=' + name)
	response = requests.get(FIND_USER_URL)

	if (response.ok):
		return response
	else:
		None

#Find user by username
def find_users_by_username(username):
	FIND_USER_URL = urljoin(BASE_URL, 'users?username=' + username)
	response = requests.get(FIND_USER_URL)

	if (response.ok):
		return response
	else:
		None

# Find user by email
def find_users_by_email(email):
	FIND_USER_URL = urljoin(BASE_URL, 'users?email=' + email)
	response = requests.get(FIND_USER_URL)

	if (response.ok):
		return response
	else:
		None

# Create new user
def create_user(data):
	CREATE_USER_URL = urljoin(BASE_URL, 'users')
	response = requests.post(CREATE_USER_URL, data=data)

	if(response.ok):
		return response
	else:
		None

# Update user
def update_user(user_id, data):
	UPDATE_USER_URL = urljoin(BASE_URL, 'users/' + user_id)
	response = requests.put(UPDATE_USER_URL, data)

	if(response.ok):
		return response
	else:
		None

# Delete user
def delete_user(user_id):
	DELETE_USER_URL = urljoin(BASE_URL, 'users/' + user_id)
	response = requests.delete(DELETE_USER_URL)

	if(response.ok):
		return response
	else:
		None
