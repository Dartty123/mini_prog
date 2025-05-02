html_doc = """
<html>
  <head>
    <title>Мій перший сайт</title>
  </head>
  <body>
    <h1>Привіт, світ!</h1>
    <h1>Привіт, планета Земля!</h1>
    <p class="intro">Це перший абзац.</p>
    <p class="content">А це другий абзац.</p>
    <a href="https://example.com">Відвідати приклад</a>
    <ul>
      <li>Пункт 1</li>
      <li>Пункт 2</li>
      <li>Пункт 3</li>
    </ul>
  </body>
</html>
"""

import requests
from bs4 import BeautifulSoup



soup = BeautifulSoup(html_doc, 'html.parser')

if __name__ == '__main__':
    print(soup.title)
    print(soup.h1)
    print(soup.title.text)
    print(soup.h1.text)

    print(soup.p)
    print(soup.find('p'))

    all_paragraphs = soup.find_all('p')
    print(all_paragraphs)
    for p in all_paragraphs:
        print(p.text)

    intro_path = soup.find('p', class_="intro")
    print(intro_path)

    content_path = soup.find('p', class_="content")
    print(content_path)

    link = soup.find('a')
    print(link)
    print(link.text)
    print(link['href'])

    items = soup.find_all('li')
    for item in items:
        print(item.text)