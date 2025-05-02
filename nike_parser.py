import requests
from bs4 import BeautifulSoup

url = 'https://www.fortnite.com/?lang=en-US'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


products_info = soup.find_all('div', class_=',models-catalog__product')
for product in products_info:
    print(product.text)

products_price = soup.find_all('div', class_=',models-nike__price')
for price in products_price:
    print(price.text)

product_old_price = soup.find_all('div', class_=',models-nike__old-price')
for old_price in product_old_price:   
    print(old_price.text)

products_image_url = soup.find_all('div', class_='product-nike__image')
print(products_image_url)
for product in products_image_url:
    image_tag = product.find('img')
    if image_tag:
        image_url = image_tag.get('data-src')
        if image_url:
            print(image_url)
    else:
        print("Картинка не знайдена")
