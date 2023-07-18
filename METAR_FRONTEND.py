# General Imports #####################################################

from __future__ import print_function
from time import sleep,localtime,asctime
import os.path
import neopixel
import board

# Google Imports ######################################################

import gspread
from oauth2client.service_account import ServiceAccountCredentials

###########################################################################


#                    WILL VARY DEPENDING ON PHYSICAL SETUP!               
###########################################################################

# Choose pin lights are connected to, along with total number of lights
pixels = neopixel.NeoPixel(board.D18, 44) 
pixels.fill((0,0,0)) # Start all lights as off

# Choose amount of time you would like the map to wait before
# another reading in seconds, 120 seconds is default
update_interval = 120



urls = ['https://metar-taf.com/KPVC','https://metar-taf.com/KHYA','https://metar-taf.com/KACK','https://metar-taf.com/KMVY',
'https://metar-taf.com/KPYM','https://metar-taf.com/KEWB','https://metar-taf.com/KOWD','https://metar-taf.com/KBOS',
'https://metar-taf.com/KBED','https://metar-taf.com/KPSM','https://metar-taf.com/KSFM','https://metar-taf.com/KLCI',
'https://metar-taf.com/KCON','https://metar-taf.com/KASH','https://metar-taf.com/KFIT','https://metar-taf.com/KORH',
'https://metar-taf.com/KPVD','https://metar-taf.com/KBID','https://metar-taf.com/KGON','https://metar-taf.com/KIJD',
'https://metar-taf.com/KBDL','https://metar-taf.com/KBAF','https://metar-taf.com/KCEF','https://metar-taf.com/KORE',
'https://metar-taf.com/KEEN','https://metar-taf.com/KVSF','https://metar-taf.com/KGFL','https://metar-taf.com/KALB',
'https://metar-taf.com/KAQW','https://metar-taf.com/KPSF','https://metar-taf.com/KPOU','https://metar-taf.com/KDXR',
'https://metar-taf.com/KHVN']


def main():
    scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('frontend.json',scope)
    # intitialize the authorization object            
    gc = gspread.authorize(credentials)
    # Open Google Sheets file
    sheet = gc.open('METARMAP').sheet1

    for i in range(len(urls)):

        row = str(i + 2)

        led = sheet.get_values("B" + row)
        led = led.strip("[]")

        try:
            current = sheet.get_values("C" + row)
            current = current.strip("[]")

            if current == 'VFR':
                pixels[led] = (255,0,0)
                print("VFR")
            elif current == 'MVFR':
                pixels[led] = (0,0,255)
                print("MVFR")
            elif current == 'IFR':
                pixels[led] = (0,255,0)
                print("IFR")
            elif current =='LIFR':
                pixels[led] = (0,255,255)
                print("LIFR")

        except:
            print('Error Occurred')
            pixels[led] = (0,0,0)





if __name__ == '__main__':
    while True:
        main()
        sleep(update_interval)