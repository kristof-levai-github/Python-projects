from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError
import re
import datetime
import random

#beimportálások
#setting -> project -> project interpreter -> install mod !!!!!
#semmi más gecit nem eszik meg a nyomorék win - ez kell pandába, soleniumba stb, de kell a pip install is

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser') #a html oldal át lett alakítva soup objecté

#másik jó parser : lxml -> kicsit jobb, de thrid party (főleg jobban formáz)

#felépítés: tipikus html -> html → <html><head>...</head><body>...</body></html>
#— head → <head><title>A Useful Page<title></head>
#— title → <title>A Useful Page</title>
#— body → <body><h1>An Int...</h1><div>Lorem ip...</div></body>
#— h1 → <h1>An Interesting Title</h1>
#— div → <div>Lorem Ipsum dolor...</div>

print(bs.h1) # vissza adja a legelső h1 tagot az oldalon
print(bs.body.h1)
print(bs.html.h1)

#fontos az exception handling, hogy automatikánál kezelje a hibát ->
#url lekérésnél 2 hiba lehet: nincs page | nincs szerver

#//nincs page (http)
try:
 html = urlopen('http://www.pythonscraping.com/pages/page1.html')
except HTTPError as e:
 print(e)
 # return null, break, or do some other "Plan B"
else:
    print()
 # program continues. Note: If you return or break in the
 # exception catch, you do not need to use the "else" statement


#nem érhető el az url : (szerver)
try:
 html = urlopen('https://pythonscrapingthisurldoesnotexist.com')
except HTTPError as e:
 print(e)
except URLError as e:
 print('The server could not be found!')
else:
 print('It Worked!')


#rossz / hibás / nem létező tagek szűrése -> ha nincs olyan, akkor none-t fog vissza dobni
#ha ezt viszont meghívnánk valahova, már hibát dobna
#kezelés :


#try:
# badContent = bs.nonExistingTag.anotherTag
#except AttributeError as e:
# print('Tag was not found')
#else:
 #if badContent == None:
 #print('Tag was not found')
 #else:
 #print(badContent)





 #tipp : when writing scrapers, it’s important to think about the overall pattern of your code
#in order to handle exceptions and make it readable at the same time. You’ll also likely
#want to heavily reuse code. Having generic functions such as getSiteHTML and
#getTitle (complete with thorough exception handling) makes it easy to quickly—
#and reliably—scrape the web.






#többet egymásba lehet ágyazni ->funckionalitás növelése -> egy funkción belül nem 1-1 hanem több dolgot is ellenőrzünk

#def getTitle(url):

# try:
 # html = urlopen(url)
 #except HTTPError as e:
 #return None
 #try:
 #bs = BeautifulSoup(html.read(), 'html.parser')
 #title = bs.body.h1
 #except AttributeError as e:
 #return None
 #return title
#title = getTitle('http://www.pythonscraping.com/pages/page1.html')
#if title == None:
 #print('Title could not be found')
 #else:
 #print(title)






#nem mindig a bonyolult kód a jó - legyen flexibilis, csak végső esetben statikus inkább

#mobil nézet néha sokkal egyszerűbb
#hidden info javascriptben
#néha url-ben is van infó



#In this section, we’ll discuss searching for tags by
#attributes, working with lists of tags, and navigating parse trees


#css classok és ID-k nagyon jók -> mivel egyediek, könnyű szűrni és pozicionálni őket

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')

nameList = bs.findAll('span', {'class':'green'})
for name in nameList:
 print(name.get_text()) #a .get_text elválasztja a szöveget és a tageket

#find_all('span', {'class:{'green','red'}})
#find_all(['h1','h2','h3','h4','h5','h6'])


#Ez megkereséni az összes prince szöveget az oldalon és megszámolná
#Van BS.FIND ÉS BS.FIND_ALL (all-nak van limitje)
#nameList = bs.find_all(text='the prince')
#print(len(nameList))

#title = bs.find(id='title')
#title = bs.find_all(id='title', class_='text')

#Mindent amit meg lehet oldani így keywordos kereséssel, meg lehet oldani később más módszerekkel is pl:
#regular_expressel vagy lambda_expressel (sőt ezek lesznek majd a jobbak)
#pythonba a class nem lehet változónév


#bs.find_all(class='green') ->hibás lenne |megoldás1 : bs.find_all(class_='green') | megoldás2: bs.find_all('', {'class':'green'})



#tree navigation
#children -> közvetlen egyel alatta van
#descendant -> leszármazott, azaz valamiből lett -> lehet children is
#minden children descendant, de nem minden descendant children


#a beautifulsoup mindig a válaszott objektum leszármazottjaival foglalkozik

#pl :
#bs.div.find_all('img') | megtalálja az első img divet, majd az összes descendantot listázza

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

for child in bs.find('table',{'id':'giftList'}).children: # | .children -> csak olyan felmenőket keres, akik childrenek
 print(child)

#van .descendant tag is értelem szerűen!



html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

for sibling in bs.find('table', {'id':'giftList'}).tr.next_siblings:
 print(sibling)

 # a testvérek " siblingek " nem lehetnek önmaguk -> ezért ez a sor úgy dolgoz fel egy táblázatot, hogy a címet kihagyja
 #van .previous_sibling tag is értelem szerűen!

 #------------42 alja

 html = urlopen('http://www.pythonscraping.com/pages/page3.html')
 bs = BeautifulSoup(html, 'html.parser')

 print(bs.find('img', {'src': '../img/gifts/img1.jpg'})
       .parent.previous_sibling.get_text())


#------------Regular Expressions
#“Yes, this string you’ve given me follows the rules, and I’ll return
#it,” or “This string does not follow the rules, and I’ll discard it.” This can be exception‐
#ally handy for quickly scanning large documents to look for strings that look like
#phone numbers or email addresses.


#bbb -> 3db b
#aa* -> van a és másik a követi (0 is) -> így mindig lesz benne a
#(cc)* -> egy pár c, 0 is lehet
#(d|e) -> vagy d vagy e -> valamelyik a kettő közül

#cheat sheet asztalon





#-------------- email rule
#cheat sheet asztalon
#pl email-nél : [A-Za-z0-9\._+]+@[A-Za-z]+\.(com|org|edu|net)



#----------------- reguláris kifejezések beautifulsoupban

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img',
 {'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})
for image in images:
 print(image['src'])

#csak azokat a képeket keresi meg, ami /img/gifts/img(valami).jpg formátumúak




#----------------- sajátosságok (attribútumok) elérése

#nem mindig tagra keresünk, sokszor egy tagon belül valamilyen tulajdonságra
#például a után a href tag URL-jét keresve, vagy az img src tagját

#szintaxis :
#myTag.attrs
#myImgTag.attrs['src']



#----------------- Lambda kifejezések
#49.oldal alja.
#gyakorlatilag funkciókat lehet átadni paraméterként



#-------------- writing web crawlers

#a web crawlerek alapja :
# At their core is an element of recursion. They must retrieve page contents for a URL, examine that page for another URL, and retrieve that page, ad infinitum.




#wikipedia project -> 2 paget a legkevesebb ugrás számmal össze kapcsolni

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')

for link in bs.find('div', {'id':'bodyContent'}).find_all(
'a', href=re.compile('^(/wiki/)((?!:).)*$')):
 if 'href' in link.attrs:
   print(link.attrs['href'])

#szűrve megjeleníti a kapcsolódó linkeket

#ugyan ez flexibilis megoldással :
#azonban mind a kettő jó, és működő képes


def getLinks(articleUrl):
 html = urlopen('http://en.wikipedia.org{}'.format(articleUrl))
 bs = BeautifulSoup(html, 'html.parser')
 return bs.find('div', {'id':'bodyContent'}).find_all('a',
       href=re.compile('^(/wiki/)((?!:).)*$'))

links = getLinks('/wiki/Kevin_Bacon')
while len(links) > 0:
 newArticle = links[random.randint(0, len(links)-1)].attrs['href']
print(newArticle)
links = getLinks(newArticle)


#egész oldalas scraperek :
#hasznosak : adatgyűjtésre, és site map készítésre

#site map -> a top (általában main page) el kezdjük -> ez linket keres, ami megint linket keres -> végtelen trigger
#sok a duplikált site -> rendezett adat kell rá -> nem listába, hanem setbe gyűjtjük, mivel ebbe minden elemnek egyedinek kell lennie
#így ebbe csak az "új" linkek fognak bekerülni


#wiki oldalait scrapelő dolog példa:

#pages = set()
#def getLinks(pageUrl):
#global pages
#html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
#bs = BeautifulSoup(html, 'html.parser')
#for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
#if 'href' in link.attrs:
#if link.attrs['href'] not in pages:
#We have encountered a new page
#newPage = link.attrs['href']
#print(newPage)
#pages.add(newPage)
#getLinks(newPage)
#getLinks('')


#python ki crashel 1000 recursive keresés után -> large siteoknál ezt meg lehet előzni egy counterrel


#-------------- collecting data across an entire site
#help az asztalon | kód is


#With server-side redirects, you usually don’t have to worry. If you’re using the urllib
#library with Python 3.x, it handles redirects automatically! If you’re using the requests
#library, make sure to set the allow-redirects flag to True:

r = requests.get('http://github.com', allow_redirects=True)

#kód txt-ben
#lehet ide flow chartot is használni


#-------------- Web crawling models

#általában minden problémára van 1-1 model alapú megoldás, vagy legalább a megoldás alapját egy modell képezi


#-------------- Dealing with Different Website Layouts

import requests

class Content:
 def __init__(self, url, title, body):
  self.url = url
  self.title = title
  self.body = body

  def getPage(url):
   req = requests.get(url) #egy request
   return BeautifulSoup(req.text, 'html.parser')


 #-----------

class Crawler:

 def getPage(self, url):
  try:
    req = requests.get(url)
  except requests.exceptions.RequestException:
   return None
  return BeautifulSoup(req.text, 'html.parser')

#jobb megoldás 74-75. oldal körül


#Crawling sites through links
#80kb




#Crawling multiple page types



#Scrapy - scraping framework
#86. oldal -> install és simple alap cucc
# +CrawlSpider class
#ez mivel CMD-ből megy, így addig fog futni, amíg ki nem lépünk a programból, vagy be nem zárjuk a terminált










#Storing Data
#Élhető formában kell elmenteni az adatot, hogy használható is legyen, ne csak egy nagy "halmaz"
#nagy általánosságban 3 lehetőség van :
#a scraper adatbázisba ír
#A scraper egy adatforrásba ír (file stream)
#Emailbe dolgozik a scraper



#Adatformák tárolása :
#Média Fájlok -> vagy magát a fájlt letöltve, vagy az azt tárolt url-re hivatkozva
#link előnyei: gyorsabban fut a scraper, nem foglal helyet, könnyebb a kódot írni, kevesebb bandwitet eszik az oldalról
#hátrány: változhat, úgy tűnhet, hogy robot vagy -> tilthat, hotlinkingnek számít


from urllib.request import urlretrieve
from urllib.request import urlopen

html = urlopen('http://www.pythonscraping.com')
bs = BeautifulSoup(html, 'html.parser')
imageLocation = bs.find('a', {'id': 'logo'}).find('img')['src']
urlretrieve (imageLocation, 'logo.jpg')
#az urlretrieve egy adott link helyéről megpróbálja távolról letölteni az adott képet / fájlt
#alapból ugyan abba a mappába tárolja a letöltést, mint ahol a script fut

#ez a script csak egy fájlt tölt le -> általában nem aktuális, de megeshet

#ami mindent letölt egy oldalról -> 104. oldal !!!!
#figyelni kell, ha minden lejön | lehet benne random bash script, .exe fájl, malware stb




#----------- Storing Data to CSV

#egy sima táblázatot hoz létre, ahol az első szám egy szám, a második a szám plusz 2, a harmadik pedig a számX2
import csv
csvFile = open('test.csv', 'w+')
try:
 writer = csv.writer(csvFile)
 writer.writerow(('number', 'number plus 2', 'number times 2'))
 for i in range(10):
  writer.writerow( (i, i+2, i*2))
finally:
 csvFile.close()


#egy egész wikipédia táblázat leszedése és CSV-be rakása:
#Ez általában akkor hasznosabb, ha 1-2-nél több táblázat van, mivel kisebb táblákat vagy kevés táblát simán lehet copy pastel is megoldani, gyorsabb lesz, mint a script

import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://en.wikipedia.org/wiki/'
 'Comparison_of_text_editors')
bs = BeautifulSoup(html, 'html.parser')
#The main comparison table is currently the first table on the page
table = bs.findAll('table',{'class':'wikitable'})[0]
rows = table.findAll('tr')
csvFile = open('editors.csv', 'wt+')

writer = csv.writer(csvFile)
try:
 for row in rows:
  csvRow = []
  for cell in row.findAll(['td', 'th']):
   csvRow.append(cell.get_text())
   writer.writerow(csvRow)
finally:
  csvFile.close()



#--------- MySQL

#parancsok ugyan azok mint régen
#kell command lineba is dolgozni | parancsok ugyan azok
#phpMyAdminba is lehet -> könnyebb a visualization miatt
#110.-111. oldal -> régi alap parancsok
#előbb SELECT-el nézzük meg, hogy jó-e az adat, csak aztán használjunk UPDATE / DELETE parancsot




#---------- Integrating MySQL with python

#alapból nem beépített : pip intsall PyMySQL
#113.oldal -> hogyan tudjuk connectelni, mi a cur,conn és fetchcone()
#114.oldal | a wikipédia táblázat adatbázisba kapcsolása(írása)
# | utána csak tippek |



#119. oldal -> link storer code example
# új dolgok -> |
# insertPageIfNotExists() - akkor ad hozzá rekordot, ha nincs olyan oldal
# insertLink - egy új linket vesz fel a táblázatba akkor, ha már nincs egy ilyen link
# loadPages - ez dönti el, hogy egy oldal volt-e már látogatva vagy nem



#---------- Email

#az alapja ugyan az, mint a másik file-ba az email : smtplib és mimetext
#itt általában max 1-2 dolgot kell csatolni, a többi mehet simán (pl: JSONT)
#de kell hozzá egy email (SMTP) server
#kód 122. oldal (ugyan az, csak van benne egy bs4-es keresés)



#Encoding típusok, változások a kódban

#ASCII, UTF-8|16 stb -> több bit, azonban más nyelv és sokkal nagyobb karakter készlet
#ha nem annyira ismert a nyelv, akkor nagyobb a bit szám

html = urlopen('http://en.wikipedia.org/wiki/Python_(programming_language)')
bs = BeautifulSoup(html, 'html.parser')
content = bs.find('div', {'id':'mw-content-text'}).get_text()
content = bytes(content, 'UTF-8')
content = content.decode('UTF-8')



#JOBB CSV olvasás

#vagy letöltve olvassuk
#vagy script leszedi, beolvassa majd kitörli
#vagy StringIO objektummal beolvassuk -> legjobb megoldás


from io import StringIO

data = urlopen('http://pythonscraping.com/files/MontyPythonAlbums.csv').read().decode('ascii', 'ignore')
dataFile = StringIO(data)
csvReader = csv.reader(dataFile)
for row in csvReader:
 print(row)

#Sorok közötti hozzáférhetőség

 for row in csvReader:
  print('The album "' + row[0] + '" was released in ' + str(row[1]))


#A DictReader kiszedi az első sort a CSV fájlból (pl: nem lesz ott, hogy év, nap, id stb)

data = urlopen('http://pythonscraping.com/files/MontyPythonAlbums.csv').read().decode('ascii', 'ignore')
dataFile = StringIO(data)
dictReader = csv.DictReader(dataFile)
print(dictReader.fieldnames)

for row in dictReader:
 print(row)



#PDF -> PDFMiner3K
  #pip installos


#egy basic pdf beolvasása szövegként:

from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open

def readPDF(pdfFile):
 rsrcmgr = PDFResourceManager()
 retstr = StringIO()
 laparams = LAParams()
 device = TextConverter(rsrcmgr, retstr, laparams=laparams)
 process_pdf(rsrcmgr, device, pdfFile)
 device.close()
 content = retstr.getvalue()
 retstr.close()
 return content
pdfFile = urlopen('http://pythonscraping.com/'
 'pages/warandpeace/chapter1.pdf')
outputString = readPDF(pdfFile)
print(outputString)
pdfFile.close()



#117. oldal -> szenvedés a worddel


#-----------------------
#Az adat normális, olvashatóvá tétele
#az adatok sokszor rossz "formátumban" jönnek -> elírások, írásjelek, sortörések, helyesírási hibák miatt stb - > nekünk ezeket kell kijavítani
#sokszor már csak az adatbázisba kerülés után lehet kijavítani ha rosszul van megformázva

#megnézni mi az az ngram és 2gram, 121. oldal - 126.oldal
# OpenRefine -> nem formattálja a dolgokat, de segít a saját cuccok rendbe rakásába
#githubja - > https://github.com/OpenRefine/OpenRefine/wiki/Documentation-For-Users





#-----------------------
#Reading and Writing Natural Languages
#Markov Models -> legyen akárhány opció, a választható esélyeknek mindig 100%-ot kell alkotniuk | van ehhez ábra is
#ebből lehet generálni kb végtelen számú outcomot



#NLTK -> NATIONAL LANGUAGE TOOLKIT -> szóanalizálásra használt szoftver, nem annyira érdekes
# 149.oldal felett




#-----------------------
#Crawling Through Forms and Logins

#gettel kérjük az infót oldalról, POST-al küldjük bele

#-----------------------
#152. oldal -> request library
#-----------------------




#-----------------------
#Submitting a Basic Form jön
#kell hozzá request library

#name="firstname" -> ez fontos, mivel így a "firstname" lesz majd a POST
#ha le akarjuk másolni ezt a POST-ot, akkor ennek a változónak egyeznie kell

#fontos még az action, mivel oda küldjük, nem oda, ahol éppen az a form van -> az csak egy segítség

#két példa erre:

params = {'firstname': 'Ryan', 'lastname': 'Mitchell'}
r = requests.post("http://pythonscraping.com/pages/processing.php", data=params)
print(r.text)

import requests
params = {'email_addr': 'ryan.e.mitchell@gmail.com'}
r = requests.post("http://post.oreilly.com/client/o/oreilly/forms/quicksignup.cgi",
 data=params)
print(r.text)


#-----------------------
#Radio Buttons, Checkboxes, and Other Inputs

#itt kellenek az "elementek" értékei és nevei
#ha nem vagyunk benne biztosak az url-ből, akkor
#developer tool -> network (155.oldal)

#-----------------------
#Handling Logins and Cookies
#156.oldal


#-----------------------
#Scraping JavaScript
#ha nem Jscript van, hanem valami import pl: jquery, akkor azt valahol meg importálták (<script src=http://ajax.stb></script>)
#google analytics -> jscript forgalom figyelő extension ->alján scriptbe van benne általában

#164.oldal alja -> google maps

#-----------------------
#Executing JavaScript in Python with Selenium

#Selenium works by automating browsers to load the website,
#retrieve the required data, and even take screenshots or assert that certain actions
#happen on the website.
#kell neki egy thrid party -> pl: firefox to futhasson

#-----------------------
#phantomJS -> grafikus felület nélkül háttérben futtat scriptet


#-----------------------
#167. oldal -> ajax mögötti html kiszedése !!!!!!
#171. oldal -> handling redirect (átirányítások kezelése) !!!!!!!
#-----------------------


#-----------------------
#Crawling Through APIs (Application Programming Interface)
#https://www.youtube.com/watch?v=Yzx7ihtCGBs


#(in particular, APIs that allow a web server to com‐
#municate to a browser)

#The documentation for these APIs typically describes routes or endpoints, as URLs
#that you can request, with variable parameters, either in the path of the URL or as GET
#parameters

#általában 2 fajta válasz -> JSON vagy XML


import json

#egy aktuális élet példa:

def getCountry(ipAddress):


 response = urlopen('http://freegeoip.net/json/' + ipAddress).read().decode('utf-8')
 responseJson = json.loads(response)
 return responseJson.get('country_code')
print(getCountry('50.78.253.58'))


#-----------------------
#Undocumented APIs



#-----------------------
#Finding Undocumented APIs
#183.oldal -> google inspector kép


#-----------------------
#Combining APIs with Other Data Sources


#189.oldal wikipédia x geo project !!!!!!!!!!!!!


#-----------------------
#Image processing and text recognition

#sok szöveg képként van fennt -> nehezebben olvassák a botok
#kép átalakítása szöveggé -> OCR (optical character recognition) !!!!

#2 library -> pillow és tesseract (az első tisztítja a képet, az utóbbi pedig feldogozza azt)

from PIL import Image, ImageFilter

kitten = Image.open('kitten.jpg')
blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
blurryKitten.save('kitten_blurred.jpg')
blurryKitten.show()

#documentation : https://pillow.readthedocs.io/en/stable/




#tessreact és numpy -> 200 oldal körül, főleg image processing és clarification !!!!!!!!!
#+206.oldal -> passing CAPTCHAs


#-----------------------
#Avoiding Scraping Traps

#ha pl letiltják az IP-t nehéz kitalálni miért volt
#semmilyen error messaget nem dob vissza, mint pl egy fejlesztői web panel
#botként lett kategorizálva -> tilt és ennyi

# - > kicsit emberibbnek kell tűnnie a scrapernek



#-----------------------
#Looking like a Human
#kép -> netscraper looking human / 217.oldal kép

# a fejlécet lehet módosítani -> alapból nagyon úgy néz ki mint egy bot amit küldünk urlib miatt -> ezt azonban át lehet írni, hogy sokkal emberibbnek tűnjön

#request library-val lehet átírni


session = requests.Session()
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
 'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
 'Accept':'text/html,application/xhtml+xml,application/xml;'
 'q=0.9,image/webp,*/*;q=0.8'}
url = 'https://www.whatismybrowser.com/'\
 'developers/what-http-headers-is-my-browser-sending'
req = session.get(url, headers=headers)
bs = BeautifulSoup(req.text, 'html.parser')
print(bs.find('table', {'class':'table-striped'}).get_text)


#-----------------------
#Handling cookies -> 219. oldal //kicsit jobban eljrejt


#-----------------------
#Timing Is Everything

#Ha túl gyorsan töltünk le adatot (nem emberszerű viselkedés) / túl gyorsan töltünk ki formokat -> nagy az esély rá, hogy úgy fog kezelni a rendszer, mint egy botot és letilt

import time
time.sleep(3)
#néha legyen benne 1-2-3 mp szünet legalább 2 oldal betöltése közben -> nagyban könnyítni az életet


#-----------------------
#Avoiding Honeypots

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#This applies not only to forms but to links, images, files, and any other item on the
#site that can be read by a bot but is hidden from the average user visiting the site
#through a browser. A page visit to a “hidden” link on a site can easily trigger a serverside script that will block the user’s IP address, log that user out of the site, or take
#some other action to prevent further access. In fact, many business models have been
#based on exactly this concept.


#224. oldal -> selenium is.displayed(); megoldás !!!!!!!!!!


#-----------------------
#Testing Your Website with Scrapers
#igazából ez a chapter annyit takar, hogy lehet automatán tesztelni egy weboldal front end és (korlátozottan) back endjét azzal, hogy python automated taskokat hajt végre (formokat tölt, kezeli magát az oldalakat stb)

#-----------------------
#Processes versus Threads
#239.oldal - 255.oldal

#-python támogatja mind a kettőt, néha jobb 2-3 dolgot futtatni egyszerre (gyorsabb)

#-----------------------
#Scraping Remotely

#nem külön szálakon / processoron scrapelés, hanem egy teljesen új gépen / virtuális / távoli /stb hoston keresztül
#külön remote serveren - > nincs annyi IP blokk, nem olyan erőforrás igényes,
#Tor / külön remote server / vpn - mind megoldás lehet a blockra


#PySocks - > kb ugyan az, mint a Tor, több proxy szerveren át routeolja a forgalmat
#simán lehet torral együtt is használni


import socks
import socket
socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
socket.socket = socks.socksocket
print(urlopen('http://icanhazip.com').read())

#Jó ötlet lehet még a cloud, pl amazon



#263. oldal - jogi felvetések, kérdések

#minden google bot által scrapelt oldal másolata:
#http://webcache.googleusercontent.com/search?q=cache:http