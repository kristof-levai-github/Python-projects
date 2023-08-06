import requests

url = 'https://finance.yahoo.com/quote/BTC-USD?p=BTC-USD'

#getting the page and status code
response = requests.get(url)
print(response.status_code)
print(response.status_code==200)

prop = 'previous close'
t = response.text

#getting the webpage content
#print(response.text)


#---------------------------------------------------------------#
#the index of the string in the requested page
ind = t.index('Previous Close')
print(ind)

#reduced text prints out the next 200 characters after an index
# [:3] -> first 3 element 
#redText = t[ind:ind+200].split("</span>")
#print(redText[:3])


redText = t[ind:].split("</span>")[1]
val = redText.split(">")[-1]
print(val)


