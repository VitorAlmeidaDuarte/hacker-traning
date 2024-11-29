import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import math

url = 'https://www.kabum.com.br/promocao/HARDWAREKABUM'

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}

website = requests.get(url, headers=headers)
soup = BeautifulSoup(website.content, 'html.parser')

amount_items = soup.find('div', id='listingCount').get_text()

print(amount_items)