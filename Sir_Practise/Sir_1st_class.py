from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep


# setup_data
exe_path = '../drivers/chromedriver'
URL = 'https://opensource-demo.orangehrmlive.com'
# login_data
login_url = URL + "/index.php/auth/login"
username = 'Admin'
passwd = 'admin123'

# locators
# LoginPage_locators
id_username = "txtUsername"
name_passwd = "txtPassword"
class_login = "button"

# HomePage locators
plt_welcome_msg = "Welcome"
lt_logout = "Logout"

# setup
driver = webdriver.Chrome(exe_path)
driver.get(URL)

# test steps - LoginPage
#tb_username = driver.find_element(by=By.PARTIAL_LINK_TEXT,value=id_username)
tb_username = driver.find_element_by_id(id_username)
tb_username.send_keys(username)

tb_passwd = driver.find_element_by_name(name_passwd)
tb_passwd.send_keys(passwd)

btn_login = driver.find_element_by_class_name(class_login)
btn_login.click()

# test steps - HomePage
lnk_welcome_msg = driver.find_element_by_partial_link_text(plt_welcome_msg)
try:
    assert lnk_welcome_msg.text == plt_welcome_msg + username
except AssertionError:
    print('Assertion Failed: Welcome Message is not as expected')

lnk_welcome_msg.click()
sleep(2)  # to avoid NoSuchElementException

lnk_logout = driver.find_element_by_link_text(lt_logout)
lnk_logout.click()

try:
    assert driver.current_url == login_url
except AssertionError:
    print('Assertion Failed: After Logout, Login Page is not loaded')
    driver.close()

print("Login Test cases passed for user: " + username)

# teardown
driver.close()
