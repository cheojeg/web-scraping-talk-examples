import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = "https://micm.gob.do/precios-de-combustibles"

response = requests.request("GET", url)
soup = BeautifulSoup(response.text, 'html.parser')
fuel_list = soup.find_all('tbody')[0].find_all('tr')

for fuel_row in fuel_list:
    fuel = {
        'type': '',
        'price': '',
    }
    fuel_data = fuel_row.find_all('td')
    fuel['type'] = fuel_data[0].text
    fuel['price'] = fuel_data[1].text
    pprint(fuel)
