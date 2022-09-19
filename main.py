'''
    Badminton Search
    Anirudh Koteshwar
    19-09-2022
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os 
import time 
import sys

#use the firefox webdriver (geckodriver)
driver = webdriver.Firefox() 

#open google maps
driver.get('https://maps.google.com') 
driver.implicitly_wait(5)

#find the searchbox and click on it
searchbox = driver.find_element(By.ID, 'searchboxinput') 
driver.implicitly_wait(5)
searchbox.click()

#search for badminton courts
searchbox.send_keys('badminton courts in India')
time.sleep(5)
searchbutton = driver.find_element(By.ID, 'searchbox-searchbutton')
searchbutton.click()

#find all court names
entries = driver.find_elements(By.CLASS_NAME, 'hfpxzc')

for entry in entries:
    name = entry.get_attribute("aria-label")
    with open("courts.txt", 'a') as file:
        file.write(f"{name}\n")


#terminate the session
driver.close() 
driver.quit() 

