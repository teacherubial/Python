# auto_downloader.py
# Tim Ubial

import os       # handle files
import requests # communicate using http
import bs4      # beautiful soup - parse HTML info

# Auto downloads the xkcd comic starting with todays

url = "https://xkcd.com"       # starting url

while not url.endswith("#"):
    # download the page
    print(f"Downloading page {url}...")
    
    response = requests.get(url)  # grabs the page info
    response.raise_for_status()

    # find the url of the of the comic image
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    comic_element = soup.select("#comic img")

    if not comic_element:       # if search is empty
        print("Could not find image.")
    else:
        comic_url = "https:" + comic_element[0].get("src")

        # download the image
        print(f"Downloading {comic_url}...")

        response = requests.get(comic_url)
        response.raise_for_status()

        # save the file to a specific folder
        with open(os.path.join("xkcd_images", os.path.basename(comic_url)), "wb") as image_file:
            # Fill the file in 100000 byte chunks

            for chunk in response.iter_content(100_000):
                image_file.write(chunk)

    # go to the next image -> getting the prev button's url
    previous_element = soup.select('a[rel="prev"]')

    url = "https://xkcd.com" + previous_element[0].get("href")

print("Done.")