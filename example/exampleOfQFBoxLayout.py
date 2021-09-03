#          Custom Widgets For PyQt5 Module           #
#          GPL 3.0 - myygunduz - pyqtCuWi            #
#        https://github.com/myygunduz/pyqtCuWi       #

from PyQt5.QtWidgets import QApplication,QWidget, QVBoxLayout, QLineEdit, QScrollArea, QHBoxLayout, QPushButton
from PyQt5.QtCore import  Qt, pyqtSignal
from PyQt5.QtGui import QCursor
from pyqtCuWi import QFBoxLayout

def clearOfList(InputList:list) -> list :
    Output = []
    def operation(lista:list):
        for i in lista:
            if isinstance(i,list):
                operation(i)
            else:
                Output.append(i)
    operation(InputList)
    return Output

class tagArea(QWidget):
    def __init__(self):
        super().__init__()

        self._mainLayout = QVBoxLayout()
        self._mainLayout.setContentsMargins(0,0,0,0)    
        self._mainLayout.setSpacing(0)    
        self.setLayout(self._mainLayout)

        self.entry = QLineEdit()
        self.entry.returnPressed.connect(self.__add)
        self.entry.setPlaceholderText("Entry the tag name.")
        self._mainLayout.addWidget(self.entry)

        self.__showTags()

    def __showTags(self):
        self.scroolbar = QScrollArea()
        self.scroolbar.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroolbar.setContentsMargins(0,0,0,0)
        self.scroolbar.setWidgetResizable(True)

        self.layout = QFBoxLayout()
        self.layout.setAlignment(Qt.TopLeftCorner)
        self.layout.setContentsMargins(0,0,0,0)
        self._mainLayout.addWidget(self.scroolbar)
        self.scroolbar.setWidget(self.layout)

    def __add(self):

        button = customButton(self.entry.text().strip(), parent=self.layout)

        button.clicked.connect(lambda widget: print(f'clicked the {widget}'))
        button.clickedCloseButton.connect(lambda widget:self.layout.deleteWidget(widget))
        
        self.layout.addWidget(button)

class customButton(QWidget):
    clickedCloseButton = pyqtSignal(object)
    clicked = pyqtSignal(object)
    def __init__(self, text, parent = None):
        QWidget.__init__(self, parent=parent)
        self.setMinimumWidth(60)
        self._text = text
        self._layout = QHBoxLayout()
        self._layout.setSpacing(0)
        self._layout.setContentsMargins(0,0,0,0)
        self.setLayout(self._layout)

        self.text = QPushButton("    "+self._text)
        self.text.setCursor(QCursor(Qt.PointingHandCursor))
        self.text.setObjectName("text")
        self.text.setFixedHeight(30)
        self.text.clicked.connect(self.__clickedButton)

        self._layout.addWidget(self.text)

        self.closeButton = QPushButton("✕")
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeButton.setObjectName("closeButton")
        self.closeButton.clicked.connect(lambda: self.__clickedButton(isCloseButton=True))
        self.closeButton.setFixedSize(40,30)

        self._layout.addWidget(self.closeButton)
        self.__qss()
    def __clickedButton(self, isCloseButton = False):
        self.clicked.emit(self)
        if isCloseButton:
            self.clickedCloseButton.emit(self)

    def enterEvent(self, event):
        self.setStyleSheet("""
        QWidget{
            background-color: rgb(255, 56, 122);
            border: 3px solid rgb(186, 13, 71);
            color: rgb(251, 249, 250);
        }
        QPushButton#text{
            border-top-left-radius:15px;
            border-bottom-left-radius:15px;
            border-right:0px;
        }
        QPushButton#closeButton{
            border-top-right-radius:15px;
            border-bottom-right-radius:15px;
            border-left:0px;
        }
        """)

    def leaveEvent(self, event):
        self.setStyleSheet("""
        QPushButton{
            background-color: rgb(253, 0, 84);
            border: 3px solid rgb(168, 0, 56);
            color: rgb(251, 249, 250);
        }
        QPushButton#text{
            border-top-left-radius:15px;
            border-bottom-left-radius:15px;
            border-right:0px;
        }
        QPushButton#closeButton{
            border-top-right-radius:15px;
            border-bottom-right-radius:15px;
            border-left:0px;
        }

        """)
    def __qss(self):
        self.setStyleSheet("""
        QPushButton{
            background-color: rgb(253, 0, 84);
            border: 3px solid rgb(168, 0, 56);
            color: rgb(251, 249, 250);
        }
        QPushButton:hover{
            background-color: rgb(255, 56, 122);
        }
        QPushButton#text{
            border-top-left-radius:15px;
            border-bottom-left-radius:15px;
            border-right:0px;
        }
        QPushButton#closeButton{
            border-top-right-radius:15px;
            border-bottom-right-radius:15px;
            border-left:0px;
        }

        """)

if __name__ == '__main__':
    app = QApplication([])
    tagArea = tagArea()
    tagArea.show()
    app.exec_()