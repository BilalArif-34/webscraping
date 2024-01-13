
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


url = "https://www.trendyol.com/bilgisayar-x-c108656"
driver.get(url)
driver.maximize_window()
SCROLL_PAUSE_TIME = 2


 
def scroll_page():
    for Y in range(500,1080*100,1080):
        # print(Y)
        driver.execute_script("window.scrollTo(0, '{}');".format(Y))
        time.sleep(1)
        # print("I am scrolling")
# infinite page with lazy load and footer where driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") solution doesn't work!
        
def get_listing_detail():

    scroll_page()

    brand_name=driver.find_elements(By.CSS_SELECTOR, ".prdct-cntnr-wrppr .p-card-wrppr h3 span:nth-child(1)")
    brand_name_list=[]
    for item in brand_name:
          brand_name_list.append(item.text)


    brand_detail=driver.find_elements(By.CSS_SELECTOR, ".prdct-cntnr-wrppr .p-card-wrppr h3 span:nth-child(2)")
    brand_detail_list=[]
    for item in brand_detail:
          brand_detail_list.append(item.text)


    list_ = list(zip(brand_name_list, brand_detail_list))
    count=0
    for x in list_:
         print ("count: {}".format(count), "Brand_Name: {}".format(x[0]),"Product_Details: {}".format(x[1]))
         count+=1




get_listing_detail()

print("I am out of loop")
time.sleep(5)
driver.close()