from selenium import webdriver
import time 

driver = webdriver.Chrome('C:\\Users\\ADMIN\\Desktop\\python\\chromedriver')

url = 'https://www.brake.co.uk/search?q=beer:relevance&page=2'
driver.get(url)

'''
#method 1: javascript

time.sleep(3)
#driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
previous_height =  driver.execute_script('return document.body.scrollHeight);')

while True: 
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(3)
    new_height = driver.execute_script('return document.body.scrollHeight);')
    if new_height == previous_height:
        break
    previous_height = new_height
#addig teker, amíg az eredeti magasságot el nem éri az oldal, tehát a legaljáig elvileg 

'''

#method 2: selenium keys 
from selenium.webdriver.common.keys import Keys

time.sleep(3)

element = driver.find_element_by_tag('body')

while True:
    element.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)