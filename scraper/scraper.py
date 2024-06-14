import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the page we want to scrape
url = 'vlr.gg/matches/results'

# Send a GET request to the URL
response = requests.get(url)