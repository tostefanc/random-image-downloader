from bs4 import BeautifulSoup
import random
import requests
import string
import shutil
import os


images_dir = "image_dump"
check_folder = os.path.isdir(images_dir)

if not check_folder:
    os.makedirs(images_dir)
    print("Created the image dump folder:", images_dir)

def download_the_image(count=1):
    folder = os.getcwd() + '\image_dump'
    for times in range(int(count)):
        the_numbers = random.randrange(1000, 9999)
        first_letter = random.choice(string.ascii_letters).lower()
        second_letter = random.choice(string.ascii_letters).lower()
        link = "https://prnt.sc/" + first_letter + second_letter + str(the_numbers)
        data = requests.get(link, headers={'User-Agent': 'Chrome'})
        soup = BeautifulSoup(data.content, 'html.parser')
        img = soup.find(id='screenshot-image')
        image_name_short = img['src'].split('/')
        image_source = img['src']
        image_data_request = requests.get(image_source, stream=True, headers={'User-Agent': 'Chrome'})
        if image_data_request.status_code == 200:
            image_data_request.raw.decode_content = True
            with open(image_name_short[-1], 'wb') as f:
                shutil.copyfileobj(image_data_request.raw, f)
            shutil.copy(image_name_short[-1], folder)
            print("Image downloaded:", image_name_short[-1])
            os.remove(image_name_short[-1])
        else:
            print("Status code is:", image_data_request.status_code)


download_the_image()
