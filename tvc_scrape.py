import requests
from bs4 import BeautifulSoup

url = 'https://www.tvcnews.tv/politics/'
response = requests.get(url)
# print(response)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())

with open('tvcpol.txt', 'wt') as file:
    for news in soup.find_all('article'):
        title = news.find('h3').text.strip()
        if title:
            print(title)
        else:
            print('Headline not found')
        # img = news.find('img').source.strip()
        img = news.find('img')
        if img:
            image = img.get('src')
            print(f"https:{image}")
        else:
            print('Image not found')
        li = news.find('a')
        if li:
            link = li.get('href')
            print(f"URL: {link}")
        else:
            print('link not found')
        file.write(f"Headline: {title}\n")
        file.write(f"Image: {image}\n")
        file.write(f"URL: {link}\n")
        file.write('\n')
