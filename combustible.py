import time
from selenium import webdriver
# The URL we want to browse to
import ipdb; ipdb.set_trace()
url = "https://micm.gob.do/precios-de-combustibles"
# Using Selenium's webdriver to open the page
driver = webdriver.Firefox(executable_path=r'/home/jgarcia/Documentos/pytest/dnc_download_news/geckodriver')
# driver = webdriver.PhantomJS(executable_path=r'/home/jgarcia/Documentos/pytest/dnc_download_news/phantomjs')
driver.get(url)
# time.sleep(5)
print "Aqui"
table_rows = driver.find_elements_by_tag_name("tr")
# field.send_keys("iphone 6")
# driver.find_element_by_xpath("/html/body/div[1]/section[1]/div/form/button").click()
# price_list = driver.find_elements_by_class_name("price")
for price in table_rows:
    print price.text
driver.close()
