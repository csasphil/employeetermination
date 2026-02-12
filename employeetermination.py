import pyautogui as pag
import pyperclip
from pyautogui import keyDown
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui


import time
import csv

USER_NAME = input("Enter Username: ")
USER_PASS = input("Enter Password: ")
LOC_ID = input("Enter location: ")
STARTER_ID = "0000"
CSV_FILE = 'mydata.csv'

driver = webdriver.Edge()

driver.get("https://sitewatch.cloud/remote/#/welcome")
email = driver.find_element(By.ID, "inputEmail")
thepass = driver.find_element(By.ID, "inputPassword")
siteid = driver.find_element(By.ID, "inputLocation")
st_continue = driver.find_element(By.CSS_SELECTOR, ".btn-lg")
action = ActionChains(driver)



time.sleep(4)
email.click()
email.send_keys(USER_NAME)
time.sleep(2)
thepass.click()
thepass.send_keys(USER_PASS)
time.sleep(2)
siteid.click()
siteid.send_keys(LOC_ID)
time.sleep(2)

st_continue.click()




time.sleep(5)
driver.get("https://sitewatch.cloud/#/console/config/employees")
time.sleep(25)
st_search = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div[1]/div[1]/div[1]/input")
st_search.click()
st_search.send_keys(STARTER_ID)

time.sleep(8)
with open('mydata.csv', 'r') as f:
  reader = csv.reader(f)
  next(reader)  # Skip the header row
  for row in reader:
    action.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).perform()
    time.sleep(5)
    st_search.send_keys(row[0])
    time.sleep(2)
    button_edit = driver.find_element(By.XPATH, "//button[contains(text(), 'Edit Employee')]")
    actions = ActionChains(driver)

    if button_edit.is_enabled():
                print(f"Processing: {row[0]} - Button is active!")
                button_edit.click()
                time.sleep(5)
                actions.send_keys(Keys.TAB).perform()
                actions.send_keys(Keys.TAB).perform()
                action.send_keys(Keys.ENTER).perform()
                print(f"{row[0]} Terminated successfully!")
                # Small sleep to allow the UI to reset/save before the next loop
                time.sleep(15)
                st_search.click()
    else:
        print(f"{row[0]} - Employee already terminated.")
        time.sleep(15)



time.sleep(80)
