try:
    from pyautogui import *
    import pyautogui, time, win32api, win32con,keyboard
except ImportError:
  input("Az importok nem lettek teljesítve a requirements.txt fájlból!")

time.sleep(4)
#első argument az x kezdet, második az y kezdet, harmadik a szélesség, negyedik a magasság


#HOGYAN KAPJUNK MEG EGY BÜDÖS SZAR REGION HELYZETET
get1 = input('\nPlace cursor at the top left of the region you want to capture, and then press enter \n')
pos1 = pyautogui.position()

get2 = input('Now place your cursor at the bottom right of the region you want to capture, and press enter \n')
pos2 = pyautogui.position()

width = pos2[0] - pos1[0]
height = pos2[1] - pos1[1]

print('Your region is... \n')

print('region=('+str(pos1[0])+','+str(pos1[1])+','+str(width)+','+str(height)+') \n')

#img = pyautogui.screenshot(region=(150,200,1000,1000))
#img.save(r"C:\Users\ADMIN\Desktop\automation projects\aimbooster\savedimage.png")




#Kör center szine: (255, 219, 195)

while keyboard.is_pressed('q') != True:

    #kép értékei 
    pic = pyautogui.screenshot(region=())

    width, height = pic.size

    for x in range(0, width, 5):
        for y in range(0, height, 5):

            r, g, b = pic.getpixel((x, y))

            if b == 195 and r == 255 and g == 219:
                click(x+"a region első koordija", y+"A region másodi kordija")
               
        
