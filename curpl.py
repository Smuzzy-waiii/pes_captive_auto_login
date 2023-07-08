import requests

def is_internet_enabled():
	is_enabled = True

	try:
		r = requests.get("http://google.com/")
	except requests.exceptions.ConnectionError as e:
		is_enabled = False
		r = e

	is_enabled = is_enabled and (r.status_code == 200) and ("192.168.254.1:8090" not in r.text)
	if not is_enabled:
		print(f"Not able to reach internet. Response:", type(r), r)
	return is_enabled
	# returns true if google is successfully reachable

if __name__=="__main__":
	is_internet_enabled()