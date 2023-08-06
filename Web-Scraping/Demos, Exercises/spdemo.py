from bs4 import BeautifulSoup
import requests

url = 'https://finance.yahoo.com/quote/BTC-USD?p=BTC-USD'

response = requests.get(url)
r = response.text

#initialize bs4
soup = BeautifulSoup(r, features="html.parser")

# [0] is the first element
#összes tr tag megkeresése
trs = soup.find_all("tr")

#kiírja az első element textjét
#print(trs[0].text)

#kiírja az első tr első td textjét
print(trs[0].td.text)

#kiírja az első tr első td első span textjét
print(trs[0].td.span.text)

#kiírja az első tr-ben lévő componenseket
print(trs[0].contents)

#kiírja a kontenteknek a 2. elemét, ami már maga az ár -> ezt kerestük 
#childba nem lehet []-t rakni, viszont kontentbe és egyéb 'functionokbe' engedi
print(trs[0].contents[1].text)

#filter for classnames
try:
    print("td", class_="classname").text
except:
    print = 'nope'


'''
ezeken belül is lehet többször keresni
ez , a trs-en belül keresi a td-t egy data-test nevű attribútumát, aminek az értéke attribute

print(trs[0].find("td", attrs="data-test: attribute").text)

'''