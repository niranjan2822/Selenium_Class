from selenium import webdriver
from time import sleep

# setup_data
exe_path = '../drivers/chromedriver'
URL = 'https://opensource-demo.orangehrmlive.com'

# login_data
login_url = URL + "/index.php/auth/login"
username = 'Admin'
passwd = 'admin123'

# Home_page_data
mainmenu = "Admin"

# Admin_page_data
ap_header = "System Users"

# locators
# LoginPage_locators
id_username = "txtUsername"

# class_username = "form-hint" #- wrong_locator
name_passwd = "txtPassword"
class_login = "button"

# HomePage locators
plt_welcome_msg = "Welcome "
tag_maintabs = "b"
lt_logout = "Logout"

# AdminPage Locator
tag_ap_header = "h1"

# setup
driver = webdriver.Chrome(exe_path)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(URL)

# test steps - LoginPage
# tb_username = driver.find_element(by=By.PARTIAL_LINK_TEXT,value=id_username)
tb_username = driver.find_element_by_id(id_username)
tb_username.send_keys(username)

tb_passwd = driver.find_element_by_name(name_passwd)
tb_passwd.send_keys(passwd)

btn_login = driver.find_element_by_class_name(class_login)
btn_login.click()

tab_menu = driver.find_elements_by_tag_name(tag_maintabs)
for menu in tab_menu:
    if menu.text == mainmenu:
        menu.click()
        break
else:
    print(mainmenu, 'tab not found')
    print("Test cases Failed for Tab: " + mainmenu)
    driver.close()

try:
    assert driver.find_element_by_tag_name(tag_ap_header).text == ap_header
    print("Admin Test cases passed for user: " + username)
except AssertionError:
    print('Assertion Failed:', ap_header, 'header not found in', mainmenu, 'Page')
finally:
    driver.delete_all_cookies()
    driver.get(URL)
    driver.get_screenshot_as_file("with_delete_cookie.png")
    driver.close()
