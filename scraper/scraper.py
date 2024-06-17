import requests
from bs4 import BeautifulSoup
import pandas as pd


for i in range(1, 511):
    matchesUrl = 'https://vlr.gg/matches/results?page=' + str(i)
    response = requests.get(matchesUrl)
    soup = BeautifulSoup(response.text, 'lxml')
    for link in soup.find_all('a'):
        #print(link.get('href'))
        linkstr = str(link.get('href'))
        if 'champions' in linkstr:
            print('https://vlr.gg' + link.get('href'))

    print(i)

#print(soup.prettify())