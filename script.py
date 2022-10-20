from dataclasses import dataclass
from bs4 import BeautifulSoup
import requests
import wget

url = 'https://danbooru.donmai.us/posts/5730810?q=minato_aqua+rating%3Ag+'

def make_data(url):
    data = requests.get(url)
    soup = BeautifulSoup(data.text,'html.parser')

    image_url = soup.find('section', id='content').find('section')['data-file-url']
    print('Downloading from: ' + image_url)
    image_file_name = wget.download(image_url)

    characters = soup.find('ul', class_="character-tag-list").find_all(class_='search-tag')
    tags = soup.find('ul', class_="general-tag-list").find_all(class_='search-tag')

    tags_string = ''
    for tag in tags:
        # print(tag.text)
        tags_string += f'{tag.text}, '
    for character in characters:
        # print(character.text)
        tags_string += f'{character.text}, '

    print(tags_string)
    with open(f'{image_file_name}.txt', 'w') as f:
        f.write(tags_string)

make_data(url)
