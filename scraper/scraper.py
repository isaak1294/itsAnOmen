import requests
from bs4 import BeautifulSoup
import pandas as pd

j = 0
links = {}

for i in range(1, 511):
    matchesUrl = 'https://vlr.gg/matches/results?page=' + str(i)
    response = requests.get(matchesUrl)
    soup = BeautifulSoup(response.text, 'lxml')
    for link in soup.find_all('a'):
        #print(link.get('href'))
        linkstr = str(link.get('href'))
        if 'champions-tour' in linkstr:
            links[j] = 'https://vlr.gg' + link.get('href')
            j += 1

    print(i)

pd.DataFrame({'Links': links}).to_csv('links.csv')

#print(soup.prettify())
#changedemail