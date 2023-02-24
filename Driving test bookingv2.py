from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime

x = datetime.datetime.now()
date = datetime.datetime.now()
date = date.strftime("%d")
date = int(date) + 1
thedate = str(date) + "/02/2023"
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

browser.get('https://online.transport.wa.gov.au/pdabooking/manage/?0')
search = browser.find_element(by=By.CSS_SELECTOR, value="#id7 > ol > li:nth-child(8) > div > input[type=text]")
search.send_keys("") #Insert license number here
search = browser.find_element(by=By.CSS_SELECTOR, value="#licenceExpiryDatePicker")
search.send_keys("") #Insert license expiry here
search = browser.find_element(by=By.CSS_SELECTOR, value="#id7 > ol > li:nth-child(12) > div > input[type=text]")
search.send_keys("") #Insert first name
search = browser.find_element(by=By.CSS_SELECTOR, value="#id7 > ol > li:nth-child(13) > div > input[type=text]")
search.send_keys("") #Insert last name
search = browser.find_element(by=By.CSS_SELECTOR, value="#dateOfBirthPicker")
search.send_keys("") #Insert date of birth

try:
    e = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#ide-METRO"))
    )
finally:
    e= "e"

search = browser.find_element(by=By.CSS_SELECTOR, value="#fromDateInput")
search.send_keys(thedate)
search = browser.find_element(by=By.CSS_SELECTOR, value="#toDateInput")
search.send_keys("30/05/2023")
search = browser.find_element(by=By.CSS_SELECTOR, value="#idf-searchBookingContainer\:siteList_MBK").click()
search = browser.find_element(by=By.CSS_SELECTOR, value="#idf-searchBookingContainer\:siteList_MID").click()
search = browser.find_element(by=By.CSS_SELECTOR, value="#idf-searchBookingContainer\:siteList_CTYW").click()
search = browser.find_element(by=By.CSS_SELECTOR, value="#idf-searchBookingContainer\:siteList_JNP").click()
search = browser.find_element(by=By.CSS_SELECTOR, value="#id15").click()
close = input("Enter any key to close the program")


