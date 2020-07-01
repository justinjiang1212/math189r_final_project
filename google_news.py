from newsplease import NewsPlease
import requests


url = "https://news.google.com/articles/CAIiEJEOihpTd7_0e6BTqCjyKowqGQgEKhAIACoHCAowh___CjDHqosDMOj-4gU?hl=en-US&gl=US&ceid=US%3Aen"

r = requests.get(url) 

article = NewsPlease.from_url(r.url)

print(article.maintext)