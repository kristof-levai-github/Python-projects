try:
    from pyautogui import *
    import pyautogui, time, win32api, win32con,keyboard
except ImportError:
  input("Az importok nem lettek teljesítve a requirements.txt fájlból!")
#pip install pywin32

#enged bele menni a játékba
time.sleep(4)

#click function -> ezzel, sokkal gyorsabb, mintha konkrétan a pyautogui kattintgatna

#egér pozíciójának ellenőrzése:
#pyautogui.displayMousePosition()
#vagy
#while keyboard.is_pressed('q') != True:
#    print(pyautogui.position())
#    time.sleep(3)

#=============================================

#de egyébként a 4 értéket lehet 4 db pyautogui.position()-el is megoldani, ha valamit lenyomunk, mint ahogy pl a likereknél van 

#=============================================

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
    

#fekete rgb színe: 0,0,0
    
#line position 1-4
    
    
while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel(581, 400)[0] == 0:
        click(581, 400)
    if pyautogui.pixel(682, 400)[0] == 0:
        click(682, 400)
    if pyautogui.pixel(770, 400)[0] == 0:
        click(770, 400)
    if pyautogui.pixel(869, 400)[0] == 0:
        click(869, 400)
