from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import time
website = 'https://www.adamchoi.co.uk/overs/detailed'
# path ='/home/kheira/Downloads/chromedriver'
driver = webdriver.Chrome()
driver.get(website)

all_matches_button =driver.find_element(By.XPATH, " //label[@analytics-event='All matches']")
all_matches_button.click()

# select dropdown and select element inside by visible text
dropdown = Select(driver.find_element(By.ID,'country'))
dropdown.select_by_visible_text('Spain')
# implicit wait (useful in JavaScript driven websites when elements need seconds to load and avoid error "ElementNotVisibleException")
time.sleep(3)

rows = driver.find_elements(By.TAG_NAME,'tr')
dates=[]
teamsA=[]
teamsB=[]
scores=[]

for row in rows:
    date = row.find_element(By.XPATH,"./td[1]").text


    dates.append(date)
    teamsA.append(row.find_element(By.XPATH,"./td[@class='ng-binding'][2]").text)
    teamsB.append(row.find_element(By.XPATH,"./td[4]").text)
    scores.append(row.find_element(By.XPATH,"./td[3]").text)


driver.quit()

df=pd.DataFrame({'dates':teamsA})
df.to_csv('football_data.csv', index=False)



