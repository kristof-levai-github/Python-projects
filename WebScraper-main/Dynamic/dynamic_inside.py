import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup
import sys

productlinks = []
products = []

baseurl = 'https://webscraper.io'

# Set the default encoding to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

for x in range(1, 2):
    url = f'https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={x}'

    # Getting the driver path
    driver = webdriver.Chrome(executable_path="C:\\Users\\ADMIN\\Desktop\\python\\web\\chromedriver")

    driver.get(url)

    products_on_page = driver.find_elements(By.CLASS_NAME, "col-sm-4.col-lg-4.col-md-4")

    for item in products_on_page:
        link = item.find_element(By.TAG_NAME, 'a')
        productlinks.append(link.get_attribute('href'))

    driver.close()

    # Print all the links
    for link in productlinks:
        driver = webdriver.Chrome(executable_path="C:\\Users\\ADMIN\\Desktop\\python\\web\\chromedriver")
        driver.get(link)
        description = driver.find_element(By.CLASS_NAME, 'description').text
        price = driver.find_element(By.CLASS_NAME, 'pull-right.price').text
        image = driver.find_element(By.CLASS_NAME, 'img-responsive').get_attribute('src')

        product_items = {
            'description': description,
            'price': price,
            'image': image
        }
        products.append(product_items)

df = pd.DataFrame(products)
print(df)


#sima baseurl concat módszer: 
'''
The modified code returns the full URL instead of just the /test-sites/e-commerce/static/product/516 part because of the way the href attribute is being extracted.

When you use link.get_attribute('href'), it retrieves the entire URL specified in the href attribute of the <a> tag. In this case, the href attribute of the <a> tag contains the complete URL, including the base URL (https://webscraper.io) and the path (/test-sites/e-commerce/static/product/516).

If you want to extract only the /test-sites/e-commerce/static/product/516 part from the URL, you can modify the code as follows:

# ...
for item in products:
    link = item.find_element(By.TAG_NAME, 'a')
    href = link.get_attribute('href')
    product_path = href.replace(baseurl, '')
    productlinks.append(product_path)
# ...

In this updated code, the replace function is used to replace the baseurl part of the URL with an empty string. This effectively removes the base URL and retains only the path (/test-sites/e-commerce/static/product/516) portion. The modified path is then appended to the productlinks list.

Now, when you run this code, it will store only the /test-sites/e-commerce/static/product/516 part in the productlinks list, rather than the complete URL.

'''