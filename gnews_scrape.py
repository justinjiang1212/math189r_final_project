from bs4 import BeautifulSoup
import urllib
import re
import time
from newspaper import Article
import newspaper as newspaper
import requests
from urllib.error import HTTPError
from socket import error as socket_error
from datetime import datetime

linklist = []

def scrape(link):
    try: 
        url = "https://news.google.com" + str(link[1:-2])
        r = requests.get(url)
        article = Article(r.url, language = "en")
        article.download()
        article.parse()
        with open("./articles.txt", "a") as f:

            if article.text is not None or article.title is not None:
                f.write(str(article.title))
                f.write("|")

                f.write(r.url)
                f.write("|")

                f.write(str(datetime.now()))
                f.write("|")

                f.write(str(article.text).replace('\n', ' '))
                f.write('\n')

                print(str(article.title) + " is done")
    except:
        print(r.url + " failed")



while True:
    with open("./links.txt", "a") as f:
        html_page = urllib.request.urlopen("https://news.google.com/topics/CAAqBwgKMOfAkAsw0bukAw?hl=en-US&gl=US&ceid=US%3Aen")
        soup = BeautifulSoup(html_page, 'lxml')
        links = soup.findAll('a', {'class': ['VDXfz']})

        for link in links:
            if link['href'] not in linklist:
                linklist.append(link['href'])
                f.write(link['href'])
                f.write('\n')
                scrape(link['href'])

        print(len(linklist))
        f.close()

    time.sleep(60)
    print(str(datetime.now))
