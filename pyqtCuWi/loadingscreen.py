#          Custom Widgets For PyQt5 Module           #
#          GPL 3.0 - myygunduz - pyqtCuWi            #
#        https://github.com/myygunduz/pyqtCuWi       #

from PyQt5.QtWidgets import QWidget, QDesktopWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import pyqtSignal, QUrl, Qt
from PyQt5.QtGui import QDesktopServices
from random import choice
from .pyqtCuWiModules.progressBar import ProgressBar



class loadingScreen(QWidget):
    finished = pyqtSignal()
    _qssColors={
        "dark":{
            "backgroundColor":"#212121",
            "textColor":"#FAFAFA",
            "titleFontSize":40,
            "otherFontSize":15
        },
        "light":{
            "backgroundColor":"#FAFAFA",
            "textColor":"#212121",
            "titleFontSize":40,
            "otherFontSize":15
        }
    }
    def __init__(self, appName:str, time:int=100, theme:str="dark"):
        super().__init__()
        self._appName = appName.upper()
        self._width = 640
        self._height = 480
        self._subTitleTexts = []
        self._theme = theme
        self._time = time

        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.setFixedSize(self._width,self._height)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.__widgets()
        self.__qss()
    def __widgets(self):
        self._mainLayout = QVBoxLayout()
        self._mainLayout.setContentsMargins(0,0,0,0)
        self._mainLayout.setSpacing(0)
        self.setLayout(self._mainLayout)

        self.appName = QLabel(self._appName)
        self.appName.setObjectName("appName")

        if len(self._subTitleTexts) != 0:
            text = choice(self._subTitleTexts)
        else:
            text = ""
        self.subTitle = QLabel(text)
        self.subTitle.setObjectName("subTitle")


        self.loadingBar = ProgressBar(minimum=0, maximum=self._time, textVisible=False)
        self.loadingBar.setObjectName("loadingBar")
        self.loadingBar.signal.connect(self.__loadingBarFunction)
        self.loadingBar.finished.connect(self.finished.emit)
        self.loadingBar.setFixedWidth(600)

        self.loadingText = QLabel("Loading..")
        self.loadingText.setObjectName("loadingText")

        self.developer = QLabel("Developed by Mücahit Gündüz")
        self.developer.setObjectName("developer")
        self.developer.mousePressEvent =lambda event:QDesktopServices.openUrl(QUrl("https://github.com/myygunduz"))

        self._mainLayout.addWidget(self.appName,alignment=Qt.AlignBottom|Qt.AlignCenter)
        self._mainLayout.addWidget(self.subTitle,alignment=Qt.AlignTop|Qt.AlignCenter)
        self._mainLayout.addWidget(self.loadingBar,alignment=Qt.AlignBottom|Qt.AlignCenter)
        self._mainLayout.addWidget(self.loadingText,alignment=Qt.AlignTop|Qt.AlignCenter)
        self._mainLayout.addWidget(self.developer,alignment=Qt.AlignBottom|Qt.AlignRight)

    def __loadingBarFunction(self):
        if len(self._subTitleTexts) != 0:
            changeText = choice(self._subTitleTexts)
        else:
            changeText = ""
        self.subTitle.setText(changeText)
        self.loadingText.setText("Loading." if self.loadingText.text()=="Loading.." else "Loading..")


    def __repr__(self):
        return '<pyqtCuWi.loadingScreen()>'
    
    def __qss(self):
        if self._theme != "custom":
            _colors = self._qssColors[self._theme]
            self._qssCode =(
                "QWidget{" 
                f"background-color:{_colors['backgroundColor']};" 
                f"color:{_colors['textColor']};" 
                "border:hidden;"
                "}"
                "QLabel{" 
                f"font-size:{_colors['otherFontSize']}px;" 
                "}"
                "QLabel#appName{" 
                f"font-size:{_colors['titleFontSize']}px;" 
                "}"
            )

            self.setStyleSheet(self._qssCode)

    def addSubTitle(self,subTitle:str):
        if type(subTitle) == list:
            for i in subTitle:
                self._subTitleTexts.append(i)
        elif type(subTitle) == str:
            self._subTitleTexts.append(subTitle)

    def deleteDeveloper(self):
        self.developer.deleteLater()
        self._mainLayout.addSpacing(100)

    def setAppName(self,appName:str):
        self.appName.setText(appName.upper())




