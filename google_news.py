from newsplease import NewsPlease
import requests
from urllib.error import HTTPError
from socket import error as socket_error
import sys
file = sys.argv[1]


a_file = open(file, 'r')
file_contents = a_file.read()
links = file_contents.splitlines()

print(len(links))
urls = []
for link in links:
  urls.append("https://news.google.com" + link[1:-2])

articles = []

with open("./articles.txt", "a") as f:
  for i in range(0, len(urls)):
    r = requests.get(urls[i])
    print(str(i), " out of ", str(len(urls)), " done redirecting")
    try: 
      article = NewsPlease.from_url(r.url, timeout = 20)
      print(str(i), " out of ", str(len(urls)), " scraped")
      #articles.append((article.title, r, article.maintext))

      if article.maintext is not None or article.title is not None:
        f.write(str(article.title))
        f.write("|")
        f.write(r.url)
        f.write("|")
        f.write(str(article.maintext).replace('\n', ' '))
        f.write('\n')
    except HTTPError or TimeoutError or requests.exceptions.ConnectionError or socket_error:
      print(r.url + " failed")

    




'''with open("./articles.txt", "a") as f:
  for article in articles:
    f.write(article[0])
    f.write("|")
    f.write(r.url)
    f.write("|")
    f.write(article[2])
    f.write('\n')'''
