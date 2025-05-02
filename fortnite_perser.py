import requests
from bs4 import BeautifulSoup


url = 'https://www.fortnite.com/item-shop?lang=en-US'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

item_images = soup.find_all('img')
print(item_images)
for img in item_images:
    img_url = img.get('src')
    if img_url:
        print(img_url)
    else:
        print("Картинка не знайдена")


item_info = soup.find_all('div',class_="flex")
for item in item_info:
    print(item.text)


item_data_testied = soup.find_all('div')
for item in item_data_testied:
    print(item.text)


item_screen = soup.find_all('div',class_="fixed")
for item in item_screen:
    print(item.text)
