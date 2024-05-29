import requests
from bs4 import BeautifulSoup
import os
import urllib.request
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# PATH = '/Users/nathanielserrano/Downloads/chromedriver-mac-x64/chromedriver.exe'
# service = webdriver.ChromeService(executable_path = PATH)
# driver = webdriver.Chrome(service=service)


# Function to create a directory if it does not exist
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to download an image from a URL and save it to a directory
def download_image(image_url, save_directory, image_name):
    image_path = os.path.join(save_directory, image_name)
    urllib.request.urlretrieve(image_url, image_path)
    print(f"Downloaded {image_name}")

# Function to scrape images from a WGA page
def scrape_images_from_wga(page_url, save_directory, delay=1):
    # Fetch the HTML content of the page
    response = requests.get(page_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Create the directory to save images
    create_directory(save_directory)

    # Find all tables on the page
    tables = soup.find_all('table')

    driver.switch_to.frame('buttonframe')


    # Check if there are tables on the page
    if tables:
        for table in tables:
            # Find all image tags within each table
            image_tags = table.find_all('img')
            for img_tag in image_tags:
                img_url = img_tag.get('src')
                if img_url:
                    # Construct the full image URL if it's relative
                    if not img_url.startswith('http'):
                        img_url = f"https://www.wga.hu{img_url}"
                    # Extract the image name from the URL
                    img_name = img_url.split('/')[-1]
                    # Download the image
                    download_image(img_url, save_directory, img_name)
                    # Delay between requests
                    time.sleep(delay)
    else:
        print("No tables found on the page.")

# URL of the WGA page to scrape
wga_page_url = 'https://www.wga.hu/frames-e.html?/html/a/aachen/index.html'
# Directory to save the images on the Mac desktop
save_dir = os.path.expanduser('~/Desktop/wga_images')
# Delay in seconds between each request
request_delay = 1

# Scrape images from the specified WGA page and save them
scrape_images_from_wga(wga_page_url, save_dir, delay=request_delay)
