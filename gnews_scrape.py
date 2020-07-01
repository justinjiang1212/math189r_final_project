from bs4 import BeautifulSoup
import urllib
import re
import time

linklist = []

while True:
    html_page = urllib.request.urlopen("https://news.google.com/topics/CAAqBwgKMOfAkAsw0bukAw?hl=en-US&gl=US&ceid=US%3Aen")
    soup = BeautifulSoup(html_page, 'lxml')
    links = soup.findAll('a', {'class': ['VDXfz']})

    for link in links:
        if link['href'] not in linklist:
            linklist.append(link['href'])

    print(len(linklist))
    time.sleep(20)
