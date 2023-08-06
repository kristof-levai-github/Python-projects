import requests
from bs4 import BeautifulSoup
import pandas as pd

#Imports the HTML into python
page = requests.get('https://www.carpages.ca/used-cars/search/?num_results=50&fueltype_id%5b0%5d=3&fueltype_id%5b1%5d=7&p=3')
soup = BeautifulSoup(page.text, 'lxml')
soup

#Creating our dataframe
df = pd.DataFrame({'Link':[''], 'Name':[''], 'Price':[''], 'Color':['']})

counter = 0
#This loop goes through the first 10 pages and grabs all the details of each posting
while counter < 10:
    
    #gets the HTML of all the postings on the page
    postings = soup.find_all('div', class_ = 'media soft push-none rule')

    #grabs all the details for each posting and adds it as a row to the dataframe
    for post in postings:
        link = post.find('a', class_ = 'media__img media__img--thumb').get('href')
        link_full = 'https://www.carpages.ca' +link
        name = post.find('h4', class_ = 'hN').text.strip()
        price = post.find('strong', class_ = 'delta').text
        color = post.find_all('div', class_ = 'grey l-column l-column--small-6 l-column--medium-4')[1].text.strip()
        df = df.append({'Link':link_full, 'Name':name, 'Price':price, 'Color':color}, ignore_index = True)
    
    #grabs the url of the next page
    next_page = soup.find('a', class_ = 'nextprev').get('href')
    
    #Imports the next pages HTML into python
    page = requests.get(next_page)
    soup = BeautifulSoup(page.text, 'lxml')
    counter += 1

