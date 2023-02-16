import requests
from bs4 import BeautifulSoup
import time
import board
import neopixel


#                    WILL VARY DEPENDING ON PHYSICAL SETUP!               #
###########################################################################

# Choose pin lights are connected to, along with total number of lights
pixels = neopixel.NeoPixel(board.D18, 44) 

# Choose amount of time you would like the map to wait before
# another reading in seconds, at least 10 mins to avoid spam filters
# 600 seconds is default
update_interval = 600

# URL's that function pulls from
urls=[['https://metar-taf.com/KPVC','https://metar-taf.com/KHYA','https://metar-taf.com/KACK','https://metar-taf.com/KMVY',
'https://metar-taf.com/KPYM','https://metar-taf.com/KEWB','https://metar-taf.com/KOWD','https://metar-taf.com/KBOS',
'https://metar-taf.com/KBED','https://metar-taf.com/KPSM','https://metar-taf.com/KSFM','https://metar-taf.com/KLCI',
'https://metar-taf.com/KCON','https://metar-taf.com/KASH','https://metar-taf.com/KFIT','https://metar-taf.com/KORH',
'https://metar-taf.com/KPVD','https://metar-taf.com/KBID','https://metar-taf.com/KGON','https://metar-taf.com/KIJD',
'https://metar-taf.com/KBDL','https://metar-taf.com/KBAF','https://metar-taf.com/KCEF','https://metar-taf.com/KORE',
'https://metar-taf.com/KEEN','https://metar-taf.com/KVSF','https://metar-taf.com/KGFL','https://metar-taf.com/KALB',
'https://metar-taf.com/KAQW','https://metar-taf.com/KPSF','https://metar-taf.com/KPOU','https://metar-taf.com/KDXR',
'https://metar-taf.com/KHVN',],
[12,9,10,8,13,14,44,43,42,40,39,37,35,34,33,32,15,6,5,17,18,19,20,31,30,29,27,25,22,23,0,2,3]]

###########################################################################

pixels.fill((0,0,0)) # Start all lights as off    

def scrape(url1,url2):
    # Function that scrapes HTML data   
    t1 = time.perf_counter() # Keep Track of time
    r = requests.get(url1)  # Access HTML of web page
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    Reading = (soup.find(class_= 'mb-0 align-self-center'))  # Location of data we want to scrape
    RL =(Reading.text)
    if RL == 'VFR':
        pixels[url2] = (255,0,0)
        print("VFR")
    elif RL == 'MVFR':
        pixels[url2] = (0,0,255)
        print("MVFR")
    elif RL == 'IFR':
        pixels[url2] = (0,255,0)
        print("IFR")
    elif RL =='LIFR':
        pixels[url2] = (0,255,255)
        print("LIFR")
    t2 = time.perf_counter()
    print("Network Latency: " + str(t2-t1)+ " s")  # Display Network Latency

while True:
    # Loop to update map
    try:
        addresses = urls[0]

        for airport_count, airport in enumerate(addresses):  # Use predetermined LED numbers and URL to scrape data
            try:

                current_URL = urls[0][airport_count]
                current_LED = urls[1][airport_count]
                print("Data Scrape at: " + current_URL + " | LED: "+ str(current_LED))
                scrape(current_URL,current_LED)
                time.sleep(0.5)  # Avoid rapid website searching which usually causes errors

            except:
                # Execute in case of error at specific URL
                print("Error in finding data, skipping...")

        print("Cycle Completed")
        time.sleep(update_interval)

    except:
        # Execute in case of any unknown, unforseen error
        print("Unknown Error, skipping...")
