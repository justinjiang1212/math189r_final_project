from bs4 import BeautifulSoup
import urllib
import re
import time

linklist = []

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

        print(len(linklist))
        f.close()

    time.sleep(60)
