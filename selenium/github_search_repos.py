

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time 
options= Options()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)


url = "http://github.com"
driver.get(url)
driver.maximize_window()
time.sleep(1)

search_button = driver.find_element(By.CLASS_NAME, "header-search-button")
# search button is selected
time.sleep(1)
search_button.click()
# the action will select and place the curson in your search bar
time.sleep(2)
field=driver.find_element(By.ID, "query-builder-test")
# target the input tag
field.send_keys('python')
field.send_keys(Keys.ENTER)
# send the search keyword to the input 
time.sleep(5)


result = driver.find_elements(By.CSS_SELECTOR, ".Box-sc-g0xbh4-0 .kzrAHr .hKtuLA h3")
print(result)
for element in result:
    print(element.text)

time.sleep(5)

driver.close()

