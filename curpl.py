import requests
conn_err = requests.exceptions.ConnectionError

def is_internet_enabled():
	try:
		r = requests.get("http://google.com/")
	except requests.exceptions.ConnectionError as e:
		r = e
	is_enabled = (r != conn_err) and (r.status_code == 200) and ("192.168.254.1:8090" not in r.text)
	if not is_enabled:
		print(f"Not able to reach internet. Response:", r)
	return is_enabled
	# returns true if google is successfully reachable