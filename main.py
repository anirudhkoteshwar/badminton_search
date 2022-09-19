'''
    Badminton Search
    Anirudh Koteshwar
    19-09-2022
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os 

driver = webdriver.Firefox() #use the firefox webdriver (geckodriver)
driver.get('https://www.google.com/maps/@12.9601203,77.5955137,12.12z') #open google maps
driver.implicitly_wait(5) #wait for 3 seconds if webpage loads slowly
searchbox = driver.find_element(By.ID, 'searchboxinput') #find the searchbox
driver.implicitly_wait(5)
searchbox.click() #click on the searchbox
driver.implicitly_wait(1)
searchbox.send_keys('badminton courts')
driver.implicitly_wait(5)
searchbutton = driver.find_element(By.ID, 'searchbox-searchbutton')
searchbutton.click()


