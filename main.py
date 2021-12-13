import requests
import bs4

HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;'
                     'q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,bg;q=0.6',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'Cookie': 'neuro-habr=d786d9bf-9eb6-424f-8f15-15de32d2d328;_ga=GA1.2.479450803.1618310165; hl=ru; fl=ru;'
                     'feature_streaming_comments=true; visited_articles=301436:519788:254773; '
                     '_gid=GA1.2.309514118.1639388939; habr_web_home=ARTICLES_LIST_ALL',
           'DNT': '1',
           'Host': 'habr.com',
           'If-None-Match': 'W/"38b8e-XiWUj/7koJV5qir7gGDTIhBiG7U"',
           'Referer': 'https://github.com/netology-code/py-homeworks-advanced/tree/master/6.Web-scrapping',
           'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
           'sec-ch-ua-mobile': '?0',
           'sec-ch-ua-platform': '"Windows"',
           'Sec-Fetch-Dest': 'document',
           'Sec-Fetch-Mode': 'navigate',
           'Sec-Fetch-Site': 'same-origin',
           'Sec-Fetch-User': '?1',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/96.0.4664.93 Safari/537.36'}

KEYWORDS = {'Алгоритмы', 'Искусственный интеллект', 'Гаджеты', 'Big Data'}

response = requests.get('https://habr.com/ru/all/', headers=HEADERS)
response.raise_for_status()
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')
article_list = soup.find_all('article')

if __name__ == '__main__':
    for article in article_list:
        art_link = article.find('a', class_="tm-article-snippet__title-link")
        title = art_link.find('span').text
        snippets = article.find_all('a', class_="tm-article-snippet__hubs-item-link")
        snippet = set(snippet.find('span').text for snippet in snippets)
        date = article.find('time')['title']
        if KEYWORDS & snippet:
            href = art_link['href']
            url = 'https://habr.com' + href
            print(date, '||', title, '||', url)
            print('----')