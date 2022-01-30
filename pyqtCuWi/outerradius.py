#          Custom Widgets For PyQt5 Module           #
#          GPL 3.0 - myygunduz - pyqtCuWi            #
#        https://github.com/myygunduz/pyqtCuWi       #
#                                                    #
#                    outerRadius                     #

from PyQt5.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt, QSize

from .pyqtCuWiErrors import TupleSizeError, pyqtCuWiInvaledType

class outerRadius(QWidget):
    _qssInfo = {
        'interiorColor':(43, 43, 43), 
        'exteriorColor':(33, 33, 33),
        'radius':20
    }
    _extraQss ={'default':"",'hover':"",'press':""}

    def __init__(self, widget:QWidget = QLineEdit, direction:str = 'left', width:int = 300, height:int = 150,objectName:str = 'widget'):
        super().__init__()
        self._objectName = objectName
        self._widgetName = str(widget).split('.')[-1].split("'")[0]
        self.widget = widget()
        self.widget.setObjectName(self._objectName)
        if direction in ['left','right','up','down']: self._direction = direction
        else: raise pyqtCuWiInvaledType("Direction",direction,['left','right','up','down'])
        self._width = width
        self._height = height
        self._layoutType = QVBoxLayout if self._direction != 'up' and self._direction != 'down' else QHBoxLayout

        self._layout = self._layoutType()
        self.__AlignmentDef(self._layout)
        self._layout.setSpacing(0)
        self._layout.setContentsMargins(0,0,0,0)

        self._mainWidget = QWidget()
        self._mainWidget.setFixedSize(QSize(int(self._width*0.3),self._height) if self._direction == 'left' or self._direction == 'right' else QSize(self._width,int(self._height*0.3)))
        self._mainWidget.setObjectName('mainWidget')

        self._layout.addWidget(self._mainWidget,alignment = Qt.AlignLeft)

        self._mainLayout = self._layoutType()
        self.__AlignmentDef(self._mainLayout)
        self._mainLayout.setSpacing(0)
        self._mainLayout.setContentsMargins(0,0,0,0)

        self._mainWidget.setLayout(self._mainLayout)

        self.setFixedSize(self._width,self._height)
        self.setLayout(self._layout)
        self.__widgets()
        self.__Qss(extraQss=self._extraQss)
    def __repr__(self):
        return '<pyqtCuWi.outerRadius()>'

    def __AlignmentDef(self,widgetOrLayout):
        if self._direction == 'left':widgetOrLayout.setAlignment(Qt.AlignLeft) 
        elif self._direction == 'right':widgetOrLayout.setAlignment(Qt.AlignRight)
        elif self._direction == 'up':widgetOrLayout.setAlignment(Qt.AlignTop)
        elif self._direction == 'down':widgetOrLayout.setAlignment(Qt.AlignBottom)
            
    def __widgets(self):
        self._up = QLabel()
        self._up.setObjectName('up')
        self.__AlignmentDef(self._up)
        self._up.setFixedSize(int(self._width*0.3),int(self._height*0.3))

        self._down = QLabel()
        self._down.setObjectName('down')
        self.__AlignmentDef(self._down)
        self._down.setFixedSize(int(self._width*0.3),int(self._height*0.3))

        self._right = QLabel()
        self._right.setObjectName('right')
        self.__AlignmentDef(self._right)
        self._right.setFixedSize(int(self._width*0.3),self._height)

        self._left = QLabel()
        self._left.setObjectName('left')
        self.__AlignmentDef(self._left)
        self._left.setFixedSize(int(self._width*0.3),self._height)


        condition = self._direction == 'up' or self._direction == 'down'
        self._mainLayout.addWidget(self._left if condition else self._up)
        self._mainLayout.addSpacing(int(self._height*0.4) if not condition else int(self._width*0.4)) 
        self._mainLayout.addWidget(self._right if condition else self._down)

        self.__Widget()

    def __Widget(self):
        widget = QWidget(self)
        widget.setObjectName('widget')
        layout = self._layoutType()
        layout.setSpacing(0)
        layout.setContentsMargins(0,0,0,0)
        widget.setLayout(layout)

        layout.addWidget(self.widget)

        if self._direction == 'left' or self._direction == 'right': 
            widget.setFixedSize(self._width,int(self._height*0.4))
            self.widget.setFixedSize(self._width,int(self._height*0.4))
        elif self._direction == 'up' or self._direction == 'down': 
            widget.setFixedSize(int(self._width*0.4)+4,self._height)
            self.widget.setFixedSize(int(self._width*0.4)+4,self._height)

        if self._direction == 'left': x,y = 0,int(self._height*0.3)
        elif self._direction == 'right': x,y = 0,int(self._height*0.3)
        elif self._direction == 'up': x,y = int(self._width*0.3)-2,0
        elif self._direction == 'down': x,y = int(self._width*0.3)-2,0
        widget.move(x,y)

        widget.raise_()
        
    def __Qss(self,extraQss):
        if self._direction == 'left': widgetRadiusOne, widgetRadiusTwo = 'border-top-right-radius','border-bottom-right-radius',
        elif self._direction == 'right': widgetRadiusOne, widgetRadiusTwo = 'border-top-left-radius','border-bottom-left-radius',
        elif self._direction == 'up': widgetRadiusOne, widgetRadiusTwo = 'border-bottom-left-radius','border-bottom-right-radius',
        elif self._direction == 'down': widgetRadiusOne, widgetRadiusTwo = 'border-top-left-radius','border-top-right-radius',
        
        qss = (
            "QWidget{"
            f"background-color:rgb{self._qssInfo['exteriorColor']};"
            "}"
            "QWidget#mainWidget{"
            f"background-color:rgb{self._qssInfo['interiorColor']};"
            "}"
            "QWidget#widget{"
            f"background-color:rgb{self._qssInfo['interiorColor']};"
            f"{widgetRadiusOne}:{self._qssInfo['radius']}px;"
            f"{widgetRadiusTwo}:{self._qssInfo['radius']}px;"
            "}"
            f"{self._widgetName}#{self._objectName}" "{"
            "background-color:rgba(0,0,0,0);"
            "border:hidden;"
            f"{widgetRadiusOne}:{self._qssInfo['radius']}px;"
            f"{widgetRadiusTwo}:{self._qssInfo['radius']}px;"
            f"{extraQss['default']}"
            "}"
            f"{self._widgetName}#{self._objectName}" ":hover{"
            f"{extraQss['hover']}"
            "}"
            f"{self._widgetName}#{self._objectName}" ":pressed{"
            f"{extraQss['press']}"
            "}"
            "QLabel#up{"
            "border:hidden;"
            f"background-color:rgb{self._qssInfo['exteriorColor']};"
            f"border-bottom:1px solid rgb{self._qssInfo['exteriorColor']};"
            f"border-left:1px solid rgb{self._qssInfo['exteriorColor']};"
            f"border-bottom-{self._direction}-radius:{self._qssInfo['radius']}px;"
            "}"
            "QLabel#down{"
            "border:hidden;"
            f"background-color:rgb{self._qssInfo['exteriorColor']};"
            f"border-top:1px solid rgb{self._qssInfo['exteriorColor']};"
            f"border-left:1px solid rgb{self._qssInfo['exteriorColor']};"
            f"border-top-{self._direction}-radius:{self._qssInfo['radius']}px;"
            "}"
            "QLabel#left{"
            "border:hidden;"
            f"background-color:rgb{self._qssInfo['exteriorColor']};"
            f"border-{'bottom' if self._direction == 'down' else 'top'}:1px solid rgb{self._qssInfo['exteriorColor']};"
            f"border-right:0px solid rgb{self._qssInfo['exteriorColor']};"
            f"border-{'bottom' if self._direction == 'down' else 'top'}-right-radius:{self._qssInfo['radius']}px;"
            "}"
            "QLabel#right{"
            "border:hidden;"
            f"background-color:rgb{self._qssInfo['exteriorColor']};"
            f"border-{'bottom' if self._direction == 'down' else 'top'}:1px solid rgb{self._qssInfo['exteriorColor']};"
            f"border-left:0px solid rgb{self._qssInfo['exteriorColor']};"
            f"border-{'bottom' if self._direction == 'down' else 'top'}-left-radius:{self._qssInfo['radius']}px;"
            "}"
        )
        self.setStyleSheet(qss)

    def addWidgetQss(self,qssCode:str,Type:str = 'default',objectName:str = 'widget'):
        if Type not  in ['default','hover','press']: raise pyqtCuWiInvaledType("Style",Type,['default','hover','press'])
        self._extraQss[Type] = qssCode
        self._objectName = objectName
        self.__Qss(extraQss=self._extraQss)
    
    def changeDefaultQss(self,qssCode:dict):
        for i in qssCode:
            if i in self._qssInfo.keys():
                if i == 'radius' and type(qssCode[i]) != int:
                    raise pyqtCuWiInvaledType("Value",qssCode[i],[int])
                elif i != 'radius' and type(qssCode[i]) != tuple:
                    raise pyqtCuWiInvaledType("Value",qssCode[i],[tuple])
                elif i != 'radius' and len(qssCode[i]) != 3:
                    raise TupleSizeError(3,outerRadius=True)
                self._qssInfo[i] = qssCode[i]
            else:
                raise  pyqtCuWiInvaledType("Style",i,self._qssInfo.keys())
        
        self.__Qss(extraQss=self._extraQss)