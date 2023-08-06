'''
print(a)

print(a) hibát ad, mivel nincs benne "" -> le lehet kezelni pl: try:, except: 
//különböző hibákra, különböző hibak"kód" -> ezeket külön le lehet kezelni
'''
#example2
try:
    print(x)
except:
    #you can use pass, continue or break
    pass

#example1
#because of a part of the try statement failed, its not going to execute at all
try:
    print("ab")
    print(a)
except:
    print("A not exist cuz error")

print("we are here now!")

# we can put these in loops too for example
for i in range(5):
    try:
        print("ab")
        print(b)
    except:
        print("Not exist cuz error")

#you can write Exceptions in the except: these are going to save the error into a variable, and you can print that out as a string 
try:
    print(a)
except Exception as e:
    print(str(e))