req = requests.get("https://www.books.ie/")
print(req)
print(type(req))

#req2 = requests.api
#print(req2)

req3 = requests.Response
print(req3)

req4 = requests.get("https://www.books.ie/")
print(req4.headers)

req5 = requests.get("https://www.books.ie/")
#print(req4.text)

req6 = requests.get("https://www.books.ie/")
print(req6.text.count("a"))

req7 = requests.get("https://www.books.ie/")
#print(req7.url)
#print(req7.cookies)
#print(req7.content)
#print(req7.elapsed) #ping
print(req7.encoding)

#link_lista = [
#    "https://www.facebook.com/"
#    "https://www.google.com/search?q=google&oq=google&aqs=chrome..69i57j46i131i199i433i465i512j0i131i433i512l5j0i512j0i131i433i512l2.573j0j7&sourceid=chrome&ie=UTF-8"
#]

#for links in link_lista:
#    req9 = requests.get(links)
#    print(req9.text)
#    outfile = open("C:/Users/ADMIN/Desktop/asd/test.txt", "w")
#    outfile.write(str(test.text))