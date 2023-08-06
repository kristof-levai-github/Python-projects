from bs4 import BeautifulSoup
import requests

#extract the symbol of the s&p 500 wiki page 
#ezzel a technikával a többit is le lehetne szedni, majd mindegyik egy structba, azok meg egy dictbe és már meg is lenne a dataframe

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

response = requests.get(url)
r = response.text

soup = BeautifulSoup(r, features="html.parser")

'''
header = []
frow = []

#getting the first row 
for i in range(8):
    trs = soup.find_all("th")
    header.append(trs[i].text)

#getting the second row: 
for i in range(8):
    td = soup.find_all("td")
    frow.append(td[i].text)

data = {
    'header':header,
    'frow':frow
}
print(data)
'''
#minden 2. contentre ad egy sort 
tsymbol = []
endsymbol = 'ZTS'
tbody = soup.find_all("tbody")
print(tbody[0].contents[2].contents[1].text)

#ha kisebb mint 2, vagy nem osztható 2-vel (azaz páratlan), akkor menjen tovább és azokat ne nézze 
for i in range(len(tbody[0].contents)):
    if i < 2:
        continue
    if i % 2 != 0:
        continue
    else:
        symbol = tbody[0].contents[i].contents[1].text #this is where the symbol text is
        tsymbol.append(symbol.strip('\n'))
        if symbol == endsymbol:
            break

print(tsymbol)
print(len(tsymbol))

#print(len(tsymbol)) #milyen hosszú
#print(tsymbol[0]) #első entry
#print(tsymbol[-1]) #utolsó entry 