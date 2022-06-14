from errno import errorcode
import requests
from bs4 import BeautifulSoup
import sys
import os

hasSaveLocation = len(sys.argv) == 2

if (hasSaveLocation):
  saveLocation = sys.argv[1]
  print(saveLocation)
  url = "https://chicken.photos"
  response = requests.get(url)
  if (response.status_code > 200):
    print('{statusCode} Failure '.format(statusCode=response.status_code))
    print(response.json())
    exit()
  scraped = BeautifulSoup(response.content, "html.parser")

  img = scraped.find('img')

  if (img):
    src = img['src'];
    reversedSrc = src[::-1]
    indexOfLastSlash = len(reversedSrc) - reversedSrc.index("/")
    img_name = src[indexOfLastSlash:]
    img_data = requests.get(src)
    if (img_data.ok):
      fullPath = '{saveLocation}/{img_name}.jpg'.format(saveLocation=saveLocation, img_name=img_name)
      with open(fullPath, 'wb') as handler:
        handler.write(img_data.content)
      os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri {fullPath}".format(fullPath=fullPath))
    else:
      print('{error} on {url}'.format(error=img_data.status_code, url=src))
else:
  print("Missing saveLocation argument. Please specify one.")