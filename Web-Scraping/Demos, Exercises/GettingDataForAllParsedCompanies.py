import requests


wikiURL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

wikiResponse = requests.get(wikiURL)

data = {"Company":[]}

wikiFirstParse = wikiResponse.text.split("0001555280")[0]
wikiDataTable = wikiFirstParse.split("Component Stocks")[3]
hyperLinkSplitWiki = wikiDataTable.split("href=")
start = 4
for position in range(len(hyperLinkSplitWiki)):
    if position > start:
        if "nyse" in hyperLinkSplitWiki[position]:
            if "quote" in hyperLinkSplitWiki[position]:
                tempData = hyperLinkSplitWiki[position].split('">')[1].split("</")[0]
                data["Company"].append(tempData)
        elif "nasdaq" in hyperLinkSplitWiki[position]:
            if "symbol" in hyperLinkSplitWiki[position]:
                tempData = hyperLinkSplitWiki[position].split('">')[1].split("</")[0]
                data["Company"].append(tempData)

#5->9->13
Indicators = {"Previous Close":[],
            "Open":[],
            "Bid":[],
            "Ask":[],
            "Day&#x27;s Range":[],
            "52 Week Range":[],
            "Volume":[],
            "Avg. Volume":[],
            "Market Cap":[],
            "Beta":[],
            "PE Ratio (TTM)":[],
            "EPS (TTM)":[],
            "Earnings Date":[],
            "Dividend &amp; Yield":[],
            "Ex-Dividend Date":[],
            "1y Target Est":[]}



url = "http://finance.yahoo.com/quote/AAPL?p=AAPL"
#print(htmlText)
counter = 0 
for tickerSymbol in data["Company"]:
    url = ("http://finance.yahoo.com/quote/"+tickerSymbol
       +"?p="+tickerSymbol)
    response = requests.get(url)
    htmlText = response.text
    for indicator in Indicators:
        splitList = htmlText.split(indicator)
        afterFirstSplit = splitList[1].split("\">")[1]
        afterSecondSplit = afterFirstSplit.split("</td>")
        dataValue = afterSecondSplit[0]
        Indicators[indicator].append(dataValue)

print(Indicators)



