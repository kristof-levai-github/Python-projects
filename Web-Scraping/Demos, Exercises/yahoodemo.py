from bs4 import BeautifulSoup
import requests

url = 'https://finance.yahoo.com/quote/BTC-USD?p=BTC-USD'

response = requests.get(url)
r = response.text

soup = BeautifulSoup(r, features="html.parser")

#getting the previos close price
trs = soup.find_all("tr")
print(trs[0].contents[1].text)


#MANUAL WAY with dict and struct
open = []
dayrange = []
startdate = []
algorithm = []
weekrange = []
marketcap = []
circsupply = []
maxsupply = []
volume = []
volume_twentyfour = []
volume_all_currency = []

#getting the open
open.append(trs[1].contents[1].text)
#getting the days range 
dayrange.append(trs[2].contents[1].text)
#getting the start date
startdate.append(trs[3].contents[1].text)
#getting the algorithm
algorithm.append(trs[4].contents[1].text)
#getting the 52th week range
weekrange.append(trs[5].contents[1].text)
#getting the market cap
marketcap.append(trs[6].contents[1].text)
#getting the circulation supply
circsupply.append(trs[7].contents[1].text)
#getting the max supply 
maxsupply.append(trs[8].contents[1].text)
#getting the volume 
volume.append(trs[9].contents[1].text)
#getting the volume (24hrs)
volume_twentyfour.append(trs[10].contents[1].text)
#getting the Volume (24hr) All Currencies
volume_all_currency.append(trs[11].contents[1].text)


data = {

    'open': open,
    'dayrange': dayrange,
    'startdate': startdate,
    'algorithm': algorithm,
    'weekrange': weekrange,
    'marketcap': marketcap,
    'circsupply': circsupply,
    'maxsupply': maxsupply,
    'volume': volume,
    'volume_twentyfour': volume_twentyfour,
    'volume_all_currency': volume_all_currency
}
print(data, "\n")

#ezt jobb ilyen JSON formás cuccba írni pl: 'name':name, 
#save names, values etc (to an array) [] -> make a dictionary from them {}


#sima manual pl: 

'''
volume_twentyfour = print(trs[10].contents[1].text)
#getting the Volume (24hr) All Currencies
volume_all_currency = print(trs[11].contents[1].text)
'''

'''
#sima loop
for i in range(1,11):
    print(trs[i].contents[1].text)
'''



'''
másik megoldás: 

url = 'https://finance.yahoo.com/quote/BTC-USD?p=BTC-USD'

response = requests.get(url)
r = response.text

soup = BeautifulSoup(r, features="html.parser")

finalName = 'Volume (24hr) All Currencies'
trs = soup.find_all("tr")

names = []
values = []
namval = {}

for i in range(len(trs)):
    for j in range(len(trs[i].contents)):
        if j == 0: #names
            try: 
                name = trs[i].contents[j].text
                names.append(name)
            except:
                continue
            if j == 1: #values
                try: 
                    value = trs[i].contents[j].text
                    values.append(value)
                except:
                    continue
    namval[name] = values
    if name == finalName:
        break

#print(names)
#print(values)
print(namval)

'''