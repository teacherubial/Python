# auto_downloader.py
# Tim Ubial

import os       # handle files
import requests # communicate using http
import bs4      # beautiful soup - parse HTML info

# Auto downloads the xkcd comic starting with todays

url = "https://xkcd.com"       # starting url

for _ in range(1):
    # TODO: download the page
    print(f"Downloading page {url}...")
    
    response = requests.get(url)  # grabs the page info
    response.raise_for_status()
    print(response.text)

    # TODO: find the url of the of the comic image
    # TODO: download the image
    # TODO: save the file to a specific folder
    # TODO: go to the next image -> getting the prev button's url