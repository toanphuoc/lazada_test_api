try:
	from urllib.parse import urljoin
except ImportError:
	from urlparse import urljoin

import requests

from constants import BASE_URL

def get_users():

	GET_USERS_URL = urljoin(BASE_URL, 'users')
	
	response = requests.get(GET_USERS_URL)

	if(response.ok):
		users = response.json()
		return users
	else:
		None

def find_users():
	FIND_USER_URL = urljoin(BASE_URL, 'users', 1)
	response = requests.get(FIND_USER_URL)

	if(response.ok):
		return  response
	else:
		None

