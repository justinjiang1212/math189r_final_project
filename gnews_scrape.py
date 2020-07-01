from bs4 import BeautifulSoup
import urllib
import re

html_page = urllib.request.urlopen("https://news.google.com/topics/CAAqBwgKMOfAkAsw0bukAw?hl=en-US&gl=US&ceid=US%3Aen")
soup = BeautifulSoup(html_page, 'lxml')
links = soup.findAll('a', {'class': ['VDXfz']})

'''print(len(links))

for link in links:
    print(link['href'])'''
