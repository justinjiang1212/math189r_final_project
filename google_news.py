from newsplease import NewsPlease
import requests

f = open("links.txt", 'r')
links = []
for x in f:
  links.append(x)

urls = []
for link in links:
  urls.append("https://news.google.com" + link[1:-2])


for i in range(0, len(urls)):
  r = requests.get(urls[i])
  print(str(i), " out of ", str(len(urls)), " done redirecting")
  urls[i] = r.url

articles = []
counter = 0

for url in urls:
  article = NewsPlease.from_url(url)
  articles.append((article.title, article.maintext))
  print(str(counter), " out of ", str(len(urls)), " done redirecting")
  counter += 1

with open("./articles.txt", "a") as f:
  for article in articles:
    f.write(article[0])
    f.write("|")
    f.write(article[1])
    f.write('\n')
