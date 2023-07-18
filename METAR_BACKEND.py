
# General Imports #####################################################

from __future__ import print_function
from time import sleep,localtime,asctime
import os.path

# Webdriver Imports ###################################################

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#######################################################################

# Google Imports ######################################################

import gspread
from oauth2client.service_account import ServiceAccountCredentials

#######################################################################

# URL's that bot pulls from
urls=['https://metar-taf.com/KPVC','https://metar-taf.com/KHYA','https://metar-taf.com/KACK','https://metar-taf.com/KMVY',
'https://metar-taf.com/KPYM','https://metar-taf.com/KEWB','https://metar-taf.com/KOWD','https://metar-taf.com/KBOS',
'https://metar-taf.com/KBED','https://metar-taf.com/KPSM','https://metar-taf.com/KSFM','https://metar-taf.com/KLCI',
'https://metar-taf.com/KCON','https://metar-taf.com/KASH','https://metar-taf.com/KFIT','https://metar-taf.com/KORH',
'https://metar-taf.com/KPVD','https://metar-taf.com/KBID','https://metar-taf.com/KGON','https://metar-taf.com/KIJD',
'https://metar-taf.com/KBDL','https://metar-taf.com/KBAF','https://metar-taf.com/KCEF','https://metar-taf.com/KORE',
'https://metar-taf.com/KEEN','https://metar-taf.com/KVSF','https://metar-taf.com/KGFL','https://metar-taf.com/KALB',
'https://metar-taf.com/KAQW','https://metar-taf.com/KPSF','https://metar-taf.com/KPOU','https://metar-taf.com/KDXR',
'https://metar-taf.com/KHVN']

cell = "C"
airport_cells = []
interval = 600


for i in range(len(urls)):
    num = i + 2
    temp = cell + str(num)
    airport_cells.append(temp)


###########################################################################

def init():
    # Create Web Driver using options to remain under the radar
    global driver

    # Options to remove flags that show page is bot controlled
    options = Options()
    options.add_experimental_option("detach",True)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
    options.add_experimental_option("useAutomationExtension", False) 

    # Generate Random User Agent to prevent being detected
    ua = UserAgent()
    user_agent = ua.random
    options.add_argument(f'user-agent={user_agent}')

    options.add_argument("--incognito")

    # Initialize Chrome Driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)


def main():
    current_status = []

    for i in urls:
        driver.get(i)
        try:
            stat = waitToLoad_storage("XPATH","/html/body/div[3]/div/div/div[3]/div[1]/div/div[1]/h3").text
            current_status.append(stat)
        except:
            current_status.append("")
    driver.quit()
    return current_status

def upload(stats):

    scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('frontend.json',scope)

    # intitialize the authorization object            
    gc = gspread.authorize(credentials)
    # Open Google Sheets file
    sheet = gc.open('METARMAP').sheet1
    for i in range(len(stats)):
        try:
            sheet.update(str(airport_cells[i]),str(stats[i]))
        except:
            print('Error Occurred')
    return

def waitToLoad_click(bytype,id):
    # Wait for <a> to load and then click
    for i in range(3):
        try:
            if bytype == "XPATH":
                WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.XPATH,id)))
                driver.find_element(By.XPATH,id).click()
            elif bytype == "ID":
                WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.ID,id)))
                driver.find_element(By.ID,id).click()
            elif bytype == "LINK_TEXT":
                WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.LINK_TEXT,id)))
                driver.find_element(By.LINK_TEXT,id).click()
            elif bytype == "CLASS_NAME":
                WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.CLASS_NAME,id)))
                driver.find_element(By.LINK_TEXT,id).click()
            elif bytype == "CSS":
                WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.CSS_SELECTOR,id)))
                driver.find_element(By.LINK_TEXT,id).click()
            elif bytype == "TAG_NAME":
                WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.TAG_NAME,id)))
                driver.find_element(By.TAG_NAME,id).click()
        except: 
            sleep(1)

def waitToLoad_storage(bytype,id):
        # Wait for <a> to load and then return element
        for i in range(3):
            try:
                if bytype == "XPATH":
                    WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.XPATH,id)))
                    return driver.find_element(By.XPATH,id)
                elif bytype == "ID":
                    WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.ID,id)))
                    return driver.find_element(By.ID,id)
                elif bytype == "LINK_TEXT":
                    WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.LINK_TEXT,id)))
                    return driver.find_element(By.LINK_TEXT,id)
                elif bytype == "CLASS_NAME":
                    WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.CLASS_NAME,id)))
                    return driver.find_element(By.LINK_TEXT,id)
                elif bytype == "CSS":
                    WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.CSS_SELECTOR,id)))
                    return driver.find_element(By.LINK_TEXT,id)
                elif bytype == "TAG_NAME":
                    WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.TAG_NAME,id)))
                    return driver.find_element(By.TAG_NAME,id)
            except: 
                sleep(1)






if __name__ == "__main__":
    # Loop to constantly update google sheet
    init()
    while True:
        stats = main()
        upload(stats)
        sleep(interval)
