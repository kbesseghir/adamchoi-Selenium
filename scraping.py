from selenium import webdriver
from selenium.webdriver.common.by import By

website = 'https://www.adamchoi.co.uk/overs/detailed'
# path ='/home/kheira/Downloads/chromedriver'
driver = webdriver.Chrome()
driver.get(website)

all_matches_button =driver.find_element(By.XPATH, " //label[@analytics-event='All matches']")
all_matches_button.click()