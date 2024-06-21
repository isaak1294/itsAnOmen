import requests
from bs4 import BeautifulSoup
import pandas as pd

links = pd.read_csv('links.csv')

##for i in links['Links']:
##    response = requests.get(i)
##    soup = BeautifulSoup(response.text, 'lxml')
##    print(soup.prettify())

page = str(links.loc[9, 'Links'])
response = requests.get(page)
soup = BeautifulSoup(response.text, 'lxml')
print(soup.prettify())