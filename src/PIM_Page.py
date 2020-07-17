from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


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
pim_page_header = "Employee Information"

# locators
# login page locators

id_username = 'txtUsername'
name_password = 'txtPassword'
class_login = 'button'

# Home Page locator
id_pim = "menu_pim_viewPimModule"
link_text_logout = "Logout"

# Admin page locator
tag_pim_header = "h1"

# Set up

driver = webdriver.Safari()
driver.get(url)
driver.maximize_window()

# Test Steps : Login Page

text_box_username = driver.find_element_by_id(id_username)
text_box_username.send_keys(username)

text_box_password = driver.find_element_by_name(name_password)
text_box_password.send_keys(password)

button_box_login = driver.find_element_by_class_name(class_login)
button_box_login.click()

wait = WebDriverWait(driver,20)
tab_menu = wait.until(EC.visibility_of(driver.find_element_by_id(id_pim)))

print(tab_menu.text)
tab_menu.click()
pim_header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, tag_pim_header)))

try:
    assert pim_header.text == pim_page_header
    print(pim_header.text)
    print("PIM test cases passed for user: " + username)
except AssertionError:
    print('Assertion Failed:', pim_page_header, 'header not found in', mainmenu, 'Page')
finally:

    driver.close()
