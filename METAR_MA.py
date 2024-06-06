# General Imports #####################################################

from __future__ import print_function
import os.path
from time import sleep
import neopixel
import board


# Webdriver Imports ###################################################

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium.webdriver.support import expected_conditions as EC

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

interval = 600
# Choose pin lights are connected to, along with total number of lights
pixels = neopixel.NeoPixel(board.D18, 44) 
pixels.fill((0,0,0)) # Start all lights as off

def init():
    # Create Web Driver using options to remain under the radar
    global driver

    # Options to remove flags that show page is bot controlled
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")

    # Generate Random User Agent to prevent being detected
    ua = UserAgent()
    user_agent = ua.random
    options.set_preference("general.useragent.override", user_agent)

    # Initialize Firefox Driver
    service = FirefoxService(executable_path='/usr/local/bin/geckodriver')
    #driver = webdriver.Firefox(service=service, options=options)
    driver = webdriver.Firefox(service='/usr/local/bin/geckodriver')
    
    return driver

def main():
    for i in range(len(urls)):
        airport_path = urls[i]
        driver.get(airport_path)
        current = waitToLoad_storage("XPATH", "/html/body/div[2]/div/div/div[3]/div[1]/div/div[1]/h3").text
        driver.quit()

        try:
            if current == 'VFR':
                pixels[i] = (255,0,0)
                print("VFR")
            elif current == 'MVFR':
                pixels[i] = (0,0,255)
                print("MVFR")
            elif current == 'IFR':
                pixels[i] = (0,255,0)
                print("IFR")
            elif current == 'LIFR':
                pixels[i] = (0,255,255)
                print("LIFR")
        except:
            print('Error Occurred')
            pixels[i] = (0,0,0)

def waitToLoad_click(bytype, id):
    # Wait for <a> to load and then click
    for i in range(3):
        try:
            if bytype == "XPATH":
                WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.XPATH, id)))
                driver.find_element(By.XPATH, id).click()
            elif bytype == "ID":
                WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.ID, id)))
                driver.find_element(By.ID, id).click()
            elif bytype == "LINK_TEXT":
                WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.LINK_TEXT, id)))
                driver.find_element(By.LINK_TEXT, id).click()
            elif bytype == "CLASS_NAME":
                WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.CLASS_NAME, id)))
                driver.find_element(By.LINK_TEXT, id).click()
            elif bytype == "CSS":
                WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.CSS_SELECTOR, id)))
                driver.find_element(By.LINK_TEXT, id).click()
            elif bytype == "TAG_NAME":
                WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.TAG_NAME, id)))
                driver.find_element(By.TAG_NAME, id).click()
        except:
            sleep(1)

def waitToLoad_storage(bytype, id):
    # Wait for <a> to load and then return element
    for i in range(3):
        try:
            if bytype == "XPATH":
                WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.XPATH, id)))
                return driver.find_element(By.XPATH, id)
            elif bytype == "ID":
                WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.ID, id)))
                return driver.find_element(By.ID, id)
            elif bytype == "LINK_TEXT":
                WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.LINK_TEXT, id)))
                return driver.find_element(By.LINK_TEXT, id)
            elif bytype == "CLASS_NAME":
                WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.CLASS_NAME, id)))
                return driver.find_element(By.LINK_TEXT, id)
            elif bytype == "CSS":
                WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.CSS_SELECTOR, id)))
                return driver.find_element(By.LINK_TEXT, id)
            elif bytype == "TAG_NAME":
                WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.TAG_NAME, id)))
                return driver.find_element(By.TAG_NAME, id)
        except:
            sleep(1)

if __name__ == "__main__":
    init()
    while True:
        main()
        sleep(interval)
