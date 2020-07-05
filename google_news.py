from newsplease import NewsPlease
import requests
from urllib.error import HTTPError

f = open("links.txt", 'r')
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


for i in range(100, 200):
  r = requests.get(urls[i])
  print(str(i), " out of ", str(len(urls)), " done redirecting")
  try: 
    article = NewsPlease.from_url(r.url)
    articles.append((article.title, r, article.maintext))
  except HTTPError:
    print(r.url + " failed")

  print(str(i), " out of ", str(len(urls)), " scraped")



#for url in urls:
#  article = NewsPlease.from_url(url)
#  articles.append((article.title, url, article.maintext))
#  print(str(counter), " out of ", str(len(urls)), " done redirecting")
#  counter += 1

with open("./articles.txt", "a") as f:
  for article in articles:
    f.write(article[0])
    f.write("|")
    f.write(article[1])
    f.write("|")
    f.write(article[2])
    f.write('\n')
