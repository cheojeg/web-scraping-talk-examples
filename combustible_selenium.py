from selenium import webdriver
from pprint import pprint

# The URL we want to browse to
url = "https://micm.gob.do/precios-de-combustibles"
# Using Selenium's webdriver to open the page
# driver = webdriver.Firefox(executable_path=r'./geckodriver')
driver = webdriver.PhantomJS(executable_path=r'./phantomjs')
driver.get(url)
table_body = driver.find_elements_by_tag_name("tbody")
table_rows = table_body[0].find_elements_by_tag_name("tr")

for price in table_rows:
    fuel = {
        'type': '',
        'price': '',
    }
    fuel_data = price.find_elements_by_tag_name('td')
    fuel['type'] = fuel_data[0].text
    fuel['price'] = fuel_data[1].text
    pprint(fuel)

driver.close()
