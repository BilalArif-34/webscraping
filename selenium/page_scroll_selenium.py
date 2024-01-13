
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


url = "https://shredcapital.com/?ref=onepagelove"
driver.get(url)
driver.maximize_window()
SCROLL_PAUSE_TIME = 2


def scroll_page():

    last_height = driver.execute_script("return document.body.scrollHeight/4")
    document_height=1000000

    while True:
            # delta is the increment in height each time loops iterate
            delta = 1080
            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)
            # Calculate new scroll height and compare with last scroll height
            new_height = last_height+delta
            # checks if scrollTo is still scrolling 
            if new_height < document_height:
                driver.execute_script("window.scrollTo(0, {});".format(new_height))
                last_height=new_height
                print("last_height",last_height)
                # After scrolling and page load the new total height of document, will give the max height of document
                document_height=driver.execute_script("return document.body.scrollHeight")
                print("document_total_height",document_height)

            else:
                break

scroll_page()

print("I am out..")
time.sleep(5)
driver.close()