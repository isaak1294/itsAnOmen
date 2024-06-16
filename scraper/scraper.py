import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the page we want to scrape
matchesUrl = 'https://vlr.gg/matches/results'

# Send a GET request to the URL
response = requests.get(matchesUrl)

soup = BeautifulSoup(response.text, 'lxml')
for link in soup.find_all('a'):
    print(link.get('href'))

#print(soup.prettify())