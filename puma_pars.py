import requests
from bs4 import BeautifulSoup

url = 'https://ua.puma.com/uk/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


item_info = soup.find_all('div', class_="page-wrapper")
for item in item_info:
    print(item.text)


item_images = soup.find_all('img')
print(item_images)
for img in item_images:
    img_url = img.get('src')
    if img_url:
        print(img_url)
    else:
        print("Картинка не знайдена")



item_message = soup.find_all('div', class_="cookie-status-message")
for item in item_message:
    print(item.text)


item_body = soup.find_all('div', class_="page-pressed")
for item in item_body:
    print(item.text)
