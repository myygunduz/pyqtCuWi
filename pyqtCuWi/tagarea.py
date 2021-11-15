#          Custom Widgets For PyQt5 Module           #
#          GPL 3.0 - myygunduz - pyqtCuWi            #
#        https://github.com/myygunduz/pyqtCuWi       #
#                      tagArea                       #

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QCompleter, QLineEdit, QScrollArea, QHBoxLayout, QPushButton
from PyQt5.QtCore import  Qt, pyqtSignal
from PyQt5.QtGui import QCursor
from .pyqtCuWiModules import  clearOfList
from .qfboxlayout import QFBoxLayout



class tagArea(QWidget):
    def __init__(self, Type:str = "oneLine"):
        super().__init__()
        self._size = (self.width(),self.height())
        self._Type = Type
        self._hintTags = []
        self._tags = []
        self._hintControl = False
        self._tagLimit = False

        self._mainLayout = QVBoxLayout()
        self._mainLayout.setContentsMargins(0,0,0,0)    
        self._mainLayout.setSpacing(0)    
        self.setLayout(self._mainLayout)

        self.completer = QCompleter(self._hintTags)
        self.entry = QLineEdit()
        self.entry.setCompleter(self.completer)
        self.entry.returnPressed.connect(self.add)
        self.entry.setPlaceholderText("Entry the tag name.")
        self._mainLayout.addWidget(self.entry)

        self.__showTags()

    def __repr__(self):
        return "<pyqtCuWi.tagArea()>"

    def __showTags(self):
        if self._Type == "oneLine":
            self.scroolbar = QScrollArea()
            self.scroolbar.setVerticalScrollBarPolicy( Qt.ScrollBarAlwaysOff )
            self.scroolbar.setContentsMargins(0,0,0,0)
            self.scroolbar.setWidgetResizable(True)

            widget = QWidget()
            self.layout = QHBoxLayout()
            widget.setLayout(self.layout)
            self.layout.setSpacing(0)
            self.layout.setContentsMargins(0,0,0,0)
            self._mainLayout.addWidget(self.scroolbar)
            self.scroolbar.setWidget(widget)
        elif self._Type == "freeBox":
            self.scroolbar = QScrollArea()
            self.scroolbar.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.scroolbar.setContentsMargins(0,0,0,0)
            self.scroolbar.setWidgetResizable(True)

            self.layout = QFBoxLayout()
            self.layout.setAlignment(Qt.TopLeftCorner)
            self.layout.setContentsMargins(0,0,0,0)
            self._mainLayout.addWidget(self.scroolbar)
            self.scroolbar.setWidget(self.layout)

    def add(self, value = None):
        if isinstance(self._tagLimit,int) and self._tagLimit > len(self._tags):
            control = True
        elif isinstance(self._tagLimit,bool): control = True
        else: 
            control = False
            self.entry.setText("Tag Limit Exceeded")
        if control:
            tagText = self.entry.text().strip() if value == None else value
            if self._hintControl:
                if tagText in self._hintTags:
                    button = customButton(tagText)
                    if self._Type == "freeBox":
                        button = customButton(tagText, parent=self.layout)
                    self.layout.addWidget(button)
            else:    
                button = customButton(tagText)
                if self._Type == "freeBox":
                    button = customButton(tagText, parent=self.layout)
                    button.clicked.connect(lambda widget: print(f'clicked the {widget}'))
                    button.clickedCloseButton.connect(self.__widgetDelete)
                
                self.layout.addWidget(button)
            self._tags.append(tagText)
            self.entry.setText("")
    def __widgetDelete(self, widget):
        self.layout.removeWidget(widget)
        self._tags.pop(self._tags.index(widget.Text()))

    def addHint(self,hintText) -> None: #list or str
        if isinstance(hintText,list):
            self._hintTags += clearOfList(hintText)
        else:
            self._hintTags.append(hintText)

        self.completer = QCompleter(self._hintTags)
        self.entry.setCompleter(self.completer)
        
    def onlyHint(self, value:bool = True) -> None:
        self._hintControl = value

    def setTagLimit(self, limitValue:int) -> None:
        self._tagLimit = limitValue

    def getTags(self) -> list:
        return self._tags

    def clearTags(self) -> None:
        self._tags = []
        self.layout.clear()
        self.entry.setText("")



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
    def Text(self):
        return self._text
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
