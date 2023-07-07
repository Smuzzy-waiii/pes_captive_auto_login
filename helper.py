from datetime import datetime

def get_rn_string():
	current_time = datetime.now()
	formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
	return formatted_time