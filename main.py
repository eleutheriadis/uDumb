from multiprocessing.sharedctypes import Value
from PyQt6.QtWidgets import QApplication, QWidget , QPushButton, QLabel
from PyQt6.QtGui import QIcon , QFont
import sys
from random import randint

#position of No
#height 200-300
#width 220-310



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple question")
        self.setWindowIcon(QIcon("logo.ico"))
        self.setGeometry(900,200,  400,350)
        #self.setGeometry(#where to spawn app,size of the app)

        self.create_widgets()

    def create_widgets(self):
        self.btnYes = QPushButton("Yes", self)
        self.btnYes.setGeometry(40,265,80,40)
        self.btnYes.clicked.connect(self.clickedYes)
        #btnYes.setStyleSheet("background-color:grey")

        self.btnNo = QPushButton("No", self)
        self.btnNo.setGeometry(270,265,80,40)#270
        self.btnNo.clicked.connect(self.clickedNo)

        self.label = QLabel("Are u dumb?", self)
        self.label.setGeometry(40,100,400,100)
        self.label.setFont(QFont("Lato",40))
        self.label.setStyleSheet("font-weight: bold")
        #label.setStyleSheet("border: 1px solid black")

    
    def clickedNo(self):
        height = randint(200,300)
        width = randint(220,310)
        self.btnNo.setGeometry(width,height,80,40)


    def clickedYes(self):
        self.label.setText("I knew it :3")
        self.label.setGeometry(60,100,400,100)
        self.btnYes.setGeometry(500,500,80,40)
        self.btnNo.setGeometry(500,500,80,40)
        

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())