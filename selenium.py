from typing import KeysView
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os 
import wget




path = 'C:/Users/HaKuRe/Desktop/python/bug/chromedriver.exe'
driver = webdriver.Chrome(path)

driver.get("https://hornydragon.blogspot.com/")

titles = driver.find_element_by_class_name("post-title")
print(titles.text)
link = driver.find_element_by_link_text(titles.text)
link.click()

#for title in titles: #^element need to elements    
#    print(title.text) #列出全部的標題
WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "tr-caption-container"))
    )
imgs =driver.find_element_by_class_name('tr-caption-container')

#path = os.path.join(titles.text)
#os.mkdir(path)
count = 0
for img in imgs:
    #save_as = os.path.join(path,titles.text + str(count)+ '.jpg')
    print(img.get_attribute('src'))
    #wget.download(img.get_attribute("src"),save_as)

    count += 1

#driver.quit()
