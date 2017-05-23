from urllib.parse import urljoin
import requests
from functools import reduce

from constants import BASE_URL

def get_users():
	GET_USER_URL = urljoin(BASE_URL, 'users')
	response = requests.get(GET_USER_URL)

	if(response.ok):
		return  response
	else:
		None

def find_users_by_id(user_id):
	FIND_USER_URL = urljoin(BASE_URL, 'users?id=' + user_id)
	response = requests.get(FIND_USER_URL)

	if(response.ok):
		return response
	else:
		None

def find_users_by_name(name):
	FIND_USER_URL = urljoin(BASE_URL, 'users?name=' + name)
	response = requests.get(FIND_USER_URL)

	if (response.ok):
		return response
	else:
		None

def find_users_by_email(email):
	FIND_USER_URL = urljoin(BASE_URL, 'users?email=' + email)
	response = requests.get(FIND_USER_URL)

	if (response.ok):
		return response
	else:
		None

def create_user(data):
	CREATE_USER_URL = urljoin(BASE_URL, 'users')
	response = requests.post(CREATE_USER_URL, data)

	if(response.ok):
		return response
	else:
		None

def update_user(user_id, data):
	UPDATE_USER_URL = urljoin(BASE_URL, 'users/' + user_id)
	response = requests.put(UPDATE_USER_URL, data)

	if(response.ok):
		return response
	else:
		None

def delete_user(user_id):
	DELETE_USER_URL = urljoin(BASE_URL, 'users/' + user_id)
	response = requests.delete(DELETE_USER_URL)

	if(response.ok):
		return response
	else:
		None
