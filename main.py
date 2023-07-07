from captive import captive_login
from curpl import is_internet_enabled
from helper import get_rn_string
import time

while True:
	print("------------------------\nChecking if Internet connected @", get_rn_string())
	if not is_internet_enabled():
		print("Unable to connect, Attempting captive login now")
		captive_login()
	else:
		print("Able to successfully connect to internet.")

	time.sleep(60) #1 min
