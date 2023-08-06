from time import sleep
from bs4 import BeautifulSoup as bs
import csv
import requests


def scrape_page(url):
    """ Scrape the give url and return the bs4 ResultSet """
    page = requests.get(url)
    soup = bs(page.content, "html.parser")


def extract_rows():
    """ Extract rows """
    rows = []
    for row in rows:
        name = row.findAll('a', {'class': 'track'}).text.strip()
        description = row.findAll('div', {'class': 'description'}).text.strip()
        price = row.findAll('div', {'class': 'price'}).text.strip()
        rows.append([name, description, price])
    return rows


big_table = []

for x in range(0, 99):
    index = scrape_page("https://sportsport.hu/arak?page=" + str(x) + ".html")
    for row in extract_rows(index):
        big_table.append(row)

print(big_table)

