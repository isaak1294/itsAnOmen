import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the page we want to scrape
url = 'https://vlr.gg/matches/results'

# Send a GET request to the URL
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

print(soup.prettify())