from selenium import webdriver

# Set up data

path = '../drivers/chromedriver'
url = 'https://opensource-demo.orangehrmlive.com'

# login data
login_url = url + "/index.php/auth/login"
username = 'Admin'
password = 'admin123'

# Home Page Data
mainmenu = "PIM"

# Admin page data
admin_page_header = "Employee Information"

# locators
# login page locators

id_username = 'txtUsername'
name_password = 'txtPassword'
class_login = 'button'

# Home Page locator
# id_admin = "menu_admin_viewAdminModule"
tag_tabMenu = "b"
link_text_logout = "Logout"

# Admin page locator
tag_admin_header = "h1"

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

tab_menu = driver.find_elements_by_tag_name(tag_tabMenu)
for menu in tab_menu:
    if menu.text == mainmenu:
        menu.click()
        break
else:
    print(mainmenu, 'tab not found')
    print("Test cases Failed for Tab: " + mainmenu)
    driver.close()

try:
    assert driver.find_element_by_tag_name(tag_admin_header).text == admin_page_header
    print("Admin Test cases passed for user: " + username)
except AssertionError:
    print('Assertion Failed:', admin_page_header, 'header not found in', mainmenu, 'Page')
finally:
    driver.delete_all_cookies()
    driver.get(url)
    driver.get_screenshot_as_file("with_delete_cookie.png")
    driver.close()
