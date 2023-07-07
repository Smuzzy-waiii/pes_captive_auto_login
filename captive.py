from selenium import webdriver
import os

def captive_login():
    #Get username and password from env vars first
    username = os.environ.get('CAPTIVE_USERNAME')
    password = os.environ.get('CAPTIVE_PASSWORD')
    selenium_url = os.environ.get('SELENIUM_URL')
    print(f"Using username: {username} and password: {password} @ {selenium_url}")

    if (username==None or password==None):
        print("Error: CAPTIVE_USERNAME and CAPTIVE_PASSWORD env variables not set.")
        return False

    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-ssl-errors=yes")
    options.add_argument("--ignore-certificate-errors")
    # options.add_argument("--disable-dev-shm-usage")

    print("Opening Chrome")

    driver = webdriver.Remote(options=options, command_executor=selenium_url)
    print("Opened Remote")

    driver.get("http://192.168.254.1:8090")
    driver.implicitly_wait(10)

    print("Opened connection")

    username_field = driver.find_element("name", "username")
    pass_field = driver.find_element("name", "password")

    username_field.send_keys(username)
    pass_field.send_keys(password)

    login_button = driver.find_element("id", "loginbutton")
    login_button.click()

    login_button = driver.find_element("id", "loginbutton")
    text = login_button.get_attribute("innerHTML")

    driver.quit()

    if (text=="Logout"):
        print("Successfully logged in to captive.")
        return True
    else:
        print("Did not successfully log in to captive")
        return False

if __name__ == "__main__":
    captive_login()
