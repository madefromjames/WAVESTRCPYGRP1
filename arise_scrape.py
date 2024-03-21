import requests
from bs4 import BeautifulSoup

base_url = 'https://www.arise.tv/category/entertainment/'
n = int(input("How many pages do you want to scrape? Pls increment the number of pages you want to scrape by +1\ne.g if you want to scarape 10 pages, input 11\n>>"))
v = range(n)
for numb in v:
    url = f"{base_url}page/{numb}"
    re = requests.get(base_url)
    pg_content = BeautifulSoup(re.text, 'html.parser')

    with open('arise.txt', 'wt') as file:
        for data in pg_content.find_all('article'):
            date = data.find('span', {'class': 'date'}).text.strip()
            title = data.find('h3').text.strip()
            img = data.find('img')
            if img:
                image = img.get('src')
            li = data.find('a')
            if li:
                link = li.get('href')
                # m = requests.get(link)
                # s = BeautifulSoup(m.text, 'html.parser')
                # for i in s.find_all('div', {'class': 'panel py-1 px-2 py-md-2 px-md-4'}):
                #     body = i.find('p').text.strip()
                #     if body:
                #         print(body)
                #     else:
                #         print('Body not found')
            file.write(f"Date: {date}\n")
            file.write(f"Headline: {title}\n")
            # file.write(f"Body: {body}\n")
            file.write(f"Image: {image}\n")
            file.write(f"URL: {link}\n")
            file.write('\n')

