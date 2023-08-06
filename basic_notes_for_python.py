#---------------------------------------------------------normál alap python

#file->new->py file -> ha nem a mainbe akarunk dolgozni
#file -> settings -> sok mindent lehet benne állítani, pl: plugin, font stb plusz a consolet is lehet basztatni pl: színt váltani, stb
#process finished executed 0 -> nincs benne hiba - run után
#mindegy , hogy ' vagy "

#tipikus print
import time

print("I love pizza")
print('its really good')

#változók
#a változók értékeket tárolnak, amilyen az érték, úgy viselkednek (numbers, string, booleans stb)
#' és " is jó

#string

name1 = 'kristof'
name2 = "levai"
name3 = name1 + name2

#változót kiiratni itt is quote nelkul kell

print(name1+" "+name2)
print(type(name1)) # a type, megadja a változó adat típusát
print(name3)

#numbers

age = 21
age = age + 1 #lehetne age+=1 is, ugyan az

print(age)
print(type(age))

#stringet és numbert nem lehet együtt kiíratni phytonba -> át kell konvertálni stringgé a numbert
print("your age is:"+str(age)) #az str átkonvertálja

#float = lebegőpontos számoknak (decimális számoknak)

height = 250.5
print(height)
print(type(height))

#boolean = igaz/hamis
#főleg if-nél használják, mikor el kell dönteni, hogy igaz-e egy állítás
#True és False is nagy T és F


human = True
print(human)
print(type(human))



#multiple assignment = egy sor kódon belül több változó

name = "Kris"
age = 21
attractive = True
#helyett

name, age, attractive = "Kris", 21, True

print(name, age, attractive)

#ha ugyan azok az értékek

spongyabob = 30
patrik = 30

spongyabob = patrik = 30

print(spongyabob, patrik)




#string metódusok

name = "Kris"

print (len(name)) #hossz

#ha a változó után írunk egy pontot, akkor kiad egy csomó opciót, amiből választhatunk name.
print(name.find("K")) #hol van az adott karakter - 0 ról kezdi a számolást
print(name.upper)
print(name.capitalize())
print(name.lower())
print(name.isdigit())
print(name.isalpha()) #minden karakter benne az abc betűi -> ha lenne benne egy space már nem lenne az
print(name.count("i"))
print(name.replace("s", "ss"))
print(name*3) #3x íratja ki a stringet, habár ez nem metódus
#stb, sok van még . után kiadja mindet is




#type casting = adatok konvertálása másik adat típussá

x = 1
y = 2.1
z = "3"

#minden intre konvertálása
#így kiíratva, az alap változó nem változik, csak a printig alakítjuk őket
#a floatingot kerekíti

print(int(y)+x+int(z))

#minden string
print(str(x)+str(y)+str(z))

#minden float
print(float(x)+y+float(z))

#ezen belül is lehet művelet
print(float(x)+y+float(z*3))



#user input kezelése
#konzolba válasz, aminek a válaszát a kerdes változó tárolja

kerdes = input("Mi a neved?:")
print("Hello" +kerdes)

#be lehet simán is kérni, úgy, hogy nincs ott az int -> de úgy nem lehet vele matematikai műveletet végezni
#egyszerűbb átalakítani, ha int vagy float a kérdés
age = int(input("Hány éves vagy"))
age += 1

print(age)

#nem lehetne intet és stringet összerakni -> vissza kell alakítani stringé, ha ki akarjuk iratni
print("Te" + str(age)+ "éves vagy")

magassag = float(input("Milyen magas vagy?"))
print("Te "+ str(magassag)+ "magas vagy")

#matematikai funkciók

import math

pi = 3.14
k = 5

print(round(pi)) #kerekít
print(math.ceil(pi)) #a math modulenak a ceil funkcióját kerestük -> mindig math. lesz, ugyan úgy kiadja mint stringnél, //ez felfele kerekít
print(math.floor((pi))) #lefelé kerekít
#print(math.abs(pi)) #mennyire van egy szám a 0-tól
#print(math.pow(pi,2))
print(math.sqrt(25)) #négyzetgyöt
print(max(pi,k)) #legnagyobb értékűt keresi, nem math.-ban van
print(min(pi,k)) #legkisebbet keresi nem math.-ban van




#string slicing  = indexing[] vagy slice()
# [start:stop:step] -> az indexelés és slice (slicenál , kell ) felépítése, nem muszáj minden indexet használni benne, mindent amit számolunk, ahhoz +1 mert az excluzive


#indexing[]
nev6 = "Kristof levai"
elso_nev = nev6[0:7:1] #7 helyeett lehehtne endet is írni, és akkor a végéig megy
print(elso_nev)

visszafelenev = nev6[::-1]

#slice()
website = "http://google.com"
website1 = "http://wikipedia.com"
slice = slice(7, -4, 1)
#negatív index -> -1-től kezdődik, szóval -4 = .com csak levágva // ez ugye azért kell, mert az url sokszor változik, de a vége marad

print(website[slice])
print(website1[slice])



#if statementek = if, elif, else //akkor valósul meg, ha valami bekövetkezik, azaz igaz rá az állítás (ha valami hamis és hamis lesz, az is igaz)
#nem kell elif vagy else, ha nem kell használni

age100 = int(input("Hány éves vagy?"))

if age100 == 100: # == a comparator
    print ("száz éves vagy!")
elif age100 >=18:
    print ("Felnőtt vagy!")
elif age100 < 0:
    print("Még meg sem születtél!")
else:
    print("gyerek vagy!")



#logikai operátorok (and, or, not ) //eldönti hogy több dolog kozül mi van
# ha bármi elé not-ot írnánk, akkor fordítva lenne a dolog (ha  nem igaz, akkor igaz
# pl: if not(temp >= 0 and temp <= 30):
#     print("maradj bennt!")


temp = int(input("milyen meleg van kinnt?"))

if temp >= 0 and temp <= 30:
    print("a hőmérséklet jó ma")
#elif temp > 30 and temp <= 60:
#   print("ki ne menj!")
elif temp < 0 or temp > 30:
    print("ki ne menj!")






#while loops = Addig végrehajtja az utasításokat, ameddig azok igazak
#kell valami, hogy kijöjjünk a while loopból, vagy infinite loop lesz

# while 1==1:
#    print("Ez egy infinity loop!")

#muszaj = ""

# while len(muszaj) == 0:
    #name = input("Enter your name: ")
    #print("Hello" +muszaj)

#itt ha bármi is be van írva, akkor már escape lesz, lehetne not muszaj is például







#for ciklus -> valahányszor végre hajt egy kódsort
#while = unlimited | for = limited
#lehet sima ranget megadni, vagy mettől meddig, a harmadik szám pedig a step (mint a slice-nál)

for i in range(10):
    print("Ez most 10x lefut?")
    print(i) # 0-9 ig számol, mivel sequenciális, lehet számolni is ezzel

for j in range(50,100): #az első szám inkluziv, a második excluziv
    print(j)

for á in range (1,10,2):
    print(á)

#ki lehet iratni egyesével is egy stringet -> ezt is lehet számolni
for v in "Kris":
    print(v)

#parancs futtatása előtti alvó állapot:
#pl: várjon 2 mp-t mielőtt a következő sort futtatja
# btw sok minden van még a time. után, azokat ki lehet irattatni

time.sleep(2)




#nested loops = loop a loopban (akár for akár while)
#az első loop mindig hamarabb lefut, minthogy valami lefutna a külső loopban

rows = int(input("how many rows?"))
columns = int(input("how many colums?"))
symbol = input("Milyen szimbólum?")

for ú in range(rows):
    for ű in range(columns):
        print(symbol, end="") #az end="" nem kezd minden szimbólumra új sort
    print()



#loop control = megváltoztatják a loop normál államotát
#break, continue, pass | break = teljesen megszakítja | skip = kihagyja a következőt a loopban | pass = semmit nem csinál, gyakorlatilag helykitöltő


phone_number = 123-457-689
# tegyük fel, hogy nem akarjuk bele a kötőjeleket -> ki tudjuk venni a continue-val
#break -> általában ha ki akarunk jönni egy whileból

#for é in phone_number:
#    if é == "-":
#        continue
#    print(é, end="")

#pass-re példa: | gyakorlatilag tényleg csak egy helykitöltő

#    if m == 13:
#        pass
#    else:
#        print(m)



#listák = egy változóba több értéket tárol

kocsi = ["bmw", "skoda", "mercedes", "aston martin"]
print(kocsi) #ha csak így adjuk meg, akkor mindent kiírat a listába

#a listában indexelve vannak az itemek. Az első item 0 indexet kap

print(kocsi[2]) #mercedes lesz


#ha azonnal változtatni kell :
#kocsi[0] = bentley
#print(kocsi[0])


#lista kiíratása forciklusba:

for í in kocsi:
    print(í)


#listák hasznos funkciói:
#food. valami -> kiadja a funkcióit

kocsi.append("citroen") #hozzáadja a lista végére
kocsi.remove("mercedes") #kiveszi a listából
kocsi.pop() # ?
kocsi.insert(0, 'peaguet') # 0. helyre berakja az elemet
kocsi.sort() # rendezi a listát
#food.remove  ---- mindent töröl a listából



#2D listák | #a 3D listák, már mátrix lesz ez még csak 2x2
#gyakorlatilag lista a listába

lista1 = ["elem1", "elem2"]
lista2 = ["elem3", "elem4"]
listalista = [lista1, lista2] #összefűzi a listákat

print(listalista) #kiíratja mindet
print(listalista[0]) # csak a lista1-et íratja ki
print(listalista[0][0]) # csak a lista1 első elemét íratja ki






#tuples = egy olyan adatkollekció, ami rendezett és megváltoztathatatlan
#használata: olyan adatokat egymáshoz rendezni, amik kapcsolódnak egymáshoz
# () []-helyett


student = ("Bro",21,"male")

#metódusok
print(student.count("Bro"))
print(student.index("male"))

#kiíratás for looppal

for apad in student:
    print(apad)

if "Bro" in student:
    print("Bro is here!")



#set = olyan adatok gyűjteménye, ami nem rendezett és nem indexelt. Nem lehet két azonos érték
# {} - kell

utensils = {"fork","spoon","knife"}
dishes = {"bowl","cup"}

#for apad2 in utensils:
#    print(apad2) #nem biztos, hogy ugyan abba a sorrendbe lesznek, mint fennt -> ha 4-5 knife lenne, akkor is csak egyet jelenítene meg

    #metódusok
  #  utensils.add("napkin")
  #  utensils.remove("fork")
    #utensils.clear() #minden elemet kitöröl
  #  utensils.update(dishes) #minden dishes elemet hozzá az a utensilshez

print(utensils)

#2 setet összefűzni egy harmadik különállóba

dinner_table = utensils.union(dishes)
print(dinner_table)

#mi van a utensilsbe, ami a másikban nincs benne (összehasonlítás)
print(utensils.difference(dishes))
#mik a közös elemek a kettőbe
print(utensils.intersection(dishes))





#dictionaries = "szótár"
#egy változtatható, nem rendezett érték kollekció, ahol minden | egyedi kulcs: érték | pár
#gyors, mert hashelhető -> gyors adathozzáférést biztosít
#ide is {} kell, csak értékkel :


fővárosok = {'USA':'Washington DC',
             'Magyarország':'Budapest',
             'Oroszország':'Moszkva'}

#Ez a megadás nem feltétlen jó -> ha olyat kérünk így, ami nincs benne, akkor kidob hibával és nem olvas tovább
print(fővárosok['Oroszország']) #Moszkva lesz

#Get method

print(fővárosok.get('Németország')) #akkor se lesz hiba, ha nincs benne, csak kiírja, hogy nincs

#érdekes metódusok

print(fővárosok.keys()) #csak az országot
print(fővárosok.values()) #csak a városokat
print(fővárosok.items()) #mindent kiír


#forciklusos kiíratás

for key,value in fővárosok.items():
    print(key,value)

#Akkor is lehet bele írni kivenni mikor a program fut

fővárosok.update({'Németország':'Berlin'})
print(fővárosok.items())

fővárosok.update({'USA': 'New York'}) #kicseréli a washingtont new yorkra
print(fővárosok.items())

#fővárosok.pop({'Magyarország'}) #kitörli ezt az elemet
print(fővárosok.items())

#fővárosok.clear() | kitörli az egész dictionarit






#index operátorok [] = hozzáférést biztosítanak egy sorozat elemeihez (legyen az string, lista, vagy sor(tuple))

egynev = "Kris"

#ha az első betű kisbetű, akkor kicseréli azt egy nagybetűre és kiíratja
if(name[0].islower()):
    egynev = name.capitalize()
    print(egynev)




#Funkciók = egy olyan kódblokk, ami csak akkor hajtódik végre, hogyha valahova meghívják
#def - el kezdődik nem function()-nal

def hello(name): # first_name, last_name kéne a ()-ba ha már 2 argumentet akarnánk küldeni -> meg kell egyeznie az adott db-nak a hívott db-al
    print("Szia! Üdvözöllek: "+name)
    #pass -> ha még nem tudjuk, mit akarunk vele csinálni csak skippeljük
    print("Legyen szép napod!")

#ha arugmenteket használunk, akkor mindig 2 kell megadni -> olyan, mint egy nickname

hello("Cecilia")
hello(name) # többször is meghívható | lehet variable-t is hívni, vagy előre megadott értéket




#return statements = a funkciók vissza küldik az értéküket a hívóhoz -> ezek az értékek a funkció visszatérési értékei

def multiply(number1,number2):
    result = number1*number2
    return result

#print(multiply(6,8))
#vagy
#x = multipy(6,8)
#print(x)

#vagy nem result és return, hanem megoldjuk egy sorban pl:
#return = number1*number 2 | //2 helyett 1 sor lett






#keyword arguments = "állítások" megelőzve egy azonosítóval, amikor elküldjük őket egy funkcióhoz
#itt a sorrend nem számít, a positional argumenteknél igen (előzőeknél)

def hellow(first,middle,last):
    print("Hello"+first+" "+middle+" "+last)

hellow(last="Zalán", first="Lévai", middle="Kristóf") #mivel van társított érték, így nem számít, a sorrend, mert mindig jól adja vissza





#nested function calls = function meghívások function meghívásokba
#először a legbelsők lesznek feldolgozva
#az egyik visszatérési érték a másik kezdő értéke lesz

#bekéri az inputot, majd átalakítja úgy, hogy pozitív egész legyen, majd legvégül kiíratja, mivel az van legkívül
print(round(abs(float(input("Írj be egy pozitív egész számot")))))





#változó kiterjedés | variable scope = az a terület, ahol egy változó érvényes
#egy sima változó, csak ott használható, ahol létre lett hozva
#létre lehet hozni globálist és lokális változókat is ->

#lehet globális és lokális név is ugyanaz -> mivel nem fogják egymást érinteni
#feldolgozási sorrend pythonnál : LEGB -> LOCAL|ENCLOSING|GLOBAL|BUILT-IN


name11 = "Code" #globális változó, bárhová meg lehet hívni, mivel semmilyen funkció, stb nem tartalmazza

def display_name():
    name10 = "Code" #local scope -> csak a funkción belüli
    print(name10)




#*args = minden argumentet bepakol egy tuple-ba (sorba)

def add(*args):
    sum = 0
    for i in args:
        sum+= i
        return sum
    #így bármilyen számot be lehet írni és összeadja őket. Nem kell korlátozni argument name-el: | add(number,1,2,stb) |
    #ugye a tuplet nem lehet változtatni. Ha valamit nekünk közben mégis kéne, át tudjuk konvertálni pl listává: stuff = list(stuff)

print(add(1,2,3,4,10,12,20))




# **kwargs = olyan paramétreke, ami minden argumentet egy dictionaribe (könyvtárba pakol)
#hasznos, mivel így a funkciók elfogadhatnak bármennyi keyword argumentet | (jobban lehet nevesített értékkel dolgozni)


def hellow1(**kwargs):
    print("Hello"+ kwargs['first']+' '+ kwargs['last'])
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")

    #így igazából ugyan úgy bármenyi értéket belerakhatunk

hellow1(title="Mr.",first="Lévai",middle="Kristóf",last="Zalán")





# str.format() = formázási metódus | opcionális | több kontrollunk lesz a kimenet felé


animal = "cow"
item = "moon"

print("The"+animal+" "+"Jumped over the"+" "+item)
print("The {} jumped over the {}".format("cow","moon")) #simán behelyettesít
print("The {0} jumped over the {1}".format(animal,item)) # positional argument
#("The {animal} jumped over the {item}".format(animal="cow", item="moon")) #keyword argument | itt már nem is kellene változót használni

# a {0}|{1} és az {animal}{item} -> megfordíthatóak -> fel lesznek cserélve a szavak de akár lehet {item}{item} is -> többször fel lehet használni
# a {} egy placeholder, |helykitöltő|, amibe bele rakjuk utólag a változót / szót
#ugyan az lesz, mintha hosszan írnánk le, viszont kicsit "elegánsabb, és jobban néz ki"


#másik módszer -> egy változóban tárolva

text = "The {} jumped over the {}"
print(text.format("cow","moon"))

#padding adása egy texthez : {:10} -> 10 egység paddig //nem látszik, csak ha mögé is van írva valami
#left-align: {:<10} | right-align: {:>10} | center-align: {:^10}
#ha egybe kéne rakni az argumenttel : {lu:^10}. Nice to meet you".format

lu = "lu"
print("Hello my name is {:10}. Nice to meet you!".format(lu))



#számok formázása
# :.2f -> 2 decimális értékig mutatja (és kerekít)
# :b -> bináris kiíratés | :o ->octo number
# :X -> nagybetű | :x ->kisbetű
#ha a szam = 1000 és :, -> mindegy 1000 elé rak egy vesszőt (1,000)
# :e -> scientific notation kisbetű | :E scientific notation nagybetű

szam = 3.14159

print("the number of pi is {:.2f}".format(szam))




#random module = random number generátor , stb | pár hasznos dolog

import random

X = random.randint(1,6) #1-6 között random szám
Y = random.random() #teljesen random és nem csak egész szám

myList = ['rock', 'paper', 'scissors']
Z = random.choice(myList) #random választ egyet

cards = [1,2,3,4,5,6,7,8,9,"J","K","Q","A"]
random.shuffle(cards) #megkeveri a listát

print(X)
print(Z)
print(cards)



#exception handling = kivételkezelés = egy olyan dolog, ami végrehajtás közben történis és megzargatja a program rendes futását
#try: ami a program | except -> kivétel //nem csak egy exceptet lehet bele rakni | végére mindig finally: -> mindig le fog futni
#ha fájl nyitás van, akkor finally: - val be lehet zárni pl
#bele lehet rakni egy ifbe -> csak akkor iratja ki, ha nincsen benne hiba, egyébként pedig csak a hibát írja

#try:
#numeratorr = int(input("Adj meg egy számot amit el akarsz osztani"))
#denominator = int(input("Adj meg egy számot, amivel osztasz: "))
#result = numeratorr / denominator
#print(result)
#except Exception as E:  //nem muszáj az E
#print(E)
#    print("valami hiba van!")
#finally: print("This will always execute")




#basic file handling

import os

path = "C:\\Users\\ADMIN\Desktop\\pythontest.txt" #double backslash, mert a \ már használja a python

if os.path.exists(path): #meg lehet vele nézni, hogy az adott út létezik-e
    print("that location exist!")
    if os.path.isfile(path): #meg lehet vele nézni, hogy fájl-e mappa-e stb
        print("it is a file!")
    elif os.path.isdir(path):
        print("ez egy könyvtár!")
else:
    print("That location doesn't exist! ")




#fájl beolvasás
#megnézni, hogy egy nagy adat szart hogy kell beolvasni és listába vagy dictionarybe rakni
#csv beolvasása többféle képpen leírás:
#https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/


#csv beolvasása:

#import csv
#with open('email.csv', 'r') as csfile: # az r a read
#   reader = csv.reader(csvfile)

#fájl beolvasás 2.0

with open("C:\\Users\\ADMIN\Desktop\\pythontest.txt") as file: #automatán bezárja magát
    print (file.read())
print(file.closed) #megnézi nyitva van-e a fáj


#vagy
try:
    with open("C:\\Users\\ADMIN\Desktop\\pythontest.txt") as file:
        print (file.read())
except FileNotFoundError:
    print("nincs ilyen fájl!")


#fájlok írása

text="Bennelévőszövegszar\nnamindegy"

with open("teszt.txt", "w") as file: #w = csak írás | #a = hozzáadja a szöveget a meglévőhöz
    file.write(text)


#fájlok másolása
#copy() = copyfile+hozzáférési mód + lehet mappába másolni
#copy2() = copy() + metaadatokat is átmásolja
#copyfile() = a fájl tartalmát másolja

import shutil

shutil.copyfile('teszt.txt', 'copy.txt') #source,destination | honnan - hova
#shutil.copy('teszt.txt', 'copy.txt')
#shutil.copy2('teszt.txt', 'copy.txt')
#meg lehet adni file pathet is C:\\stb\\stb




#fájlok mozgatása

source = 'teszt.txt'
destination = 'C:\\Users\\ADMIN\\teszttt.txt'

try:
    if os.path.exists(destination):
        print("Már van egy ilyen fájl")
    else:
        os.replace(source,destination) #átnevezzük vele és felül is írjuk, szóval innen el fog tűnni
        print("a fájl átmásolva")
except FileNotFoundError:
    print(source+"was not found!")




#fájlok törlése

import os

#os.remove('torles.txt')

#vagy

path = 'torles.txt'
#os.remove(path)

try:
    os.remove(path)
except FileNotFoundError:
    print("nem található a fálj")
except PermissionError:
    print("Nincs jogod kitörölni!")
else:
    print("A fájl törlődött!")


#mappák törlése: os.rmdir(path)
#shutil.rmtree(path) -> shutil modulba van -> kitörli a mappát és az összes hozzá tartózó fájlt




#modulok = olyan fájlok, amik python kódot tartalmaznak -> lehetnek benne funkck, osztályok stb
#moduláris programozáshoz van, ami elkülöníti a program egyes részeit

import message # egy másik .py file, vagy valami más fájl a könyvtárba

message.hello() # a messages.py hello funkcióját ide hívtuk

#vagy import message as msg = msg.hello() | gyakorlatilag olyan, mint egy alias
#vagy from message import hello,bye,stb # nem kell a message.hello, elég a hello

#help("modules") -> kilistázza az összes python modult

#---------------------------------------------------------normál alap python vége

#---------------------------------------------------------email

#kell hozzá -> smtp server

import smtplib
from email import message

#sima email küldése, attachment nélkül:


#from_addr = 'email-honnan'
#to_addr = 'email-hova'
#subject = 'ez lesz az email szövege (fejléce)'
#body vagy content = 'Ez lesz magában a levélben!'

#msg = message.Message()
#ms.add_header('from', from_addr)
#msg.add_header('to', to addr)
#msg.add_header('subject', subject)
#msg.set_payload(body)
#msg

#server = smtplib.SMTP('smtp.dreamhost.com', 587) #email-server - port
#server.login(from_addr, 'password') - email, pass
#server.send_message(msg, from_addr=from_addr, to_addrs=[to addr]) | lehet email lista is



#email küldése attachmenttel:

import smtplib
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import  MIMEMultipart
from email.mime.application import MIMEApplication


#from_addr = 'email-honnan'
#to_addr = 'email-hova'
#subject = 'ez lesz az email szövege (fejléce)'
#body vagy content = 'Ez lesz magában a levélben!'

#msg = MIMEMultipart()
#msg['From'] = from_addr
#msg['To'] = to_addr
#msg['Subject'] = subject
#body = MIMEText(content, 'plain')
#msg.attach(body)

#filename = "kep.png
#with open(filename, 'r') as f:
    #attachment = MIMEApplication(f.read(), Name=basename(filename))
    #attachment = ['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(filename))

#ezzel a 4 sorral gyakorlatilag leformáztuk

#msg.attach(attachment)

#server = smtplib.SMTP('smtp.dreamhost.com', 587) #email-server - port
#server.login(from_addr, 'password') - email, pass
#server.send_message(msg, from_addr=from_addr, to_addrs=[to addr]) | lehet email lista is




#Sok Email küldése egy .csv fájlból
#simán sok email küldése egy listából:
#https://levelup.gitconnected.com/sending-bulk-emails-via-python-4592b7ee57a5

import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import  MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders



#email_semder = "az az email, amiről küldjük a mass-t"
#password = "sender email passwordja"
#subject = "Hajrá!

#with open('email.csv', 'r') as csfile:
 #   reader = csv.reader(csvfile)
  #      for line in reader:
   #     text="hello"+line[1]+"you"+line[2]+"plan has been activated" |line1,2 = második és harmadik sor a csv-nek pl: ha ,-el van elválasztva akkor az 1 és 2. , utáni lesz
    #    print(text)

#email_send = line[0]
#msg = MIMEMultipart()
#msg[from] #ugyan az mint fennt
#msg[to]
#msg[subject]
#msg.attach(MIMEText(text,"plain"))
#text = msg.as_string()


#server = smtplib.SMTP_SSL | ha kell ssl| ('smtp.dreamhost.com', 587) #email-server - port
#server.login(from_addr, 'password') - email, pass
#server.sendmail(email_user, email_send, text)

#server.quit()
#google -> allow less secure apps: ON -> google-nél enélkül tiltja a python scriptet




#emails http-vel
#minden ugyan az, csak a body változik

#body = """<html>
#            <body>
 #             <p>Hi,<b>My name is Sarath Kaul</b></p>
  #            <p> I am reaching out to you to check my email HTML Content </p>
   #         </body>
    #      </html>
     #  """
#msg.attach(MIMEText(body, 'html')



#--------------------------------------------------------------------GUI

#https://www.youtube.com/watch?v=8KvA5tU7Fqk&list=PLBUzXlyEGqqSvVd6tia-rhcnZI2wKQn_1
#pyqt6 felrakva

#basic syntax:
#import:

from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import sys

#main window
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
                #ide lesz írva a kód
        #QMainWindow
        self.setWindowTitle("fejléc")
        self.setMinimumSize(300,300) #width,height (px)
        self.setMaximunSize(1300,1300)
        #self.setWindowIcon(Qicon("icon path")) #kell hozzá a fenti module import
        #self.setStyleSheet("ide megy a css fájl")
        #vagy lehet bele írni css-t is :
        self.setStyleSheet("background:red") #rgb -> background:rgb(0,1,2)

        #Widget
        self.main_screewn = QWidget() #létre hozzuk a main screen widgetet
        self.setCentralWidget(self.main_screewn)


        #Label
        self.label1 = QLabel(self.main_screewn)
        self.label1.setText("Hello world :)")
        self.label1.setGeometry(20,20,100,100) #(x,y,méret1,méret2 (width,height))
        self.label1.move(150,150) #nem a méretet és elhelyezést adja meg, hanem csak az elhelyezést
        self.label1.setStylesheet("background:red; color=yellow") #ugyan az mint fennt, lehet rgb és külső css is
        self.label1.setWordWrap(True) #sortörés

        #font
        self.font = QFont()
        self.font.setFamily("Calibri")
        self.font.setFontSize(18)
        self.label1.setFont(self.font) #így adjuk hozzá a labelhez


        #buttons
        self.btn1 = QPushButton(self.main_screewn)
        self.btn1.setText("Kattints rá!")
        #self.btn1.setGeometry() | ugyan az, mint a többinél
        self.btn1.setFont(self.font)
        self.btn1.setStlyeSheet("background=black;color=white") # u.a mint a többinél

        def print_hello():
            print("hello")

        self.btn1.clicked.connect(print_hello) #button össze kötése funkcióval ha rákattintanak


        #de lehet olyat is, hogy pl a print_Helloba az van, hogy self.label1.text -> akkor mindig az írná ki
        #de a funkciónak előtte kell lenni ha kiíratja
        #kivéve ha így írjuk be:
        #self.btn1.clicked.connect(Lambda: print_hello())

    #7 jön



#applikációk
app = QApplication() #ebbe még jön majd később érték []
window = Window() #ablakosan
window.show() #megjelenítés
sys.exit(app.exec()) #ha az applikáció kikapcsol, akkor a script leáll
#magyarul, amíg nem az x-el kapcsoljuk, vagy máhogy, addig fut (nem áll le, ha kikattintasz belőle)



