#          Custom Widgets For PyQt5 Module           #
#          GPL 3.0 - myygunduz - pyqtCuWi            #
#        https://github.com/myygunduz/pyqtCuWi       #
#                                                    #
#                    iconButton                      #


from PyQt5.QtWidgets import QGroupBox, QHBoxLayout,QLabel, QPushButton, QWidget
from PyQt5.QtCore import pyqtSignal,Qt

from .pyqtCuWiErrors import NoIconSize, SizeError, UndefinedDirection, NoIcon


class iconButton(QPushButton):
    #Signals 
    hoverMouse = pyqtSignal(bool)
    pressMouse = pyqtSignal(bool)

    #Parameters
    def __init__(self,text:str,icon:str=None,iconSize:tuple=None,iconDirection:str='left'):
        super().__init__()
        self._text = text
        self._icon = icon
        self._iconsize = iconSize
        self._hoverIcon = None
        self._pressIcon = None
        self._iconDirection = iconDirection
        
        

        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0,0,0,0)
        self._layout.setSpacing(0)
        self.setLayout(self._layout)

        self.label = QLabel(self._text)

        self.icon = QLabel(self.__iconText(self._icon))
        

        self.__widgetsUpdate()

    def __repr__(self):
        return "<pyqtCuWi.iconButton()>"

    
    def __widgetsUpdate(self):
        self._layout.removeWidget(self.label)
        self._layout.removeWidget(self.icon)
        if self._icon != None: 
            if self._iconDirection == 'left':
                iconalign = Qt.AlignRight
                iconIndex = 0
                textalign = Qt.AlignLeft
            elif self._iconDirection == 'right':
                iconalign = Qt.AlignLeft
                iconIndex = 2
                textalign = Qt.AlignRight
            self._layout.insertWidget(1,self.label,alignment=textalign)
            self._layout.insertWidget(iconIndex,self.icon,alignment=iconalign)
            self.__checkIconSize()
        setMinimumHeight = self.icon.sizeHint().height() if self.icon.sizeHint().height()> self.label.sizeHint().height() else self.label.sizeHint().height()
        setMinimumWidth = self.icon.sizeHint().width() if self.icon.sizeHint().width()> self.label.sizeHint().width() else self.label.sizeHint().width()
        
        self.setMinimumSize(setMinimumWidth+self._iconsize[0],setMinimumHeight)

    def __checkIconSize(self):
        if self._iconsize == None and (self._icon !=None or self._hoverIcon != None or self._pressIcon!=None):
            raise NoIconSize()

    def __iconText(self,icon):
        self.__checkIconSize()
        return f"<html><img src='{icon}'width='{self._iconsize[0]}' height='{self._iconsize[1]}'></html>" if icon != None else ""

    
    #Get methods
    def getText(self):
        return self._text
    
    def getIcons(self):
        return {'manualIcon':self._icon,'hoverIcon':self._hoverIcon,'pressIcon':self._pressIcon}

    #Set methods
    def setText(self,text:str):
        self._text = text
        self.label.setText(self._text)
        

    def setIcon(self,filepath:str):
        self._icon = filepath
        self.icon.setText(self.__iconText(self._icon))
        self.__widgetsUpdate()

    def setHoverIcon(self,filepath:str):
        self._hoverIcon = filepath
        self.__widgetsUpdate()


    def setPressIcon(self,filepath:str):
        self._pressIcon = filepath
        self.__widgetsUpdate()


    def setIconSize(self,size:tuple):
        if self._icon == None and self._hoverIcon == None and self._pressIcon == None:
            raise NoIcon("No icon you can't set size")
        width = size[0]
        height = size[1]
        if self.width() < width : raise SizeError(self.width(),width)
        elif self.height() < height : raise SizeError(self.height(),height)
        else:
            self._iconsize = (width,height)
            self.icon.setText(self.__iconText(self._icon))
            self.__widgetsUpdate()

    def setIconDirection(self, direction:str):
        if self._icon == None and self._hoverIcon == None and self._pressIcon == None:
            raise NoIcon("No icon you can't specify direction")
        if direction != 'left' and direction != 'right':
            raise UndefinedDirection()
        self._iconDirection = direction
        self.__widgetsUpdate()

    def enterEvent(self, event):
        if self._hoverIcon != None:
            self.icon.setText(self.__iconText(self._hoverIcon))
        self.hoverMouse.emit(True)

    def leaveEvent(self,event):
        if self._hoverIcon != None:
            self.icon.setText(self.__iconText(self._icon))
        self.hoverMouse.emit(False)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self._pressIcon != None:
                self.icon.setText(self.__iconText(self._pressIcon))
            self.pressMouse.emit(True)
