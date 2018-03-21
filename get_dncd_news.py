import time
from selenium import webdriver
# The URL we want to browse to
url = "http://www.dncd.gob.do/category/noticias/"
# Using Selenium's webdriver to open the page
driver = webdriver.Firefox(executable_path=r'/home/jgarcia/Documentos/pytest/dnc_download_news/geckodriver')
# driver = webdriver.PhantomJS(executable_path=r'/home/jgarcia/Documentos/pytest/dnc_download_news/phantomjs')
driver.get(url)
# time.sleep(5)
print "Aqui"
# articles = driver.find_elements_by_xpath('//*[@id="content"]')
articles = driver.find_elements_by_class_name('status-publish')
for a in articles:
    title_element = a.find_element_by_tag_name('h2')
    title = title_element.text.encode('utf8')
    url = title_element.find_element_by_tag_name('a').get_attribute('href')
    lead = a.find_element_by_tag_name('p').text.encode('utf8')
    img_element = a.find_element_by_tag_name('img').get_attribute('src')
    # img_element_p1 = img_element[0]
    # img_element_p2 = img_element[-1].split('.')[-1]
    # img_element = img_element_p1+img_element_p2
    # import ipdb; ipdb.set_trace()
    print title
    print url
    print lead
    print img_element
    print "------------------------------------------------------------"

page_links = driver.find_element_by_css_selector('div.page-links')
print "Busncado los links del resto de las paginas"
print page_links
# import ipdb; ipdb.set_trace()
# print page_links[-1].text.encode('utf8')
last_page = int(page_links.find_elements_by_tag_name('a')[-1].text.encode('utf8')) + 1
for i in range(last_page):
    if i > 1:
        url = "http://www.dncd.gob.do/category/noticias/page/" + str(i) + "/"
        driver.get(url)
        articles = driver.find_elements_by_class_name('status-publish')
        for a in articles:
            title_element = a.find_element_by_tag_name('h2')
            title = title_element.text.encode('utf8')
            url = title_element.find_element_by_tag_name('a').get_attribute('href')
            lead = a.find_element_by_tag_name('p').text.encode('utf8')
            img_element = a.find_element_by_tag_name('img').get_attribute('src')
            # import ipdb; ipdb.set_trace()
            print title
            print url
            print lead
            print img_element
            print "------------------------------------------------------------"
# for p in page_links:
#     print p.text.encode('utf8')
driver.close()
