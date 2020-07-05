from newsplease import NewsPlease
import requests
from urllib.error import HTTPError
import sys
file = sys.argv[1]

f = open(file, 'r')
links = []
for x in f:
  links.append(x)

urls = []
for link in links:
  urls.append("https://news.google.com" + link[1:-2])

articles = []

for i in range(0, 100):
  r = requests.get(urls[i])
  print(str(i), " out of ", str(len(urls)), " done redirecting")
  try: 
    article = NewsPlease.from_url(r.url)
    articles.append((article.title, r, article.maintext))
  except HTTPError:
    print(r.url + " failed")

  print(str(i), " out of ", str(len(urls)), " scraped")





with open("./articles.txt", "a") as f:
  for article in articles:
    f.write(article[0])
    f.write("|")
    f.write(article[1])
    f.write("|")
    f.write(article[2])
    f.write('\n')
