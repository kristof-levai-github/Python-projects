# Import the relevant modules
import pyautogui
import time

#=============================================================================
# Keyboard functions
#=============================================================================
pyautogui.write("hello")
pyautogui.write("hello", interval=0.25) #minden karakter után fél mp késés
pyautogui.press(["enter","enter","space"])
pyautogui.press("space", presses=3)
pyautogui.press("space")
pyautogui.keyDown("shift") #lenyomja a shiftet
time.sleep("40")
pyautogui.keyUp("shift") #felengedi a shiftet

#lenyomva tartja a shiftet, a 3 leftig, majd felengedi azt
with pyautogui.hold('shift'):
    pyautogui.press(['left', 'left', 'left'])

#keyboard keys :

['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']

#=============================================================================
# Screenshot functions
im1 = pyautogui.screenshot(region=(0,0, 300, 400)) #region = ha nem akarjuk az egész képet fotózni
pyautogui.screenshot("screenshot.png")

#ha tudjuk valamilyen képnek a helyét azt meg is lehet találni -> az abszolút helyzet változhat, azonban a pygui meg tudja találni kép alapján is
#túl sok minden van ide -> documentationbe megvan

#https://pyautogui.readthedocs.io/en/latest/screenshot.html

#=============================================================================

# Mouse Functions
#=============================================================================

# Prints the resolution of your screen
print(pyautogui.size())
# Prints the current position of the mouse
print(pyautogui.position())
# Moves the mouse over time (3 seconds)
pyautogui.moveTo(100, 100, 3)
# Move the mouse relative to its current position
pyautogui.moveRel(100, 100, 3) #azaz ahol most van, ahoz képest 100-100 px 3 mp alatt jobbra

# Click
pyautogui.click(500, 500, 3, 3, button="left")
pyautogui.click(x=200, y=200)
pyautogui.click(button='right')
pyautogui.click(button='right', clicks=3, interval=0.25)
pyautogui.leftClick()
pyautogui.rightClick()
pyautogui.tripleClick()
pyautogui.doubleClick()


# Scrolls up 500
pyautogui.scroll(500)
# Scrolls down 500
pyautogui.scroll(-500)
# move mouse cursor to 100, 200, then scroll up 10 "clicks"
pyautogui.scroll(10, x=100, y=100)

# Mouse up and down
pyautogui.mouseUp(100, 100, button="left") #mint mikor leraksz egy ceruzát egy papírra majd felemeled
pyautogui.mouseDown(100, 100, button="left")

# Example of mouse up and down
pyautogui.mouseDown(300, 400, button="left")
pyautogui.moveTo(800, 400, 3)
pyautogui.mouseUp()
pyautogui.moveTo(1000, 400, 3)

#másik megoldás mouseUp|Down nélkül:

pyautogui.dragTo(100, 200, button='left') #x-y-hoz húzza a bal gombot
pyautogui.drag(30, 0, 2, button='right') #30px-el balra húzza 2mp alatt a jobbot (magyarul relatívan)

#=============================================================================

#Message Box function

alert(text='', title='', button='OK') #egy alert boxot hoz fel egy oké gombbal

confirm(text='', title='', buttons=['OK', 'Cancel']) #egy alert boxot hoz fel, több kosztüm gombbal

prompt(text='', title='' , default='') #egy promptot hoz fel, amibe lehet választ adni / kilépni belőle

password(text='', title='', default='', mask='*') #kb prompt, csak csillagozva


#=============================================================================
# Spiral drawing using pyautogui
time.sleep(1)
distance = 300
while distance > 0:
    pyautogui.dragRel(distance, 0, 1, button="left")
    distance = distance - 20
    pyautogui.dragRel(0, distance, 1, button="left")
    pyautogui.dragRel(-distance, 0, 1, button="left")
    distance = distance - 20
    pyautogui.dragRel(0, -distance, 1, button="left")
    time.sleep(4)

#=============================================================================
#example
# TikTok Liker
#=============================================================================

time.sleep(3)
# range will be the number of TikTok's you want to like
for i in range(10):
    pyautogui.moveTo(450, 500)
    time.sleep(1)
    pyautogui.doubleClick()
    time.sleep(1)
    pyautogui.moveTo(854, 515)
    time.sleep(1)
    pyautogui.leftClick()

#=============================================================================
#example
# Dino Game - Chrome
#=============================================================================

time.sleep(3)
for i in range(20):
    pyautogui.press("space")
    time.sleep(0.5)

#=============================================================================
#https://pyautogui.readthedocs.io/en/latest/keyboard.html
#=============================================================================