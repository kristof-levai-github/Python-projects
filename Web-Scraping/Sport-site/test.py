# imports

from time import sleep
from bs4 import BeautifulSoup as bs
import csv
import requests


def fetch(url):

    global s
    stopper = 0

    while True:
        try:
            response = s.get(url, timeout=120)
            if response.status_code == 200:
                print("Everything is alright\n", end='')
                break
            else:
                print(response.status_code)
                print('Reconnecting...')
                sleep(5)
                if stopper == 10:
                    print('Timed out')
                    break
                else:
                    stopper += 1
        except:
            print(traceback.format_exc())
            sleep(5)
            print('reconnecting', end='')
            if stopper == 10:
                print("Timed out")
                break
            else:
                stopper += 1

    return response


def parse(html):
    content = bs(html, 'html.parser')

    name = [names.text.strip() for names in content.findAll('h3', {'itemprop': 'name'})]
    description = [descriptions.text.strip() for descriptions in content.findAll('div', {'class': 'description'})]
    price = [prices.text.strip() for prices in content.findAll('div', {'class': 'price'})]
   # pictures = [pictures.text.strip() for pictures in content.findAll('div', {'class': 'photo'})]


    for index in range(0, len(name)):
        results.append({
            'name': name[index],
            'description': description[index],
            'price': price[index],
          #  'picture': pictures[index],
        })


def to_csv():


    print("Start writing csv file")
    with open("sportsport.csv", "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames = results[0].keys())
        header = ['name','description','price']
        writer.writeheader()

        for row in results:
            writer.writerow(row)

        print("All datas are saved to sportsport.csv")


def run():

    index = 0

    for i in range(0, 2):
        url = "https://sportsport.hu/arak?page="
        url += str(index)

        response = fetch(url)
        parse(response.text)

    to_csv()

if __name__ == '__main__':

    s = requests.session()
    results = []
    run()


