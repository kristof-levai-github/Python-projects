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



