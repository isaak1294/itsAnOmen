import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the page we want to scrape
matchesUrl = 'https://vlr.gg/matches/results'

# Send a GET request to the URL
response = requests.get(matchesUrl)

soup = BeautifulSoup(response.text, 'html.parser')
matchLinks = soup.find_all('a')

print(matchLinks)
#print(soup.prettify())