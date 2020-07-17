from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

path = '../drivers/chromedriver'
url = 'http://demo.automationtesting.in/Windows.html'
child_win_header = "Sakinalium?"

# locator

xpath_click_btn = '//a/button'
xpath_child_win_header = "//h1/strong"

driver = webdriver.Chrome(path)
driver.maximize_window()
driver.get(url)

parent_win = driver.current_window_handle

driver.find_element(By.XPATH , xpath_click_btn).click()

all_wins = driver.window_handles
for win in all_wins:
    if win != parent_win:
        driver._switch_to.window(win)
        break

child_win_header_ele = WebDriverWait(driver , 10).until(expected_conditions.visibility_of_element_located((By.XPATH , xpath_child_win_header)))
print(child_win_header_ele.text)
driver.quit()