import requests, json, random
from bs4 import BeautifulSoup # pip install beautifulsoup4
from PIL import Image # pip install pillow

json_url = 'https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/web-cam-url-links/records?limit=100'

data = json.loads(requests.get(json_url).content)
random_num = random.randint(0, len(data['results']))
location_data = data['results'][random_num]

webpage_url = location_data['url']

html_page = requests.get(webpage_url).content
soup = BeautifulSoup(html_page, 'html.parser')
for div in soup.find_all('div', {'class': 'camera'}):
    image_url = 'https://trafficcams.vancouver.ca/' + div.find('img').get('src')
    im = Image.open(requests.get(image_url, stream=True).raw)
    w, h = im.size
    area = (0, .20*h, w, h)
    crop_im = im.crop(area)
    crop_im.show()

print('HOW TO PLAY:\n1. Open the map of Vancouver\n2. Try to guess the street number by looking at the images\n3. Press anything in console to display an answer\n4. Judge your performance yourself')

input()

print('Street name: ' + location_data['name'])