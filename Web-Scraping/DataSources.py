from bs4 import BeautifulSoup
import requests
#dataframe
import pandas as pd
#run every 15 secs
import time
#check for the overwrite
import os


def getFinancialInformation(symbol):
    url = "https://finance.yahoo.com/quote/"+symbol+"?p="+symbol

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
    return names, values


def getCompanyList():
        
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

    response = requests.get(url)
    r = response.text

    soup = BeautifulSoup(r, features="html.parser")

    #minden 2. contentre ad egy sort 
    tsymbol = []
    tbody = soup.find_all("tbody")

    #ha kisebb mint 2, vagy nem osztható 2-vel (azaz páratlan), akkor menjen tovább és azokat ne nézze 
    for i in range(len(tbody[0].contents)):
        if i < 2:
            continue
        if i % 2 != 0:
            continue
        else:
            symbol = tbody[0].contents[i].contents[1].text #this is where the symbol text is
            tsymbol.append(symbol.strip('\n'))
            if len(tsymbol) == 503:
                break
    return tsymbol

#----------- run every 15 secs -----------#
# check current time -> extract and save data -> wait for the given interval -> start again
# elmenti a kezdeti időt egy változóba
# starttime = time.time()
# megnézi, a kezdet óta mennyi idő telt el
# elteltido = time.time() - starttime
# vár 1 másodpercet
# time.sleep(1)

while True: 
    start = time.time()
    data = {
        "symbol":[],
        "metric":[],
        "value":[]
    }               

    tsymbol = getCompanyList()
    for symbol in tsymbol:
        names = getFinancialInformation(symbol)

    for i in range(len(names)):
        data["symbol"].append(symbol)
        data["metric"].append(names[i])
    # data["value"].append(values[i])

    #  getFinancialInformation(symbol)

        #print(len(tsymbol)) #milyen hosszú
        #print(tsymbol[0]) #első entry
        #print(tsymbol[-1]) #utolsó entry 

    #dataframe 
    df = pd.DataFrame(data)
    # --------------- CHECKING IF FILE EXIST, DEFINING PATH WITH OS ----------------- 
    savepath = "finaldata.csv"
    if os.path.isfile(savepath):
        #dont overwrite
        df.to_csv(savepath, mode="a", header="False", columns=["symbol","metrics","value"])
    else: 
        #create
        df.to_csv(savepath, columns=["symbol","metrics","value"]) #we can also define the colums and rows we wanna save in to be more consistent 

    timeDiff = (time.time() - start)
    #azért kell az if, mert amíg fut a program az is lehet több 15s nél -> ilyenkor a következő iterációval folytatja 
    if 15-timeDiff > 0:
        time.sleep(15-timeDiff)