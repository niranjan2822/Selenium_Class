from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('../drivers/chromedriver')
driver.get("https://google.com")
sleep(10)
driver.close()