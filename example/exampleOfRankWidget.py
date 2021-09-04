from PyQt5.QtWidgets import QLineEdit, QWidget, QVBoxLayout, QApplication, QLabel
from pyqtCuWi import rankWidget
import os
class main(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Example Of Rank Widget')
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.inputWidget = QLineEdit()
        self.inputWidget.setPlaceholderText("Enter text and press 'enter'.")
        self.inputWidget.returnPressed.connect(lambda: self.addbutton(self.inputWidget.text()))

        self.scroolBar = rankWidget(self,'V')
        self.scroolBar.sethidebutton(False)
        self.scroolBar.setstyledict(({
            'background-color':(255,0,0),
            'border-color':(0,0,0,0)
        },'default'))

        self.scroolBar.setstylesheet((
            "QWidget{" 
            "background-color:rgb(0,255,0);"
            "}",)
        )
        self.scroolBar.clickedButton.connect(self.isClicked)
        self.scroolBar.deleteButton.connect(self.isDeleted)

        self.layout.addWidget(self.inputWidget)
        self.layout.addWidget(self.scroolBar)
    def isClicked(self,widgets):
        print(widgets)
    
    def isDeleted(self,widgets):
        print(widgets)
        
    def addbutton(self,text):
        self.scroolBar.addbutton(text)
app = QApplication([])
main = main()
main.show()
app.exec_()
