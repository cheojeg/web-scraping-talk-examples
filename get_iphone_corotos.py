import time
from pprint import pprint
from selenium import webdriver

# The URL we want to browse to
url = 'https://www.corotos.com.do/'
# Using Selenium's webdriver to open the page
# Firefox
driver = webdriver.Firefox(executable_path=r'./geckodriver')
# PhantomJS
# driver = webdriver.PhantomJS(executable_path=r'./phantomjs')
driver.get(url)
# time.sleep(5)

field = driver.find_element_by_name('q')
field.send_keys('iphone 6')
driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/form/button').click()

# Just get item price
# price_list = driver.find_elements_by_class_name('price')
# for price in price_list:
#     print price.text


item_list = driver.find_elements_by_class_name('item')
for i in item_list:
    article = {
        'img': '',
        'price': '',
        'title': '',
        'url': '',
        'date': ''
    }
    img = i.find_elements_by_tag_name('img')
    if img:
        article['img'] = img[0].get_attribute('src')
    price = i.find_elements_by_class_name('price')
    if price:
        article['price'] = price[0].text
        # article['price'] = price[0].text.split(' ')[1]
    title = i.find_elements_by_tag_name('h2')
    if title:
        article['title'] = title[0].text
    date = i.find_elements_by_class_name('time')
    if date:
        article['date'] = title[0].text.strip()
    url = i.find_elements_by_class_name('history')
    if url:
        article['url'] = url[0].get_attribute('href')
    pprint(article)

driver.close()
