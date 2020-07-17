from selenium import webdriver
from selenium.common.exceptions import InvalidSessionIdException


# Set up data

path = '../drivers/chromedriver'
url = 'https://opensource-demo.orangehrmlive.com'

# login data
login_url = url + "/index.php/auth/login"
username = 'Admin'
password = 'admin123'

# locators
# login page locators

id_username = 'txtUsername'
name_password = 'txtPassword'
class_login = 'button'

# Home Page locator
partial_link_text_welcome_msg = "Welcome"
link_text_logout = "Logout"

# Set up

driver = webdriver.Chrome(path)
driver.implicitly_wait(10)
driver.get(url)
driver.maximize_window()

# Test Steps : Login Page

text_box_username = driver.find_element_by_id(id_username)
text_box_username.send_keys(username)

text_box_password = driver.find_element_by_name(name_password)
text_box_password.send_keys(password)

button_box_login = driver.find_element_by_class_name(class_login)
button_box_login.click()

#  Test Steps : Home Page

link_welcome_msg = driver.find_element_by_partial_link_text(partial_link_text_welcome_msg)
try:
    assert link_welcome_msg.text == partial_link_text_welcome_msg + username
except AssertionError:
    print("Assertion fail message is not correct ")

link_welcome_msg.click()
link_logout = driver.find_element_by_link_text(link_text_logout)
link_logout.click()

try:
    assert driver.current_url == login_url
except AssertionError:
    print("Assertion failed = After log out login page is not loader ")
    driver.close()

print("Login test case passed for user:" + username)

# teardown
driver.close()
