from captive import captive_login
from curpl import is_internet_enabled
from helper import get_rn_string
import time

while True:
	print("------------------------\nChecking if Internet connected @", get_rn_string())
	net_enabled = False
	try:
		net_enabled = is_internet_enabled()
	except Exception as e:
		print("Error while checking internet: ", e)
	
	if not net_enabled:
		print("Unable to connect, Attempting captive login now")
		try:
			captive_login()
		except Exception as e:
		 	print("Error during captive login: ", e)

	else:
		print("Able to successfully connect to internet.")

	time.sleep(60) #1 min
