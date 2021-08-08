#          Custom Widgets For PyQt5 Module           #
#          GPL 3.0 - myygunduz - pyqtCuWi            #
#        https://github.com/myygunduz/pyqtCuWi       #
#                                                    #
#                    rankWidget                      #

from PyQt5.QtWidgets import QScrollArea, QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import pyqtSignal, Qt

from pyqt5Custom import StyledButton

from .pyqtCuWiErrors import InvalidLayoutType, InvalidButtonType, InvalidValueType, TupleSizeError, InvalidButtonStyleType

from pathlib import Path


class rankWidget(QScrollArea):
    clickedButton = pyqtSignal(object)
    deleteButton = pyqtSignal(object)
    def __init__(self,main,layout_type:str='V'):
        super().__init__()
        self._main = main
        self._groupboxs = {}
        self._buttons = []
        self._layout_type = layout_type.upper()
        self.groupbox = QWidget()
        self.setWidgetResizable(True)
        self.setWidget(self.groupbox)
        if self._layout_type == 'H' or self._layout_type == 'V':
            self.layout = QVBoxLayout() if self._layout_type == "V" else QHBoxLayout()
            self.layout.setSpacing(0)
            self.layout.setContentsMargins(0,0,0,0)
            self.groupbox.setLayout(self.layout)
        else:
            raise InvalidLayoutType()
        
        self._main.resizeEvent = lambda a: self.setMaximumSize(self._main.width(),self._main.height())


        self._Qss = (
            'QWidget#widget{'
            'background-color: rgba(0,0,0,0);'
            'border: 1px solid rgb(255,255,255)'
            '}'
            
            'QLabel{'
            'background-color:rgba(0,0,0,0);'
            'border: 1px solid rgba(255,255,255,0);'
            'color:rgb(0,0,0);'
            '}'
        )
        self._QssHover = (
            'QWidget {'
            'background-color: rgba(0,0,0,0);'
            '}'
        )
        self._QssPress = (
            'QWidget {'
            'background-color: rgba(0,0,0,0);'
            '}'
        )
        self._QssDict = (({
            'background-color':(0,0,0,0),
            'border-color' : (0,0,0,0),
            'border-size':0
        },))
        self._QssDictHover = (({
            'background-color':(0,0,0,0),
            'border-color' : (0,0,0,0),
            'border-size':0
        },'hover'))
        self._QssDictPress = (({
            'background-color':(0,0,0,0),
            'border-color' : (0,0,0,0),
            'border-size':0
        },'press'))
        parent = Path(__file__).parent

        self._rightArrow = str(Path(parent, 'pyqtCuWiAssets', 'right.png'))
        self._leftArrow = str(Path(parent, 'pyqtCuWiAssets', 'left.png'))
        self._upArrow = str(Path(parent, 'pyqtCuWiAssets', 'up.png'))
        self._downArrow = str(Path(parent, 'pyqtCuWiAssets', 'down.png'))
        self._trash = str(Path(parent, 'pyqtCuWiAssets', 'trash.png'))

        self._hideButton = True

    def gettext(self,widget:object):
        return widget['text'].text()

    def sethidebutton(self,value:bool):
        if isinstance(value,bool):
            if value == None:
                self._hideButton = True
            else:
                self._hideButton = value
        else:
            raise InvalidValueType()

    def seticon(self,filepath:str,buttonType:str):
        if buttonType == 'rightArrow':self._rightArrow = filepath
        elif buttonType == 'leftArrow':self._leftArrow = filepath
        elif buttonType == 'upArrow':self._upArrow = filepath
        elif buttonType == 'downArrow':self._downArrow = filepath
        elif buttonType == 'trash':self._trash = filepath
        else: raise InvalidButtonType()


    def setstyledict(self, stylecode:tuple):
        if len(stylecode) >2:
            raise TupleSizeError(2)
        if len(stylecode) == 2 and stylecode[1] not in ['press','hover','default']: 
            raise InvalidButtonStyleType
        if len(stylecode) == 2:
            if 'hover' == stylecode[1]:
                self._QssDictHover=stylecode
            elif 'press' == stylecode[1]:
                self._QssDictPress=stylecode
            elif 'default' == stylecode[1]:self._QssDict=stylecode
        else:
            self._QssDict=stylecode

        for i in self._buttons:
            try:
                i.upButton.upButton.setStyleDict(stylecode[0],stylecode[1] if len(stylecode) != 1 else 'default')
                i.downButton.downButton.setStyleDict(stylecode[0],stylecode[1] if len(stylecode) != 1 else 'default')
                i.closeButton.closeButton.setStyleDict(stylecode[0],stylecode[1] if len(stylecode) != 1 else 'default')
            except IndexError:
                pass
    def setstylesheet(self, stylecode:tuple):
        if len(stylecode) >2:
            raise TupleSizeError(2)
        if 'QWidget' in stylecode[0]:
            stylecode = list(stylecode)
            stylecode[0]=stylecode[0].replace('QWidget','QWidget#widget')
            stylecode = tuple(stylecode)
        if len(stylecode) == 2:
            if 'hover' == stylecode[1]:
                self._QssHover=stylecode[0]
            elif 'press' == stylecode[1]:
                self._QssPress=stylecode[0]
            elif 'default' == stylecode[1]:
                self._Qss=stylecode[0]
        else:
            self._Qss=stylecode[0]

        for i in self._buttons:
            try:
                self._groupboxs[i]['mainWidget'].setStyleSheet(stylecode[0])
            except IndexError:
                pass

    def addbutton(self,text:str):
        if len(text) == 0:
            return
        self.__createButton(text)

    def __createButton(self,text,index=None):
        buttonWidget = QWidget()
        buttonWidget.setObjectName('widget')
        #buttonWidget.enterEvent = lambda event: buttonWidget.setStyleSheet(self._QssHover)
        #buttonWidget.leaveEvent = lambda event: buttonWidget.setStyleSheet(self._Qss)

        buttonLayout = QVBoxLayout() if self._layout_type == "H" else QHBoxLayout()
        buttonWidget.setLayout(buttonLayout)
        
        buttonText = QLabel(text)
        buttonLayout.addWidget(buttonText)

        upAndDownButton = self.upAndDownButton(main=self,layout_type='H' if self._layout_type == 'H' else 'V')
        upAndDownButton.upSignal.connect(lambda widget: self.__movement(widget,'up'))

        upAndDownButton.downSignal.connect(lambda widget: self.__movement(widget,'down'))

        upAndDownButton.deleteSignal.connect(lambda widget: self.__deleteWidget(widget))

        buttonInfoDict = {
            'mainWidget':buttonWidget,
            'textWidget':buttonText,
            'buttonWidget' : upAndDownButton,
            'text':buttonText.text()
        
        }

        self._groupboxs[upAndDownButton] = buttonInfoDict

        buttonLayout.addWidget(upAndDownButton,alignment=Qt.AlignRight if self._layout_type =='V' else Qt.AlignBottom)

        if index == None: 
            self.layout.addWidget(buttonWidget)
            self._buttons.append(upAndDownButton)
        else: 
            self.layout.insertWidget(index,buttonWidget)
            self._buttons.insert(index,upAndDownButton)

        buttonWidget.setStyleSheet(self._Qss)
        self.setstyledict(self._QssDict)

        buttonWidget.mouseReleaseEvent= lambda event: self.clickedButton.emit(self._groupboxs[upAndDownButton])

    def __deleteWidget(self,widget):

        index = self._buttons.index(widget)
        self._buttons.pop(index)
        buttonInfo = self._groupboxs[widget]
        buttonWidget = buttonInfo['mainWidget']
        self.layout.removeWidget(buttonWidget)
        del self._groupboxs[widget]

        self.deleteButton.emit(buttonInfo)

    def __movement(self,widget,direction):
        index = self._buttons.index(widget)
        self._buttons.pop(index)
        if direction == 'up': index-=1
        else: index+=1
        if index<0: index=0
        buttonInfo = self._groupboxs[widget]
        buttonWidget = buttonInfo['mainWidget']
        buttonText = buttonInfo['text']
        del self._groupboxs[widget]
        self.layout.removeWidget(buttonWidget)
        self.__createButton(buttonText,index)
        
    def __repr__(self):
        return "<myygunduz.rankWidget()>"
    
    class upAndDownButton(QWidget):
        upSignal = pyqtSignal(object)

        downSignal = pyqtSignal(object)

        deleteSignal = pyqtSignal(object)
        def __init__(self,main,layout_type):
            super().__init__()
            self._main = main
            self._layout_type = layout_type

            self.mainLayout = QHBoxLayout() if self._layout_type != 'H' else QVBoxLayout()
            self.mainLayout.setSpacing(0)
            self.mainLayout.setContentsMargins(0,0,0,0)
            self.setLayout(self.mainLayout)

            self.layout = QHBoxLayout() if self._layout_type == 'H' else QVBoxLayout()
            self.layout.setAlignment(Qt.AlignCenter)
            self.layout.setSpacing(0)
            self.layout.setContentsMargins(0,0,0,0)

            self.upButton = self.upWidget(self._main)
            self.upButton.rightButton.connect(self.Signals)
            self.layout.addWidget(self.upButton)


            self.downButton = self.downWidget(self._main)
            self.downButton.rightButton.connect(self.Signals)
            self.layout.addWidget(self.downButton)

            self.mainLayout.addLayout(self.layout)

            self.closeButton = self.closeWidget(self._main)
            self.closeButton.closeOperation.connect(self.Signals)
            self.mainLayout.addWidget(self.closeButton)

        def Signals(self,direction):
            if isinstance(direction,str):
                if direction == "up":
                    self.upSignal.emit(self)
                else:
                    self.downSignal.emit(self)
            else:
                self.deleteSignal.emit(self)
            


        class upWidget(QWidget):
            rightButton = pyqtSignal(str)
            def __init__(self,main):
                super().__init__()
                self._main = main

                self.layout = QVBoxLayout()
                self.layout.setSpacing(0)
                self.layout.setContentsMargins(0,0,0,0)
                self.setLayout(self.layout)

                self.upButton = StyledButton()
                if self._main._hideButton == False: self.upButton.setIcon(self._main._upArrow if self._main._layout_type == 'V' else self._main._leftArrow)
                self.upButton.setFixedSize(30,30)

                self.layout.addWidget(self.upButton)

            def enterEvent(self, event):
                if self._main._hideButton == True:
                    self.upButton.setIcon(self._main._upArrow if self._main._layout_type == 'V' else self._main._leftArrow)
                    self.upButton.setIconSize(30,30)
                    self.upButton.setStyleDict(self._main._QssDict[0])
                    self.upButton.setStyleDict(self._main._QssDictHover[0],self._main._QssDictHover[1])
                    self.upButton.setStyleDict(self._main._QssDictPress[0],self._main._QssDictPress[1])

            def leaveEvent(self, event):
                if self._main._hideButton == True:
                    self.upButton.deleteLater()
                    self.upButton = StyledButton()        
                    self.upButton.setFixedSize(30,30)
                    self.layout.addWidget(self.upButton)
                    self.upButton.setStyleDict(self._main._QssDict[0])
                    self.upButton.setStyleDict(self._main._QssDictHover[0],self._main._QssDictHover[1])


            def mousePressEvent(self, QMouseEvent):
                if QMouseEvent.button() == 2:
                    self.rightButton.emit("up")

        class downWidget(QWidget):
            rightButton = pyqtSignal(str)
            def __init__(self,main):
                super().__init__()
                self._main = main
                self.layout = QVBoxLayout()
                self.layout.setSpacing(0)
                self.layout.setContentsMargins(0,0,0,0)
                self.setLayout(self.layout)

                self.downButton = StyledButton()
                if self._main._hideButton == False: self.downButton.setIcon(self._main._downArrow if self._main._layout_type == 'V' else self._main._rightArrow)
                self.downButton.setFixedSize(30,30)
                self.layout.addWidget(self.downButton)

            def enterEvent(self, event):
                if self._main._hideButton == True:
                    self.downButton.setIcon(self._main._downArrow if self._main._layout_type == 'V' else self._main._rightArrow)
                    self.downButton.setIconSize(30,30)
                    self.downButton.setStyleDict(self._main._QssDict[0])
                    self.downButton.setStyleDict(self._main._QssDictHover[0],self._main._QssDictHover[1])
                    self.downButton.setStyleDict(self._main._QssDictPress[0],self._main._QssDictPress[1])


            
            def leaveEvent(self, event):
                if self._main._hideButton == True:
                    self.downButton.deleteLater()
                    self.downButton = StyledButton()
                    self.downButton.setFixedSize(30,30)
                    self.layout.addWidget(self.downButton)
                    self.downButton.setStyleDict(self._main._QssDict[0])
                    self.downButton.setStyleDict(self._main._QssDictHover[0],self._main._QssDictHover[1])



            def mousePressEvent(self, QMouseEvent):
                if QMouseEvent.button() == 2:
                    self.rightButton.emit("down")

        class closeWidget(QWidget):
            closeOperation = pyqtSignal(bool)
            def __init__(self,main):
                super().__init__()
                self._main = main
                self.layout = QVBoxLayout()
                self.layout.setSpacing(0)
                self.layout.setContentsMargins(0,0,0,0)
                self.layout.setAlignment(Qt.AlignCenter)
                self.setLayout(self.layout)

                self.closeButton = StyledButton()
                if self._main._hideButton == False: self.closeButton.setIcon(self._main._trash)
                self.closeButton.setFixedSize(30,30)
                self.layout.addWidget(self.closeButton)

            def enterEvent(self, event):
                if self._main._hideButton == True:
                    self.closeButton.setIcon(self._main._trash)
                    self.closeButton.setIconSize(30,30)
                    self.closeButton.setStyleDict(self._main._QssDict[0])
                    self.closeButton.setStyleDict(self._main._QssDictHover[0],self._main._QssDictHover[1])
                    self.closeButton.setStyleDict(self._main._QssDictPress[0],self._main._QssDictPress[1])


            def leaveEvent(self, event):
                if self._main._hideButton == True:
                    self.closeButton.deleteLater()
                    self.closeButton = StyledButton()
                    self.closeButton.setFixedSize(30,30)
                    self.layout.addWidget(self.closeButton)
                    self.closeButton.setStyleDict(self._main._QssDict[0])
                    self.closeButton.setStyleDict(self._main._QssDictHover[0],self._main._QssDictHover[1])

            def mousePressEvent(self, QMouseEvent):
                if QMouseEvent.button() == 2:
                    self.closeOperation.emit(True)



