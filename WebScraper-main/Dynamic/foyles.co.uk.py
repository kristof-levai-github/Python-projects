import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup
import sys

# Set the default encoding to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

books_list = []

for x in range(1,4):
    url = f'https://www.foyles.co.uk/search?filters[component_id][]=1058490&page={x}'

    # Getting the driver path
    driver = webdriver.Chrome(executable_path="C:\\Users\\ADMIN\\Desktop\\python\\web\\chromedriver")

    # Getting the URL and the source page
    driver.get(url)


    #legkülső elem kell, amibe a kis elemek vannak 
    books = driver.find_elements(By.CLASS_NAME, "product-info")

    '''
    name : info-title
    author: class="info-contributors"
    type: class="info-published"
    price: class="price-sale"
    '''

    for book in books:
        name = book.find_element(By.CLASS_NAME, 'info-title').text
        author = book.find_element(By.CLASS_NAME, 'info-contributors').text
        tipus = book.find_element(By.CLASS_NAME, 'info-published').text
        price = book.find_element(By.CLASS_NAME, 'price-sale').text
        book_item = {
            'name': name,
            'author': author,
            'type': tipus,
            'price': price
        }
        books_list.append(book_item)

df = pd.DataFrame(books_list)
print(df)