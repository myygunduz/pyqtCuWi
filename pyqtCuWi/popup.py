#          Custom Widgets For PyQt5 Module           #
#          GPL 3.0 - myygunduz - pyqtCuWi            #
#        https://github.com/myygunduz/pyqtCuWi       #
#                                                    #
#                       popUp                        #
from PyQt5.QtWidgets import (QWidget, 
                                QLabel, 
                                QVBoxLayout, 
                                QHBoxLayout, 
                                QScrollArea, 
                                QPushButton,
                                QGroupBox)
from PyQt5.QtCore import pyqtSignal, QSize, Qt
from pyqt5Custom import ImageBox

from .pyqtCuWiModules import readJ,writeJ

from .pyqtCuWiErrors import InvalidStyleVariable, InvalidThemeType, InvalidTitleType, FailedToAddTitleType

from pathlib import Path
class popUp(QWidget):
    closed = pyqtSignal(bool)
    clickedContent = pyqtSignal(dict)

    _subTitle = []
    _customQssThemplate = {
        'background-color':(33, 33, 33), 
        'text-color':(250, 250, 250),
        'font-family':'Times',
        'font-size':15,
        'title-background-color':(43, 43, 43),
        'title-font-size':20,
        'sub-title-font-size':18,
        'icon-font-size':20,

        'button-hover-color':(255, 0, 0),
        'scrollBar-background-color':(33, 33, 33),
        'scrollBar-foreground-color':(43, 43, 43),
        'subWidget-background-color':(43, 43, 43)}
    _customTitleType = {
        'append':(80, 216, 144),
        'warning':(218, 0, 55),
        'information':(253, 184, 39)
    }
    def __init__(self,parent,title:str = None,img:str = None,themeType:str = 'dark'):
        super().__init__(parent)
        self._parent = parent
        self._title = title
        self._img = img
        self._width = 650
        self._height = 800
        self._themeType = themeType
        self.setFixedSize(self._width,self._height)
        self.setObjectName('popUp')
        
        self._parent.setMinimumSize(self._width+10,self._height+10)


        setattr(self, "mousePressEvent",   self.mousePressEvent)
        setattr(self, "mouseMoveEvent",    self.mouseMoveEvent)
        setattr(self, "mouseReleaseEvent", self.mouseReleaseEvent)

        self.blockingWindow = QLabel(self._parent)
        self.blockingWindow.setStyleSheet("background-color: rgba(128, 128, 128,90);")
        self.blockingWindow.setFixedSize(QSize(self._parent.width(),self._parent.height()))
        self.blockingWindow.show()
        self.blockingWindow.raise_()
        self.raise_()
        
        self.move(int(self._parent.width()/2-self.width()/2),int(self._parent.height()/2-self.height()/2))

        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0,0,0,0)
        self._layout.setAlignment(Qt.AlignCenter)
        self._layout.setSpacing(0)
        self.setLayout(self._layout)

        self._mainWidget = QWidget()
        self.qssMainWidget = self._mainWidget
        self._mainWidget.setObjectName('mainWidget')
        self._mainLayout = QVBoxLayout()
        self._mainLayout.setAlignment(Qt.AlignCenter)
        self._mainLayout.setContentsMargins(0,0,0,0)
        self._mainLayout.setSpacing(0)
        self._mainWidget.setLayout(self._mainLayout)

        self._mainScrollArea = QScrollArea()
        self._mainScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self._mainScrollArea.setObjectName('mainScrollArea')
        self._mainScrollArea.setContentsMargins(0,0,0,0)
        self._mainScrollArea.setWidget(self._mainWidget)
        self._mainScrollArea.setWidgetResizable(True)

        self.__widgets()

        self._subWidget = QWidget()
        self._subWidget.setObjectName('subWidget')
        self._subWidget.setFixedSize(self._width,50)
        self.subLayout = QHBoxLayout()
        self.subLayout.setContentsMargins(0,0,0,0)
        self.subLayout.setSpacing(0)
        self._subWidget.setLayout(self.subLayout)
        self._layout.addWidget(self._subWidget)

        self.setThemeType(self._themeType)
    def __repr__(self):
        return '<pyqtCuWi.popUp()>'
    
    def __widgets(self):
        self._titleWidget = QWidget()
        self._titleWidget.setObjectName('titleWidget')
        self._titleWidget.setFixedSize(self._width,50)
        self._titleLayout = QHBoxLayout()
        self._titleLayout.setSpacing(0)
        self._titleLayout.setContentsMargins(10,0,0,0)
        self._titleWidget.setLayout(self._titleLayout)



        self._titleTextLayout = QVBoxLayout()
        self._titleTextLayout.setContentsMargins(0,0,0,0)
        self._titleTextLayout.setSpacing(0)
        self.title = QLabel(self._title.title() if self._title != None else'')
        self.title.setObjectName('mainTitle')

        self.subTitle = QLabel("")
        self.subTitle.hide()
        self.subTitle.setObjectName('subTitle')

        
        self._titleTextLayout.addWidget(self.title)
        self._titleTextLayout.addWidget(self.subTitle,alignment=Qt.AlignTop)
        self._titleTextLayout.setContentsMargins(0,5,0,0)
        self._titleLayout.addLayout(self._titleTextLayout)
        

        self.clsButton = QPushButton("✕")
        self.clsButton.setFixedSize(QSize(self._titleWidget.height(),self._titleWidget.height()))
        self.clsButton.setObjectName("clsButton")
        self.clsButton.clicked.connect(self.__close)
        self._titleLayout.addWidget(self.clsButton)

        self._layout.addWidget(self._titleWidget)

        if self._img != None:
            self.image = ImageBox(source=self._img)
            self.image.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.image.setFixedWidth(self._width-20)
            self._mainLayout.addSpacing(20)
            self._mainLayout.addWidget(self.image)
            self._mainLayout.addSpacing(20)

        self._layout.addWidget(self._mainScrollArea)

    def __Qss(self,titleType=None,mode='dark',noneControl = False):
        qssCodesClass = self._qssCodes(self)
        if mode == 'dark' or mode == 'light': return qssCodesClass.defaultQss(colorMode='darkMode' if mode == 'dark' else 'lightMode',titleType=titleType,scrollBarWidget=self._mainScrollArea,titleTypeColors=self._customTitleType,noneControl=noneControl)
        if mode == 'custom': return qssCodesClass.customQss(titleType=titleType,styleDict=self._customQssThemplate,scrollBarWidget=self._mainScrollArea,titleTypeColors=self._customTitleType,noneControl=noneControl)
    
    def __close(self):
        self.blockingWindow.deleteLater()
        self.closed.emit(True)
        self.close()

    def getInfos(self):
        infos = {
            'widget':self,
            'titleWidget':self._titleWidget,
            'contentWidgets':self._subTitle,
            'titleText':self._title.title(),
            'image':self._img,
            'themeType':self._themeType,
            'size':(self._width,self._height),
            'producer':'https://github.com/myygunduz/pyqtCuWi'}
        return infos

    def setWidht(self,width:int):
        self._width = width
        self.setFixedSize(self._width,self._height)

    def setHeight(self,height:int):
        self._height = height
        self.setFixedSize(self._width,self._height)

    def setThemeType(self,themeType:str):
        if themeType not in ['dark','light','custom']:
            raise  InvalidThemeType(themeType,['dark','light','custom'])
        self._themeType = themeType
        self.themeUpdate()

    def setTitleText(self,title:str):
        self._title = title
        self.title.setText(self._title.title())

    def setSubTitle(self,subTitle:str):
        if subTitle.strip() == '':
            self.subTitle.hide()
        else:
            self.subTitle.setText(subTitle)
            self.subTitle.show()

    def setImage(self,filePath:str):
        self.image.setSource(filePath)

    def setCustomQss(self,styleDict:dict):
        for i in styleDict:
            if i not in self._customQssThemplate.keys():
                raise InvalidStyleVariable(i,self._customQssThemplate.keys())
            else:
                self._customQssThemplate[i] = styleDict[i]

    def addCustomContentTitleType(self,titleType:dict):
        for i in titleType:
            if len(titleType[i]) == 3 and type(titleType[i]) == tuple and type(i) == str:
                self._customTitleType[i] = titleType[i]
            else:
                raise FailedToAddTitleType()

    def addContent(self,title:str,content:tuple,titleType:str='append'):
        groupbox = QGroupBox(title)
        groupbox.setStyleSheet(self.__Qss(titleType,mode=self._themeType,noneControl = True))
        groupbox.setFixedWidth(self._width-20)
        layout = QVBoxLayout()
        layout.setSpacing(0)
        groupbox.setLayout(layout)
        widgetText = {}
        for i in content:
            text = f'● <b>{i}</b> {content[i]}'
            widgetText[f'text{list(content.keys()).index(i)}'] = text
            label = QLabel()
            label.mousePressEvent = lambda event: self.clickedContent.emit({'widget':groupbox,'titleType':titleType,'texts':widgetText}) if event.button() == 1  else print()
            label.setOpenExternalLinks(True)
            label.setWordWrap(True)
            label.setText(text)

            layout.addSpacing(10)
            layout.addWidget(label)
            layout.addSpacing(20)
        self._mainLayout.addWidget(groupbox)
        info = {
            'widget':groupbox,
            'titleType':titleType
        }
        self._subTitle.append(info)


    def themeUpdate(self):  
        qss = self.__Qss(titleType=None,mode=self._themeType)
        self.setStyleSheet(qss)
        for i in self._subTitle:
            i['widget'].setStyleSheet(self.__Qss(i['titleType'],mode=self._themeType))

    def closeWidget(self):
        self.__close()
    class _qssCodes:
        def __init__(self,main):
            self._main = main
            parent = Path(__file__).parent

            self._colors = readJ(str(Path(parent, 'pyqtCuWiDatabase', 'colors.json')))['popUp']
        def defaultQss(self,colorMode,titleType:str=None,scrollBarWidget=None,titleTypeColors=None,noneControl = False):
            self._titleTypeColors = titleTypeColors
            colors = self._colors[colorMode]
            self._main.qssMainWidget.setStyleSheet(f"background-color:{colors['content']['backgroundColor']['hex']};" )
            qss = (
                "QScrollArea{"
                "border:hidden;"
                "}"
                "QWidget#popUp{"
                f"background-color:{colors['titleBar']['backgroundColor']['hex']};"
                f"color:{colors['content']['textColor']['hex']};"            
                "}"
                "QWidget#titleWidget{"
                f"background-color:{colors['titleBar']['backgroundColor']['hex']};"
                f"color:{colors['titleBar']['textColor']['hex']};"
                "}"
                "QLabel#mainTitle{"
                f"color:{colors['titleBar']['textColor']['hex']};"
                f"background-color:{colors['titleBar']['backgroundColor']['hex']};"
                "font-family:Times;"
                "font-size:20px;"
                "}"
                "QLabel#subTitle{"
                f"color: rgba{tuple(list(eval(colors['titleBar']['textColor']['rgb']))+[80])};"
                "font-family:Times;"
                "font-size:15px;"
                "}"
                "QPushButton#clsButton{"
                f"color:{colors['titleBar']['textColor']['hex']};"
                "background-color:rgba(0,0,0,0);"
                "font-family:Times;"
                "font-size:20px;"
                "}"
                "QPushButton#clsButton:hover{"
                f"background-color:{colors['titleBar']['buttonHover']['hex']};"
                "}"
                "QWidget#subWidget{"
                f"background-color:{colors['titleBar']['backgroundColor']['hex']};"
                "}"
            )
            if titleType in self._titleTypeColors.keys() and noneControl != False:
                qss = (
                    "QGroupBox{"
                    "background-color:rgba(0,0,0,0);"
                    f"border-top:3px solid rgb{self._titleTypeColors[titleType]};"
                    "font-size:20px;"
                    "font-family:Times;"
                    "margin-top: 0.3em;"
                    f"color:rgb{self._titleTypeColors[titleType]};"
                    "}"
                    "QGroupBox:title{"
                    "subcontrol-origin: margin;"
                    "bottom: 10px;"
                    "padding: 5px 0px 10px 0px;"
                    "}"
                    "QLabel{"
                    "font-family:Times;"
                    "font-size:15px;"
                    f"color:{colors['titleBar']['textColor']['hex']};"
                    "background-color:rgba(0,0,0,0);"
                    "border:hidden;"
                    "}"
                )
                return qss
            elif titleType not in self._titleTypeColors.keys() and noneControl != False:
                raise InvalidTitleType(titleType,self._titleTypeColors.keys())

            backgroundColor = colors['scrollBar']['backgroundColor']['hex']
            foregroundColor = colors['scrollBar']['scrollColor']['hex']
            
            self.scrollBar(backgroundColor,foregroundColor,scrollBarWidget)
            return qss
        def customQss(self,titleType,styleDict:dict,newTitleTypes:dict=None,scrollBarWidget=None,titleTypeColors=None,noneControl = False):
            
            self._titleTypeColors = titleTypeColors
            if newTitleTypes != None :
                for i in newTitleTypes:
                    self._titleTypeColors[i] = newTitleTypes[i]
            
            self._main.qssMainWidget.setStyleSheet(f"background-color:{styleDict['background-color']};" )
            qss = (
                "QScrollArea{"
                "border:hidden;"
                "}"
                "QWidget#mainWidget{"
                f"color:rgb{styleDict['text-color']};"
                f"background-color:rgb{styleDict['background-color']};"
                "}"

                "QWidget#titleWidget{"
                f"background-color:rgb{styleDict['title-background-color']};"
                "}"

                "QLabel#mainTitle{"
                f"font-size:{styleDict['title-font-size']}px;"
                f"color:rgb{styleDict['text-color']};"
                "}"

                "QLabel#subTitle{"
                f"font-size:{styleDict['sub-title-font-size']}px;"
                f"color:rgba{(styleDict['text-color'][0],styleDict['text-color'][1],styleDict['text-color'][2],100)};"
                "}"

                "QPushButton#clsButton{"
                f"font-size:{styleDict['icon-font-size']}px;"
                f"color:rgb{styleDict['text-color']};"
                "background-color:rgba(0,0,0,0);"
                "}"
                
                "QPushButton#clsButton:hover{"
                f"background-color:rgb{styleDict['button-hover-color']};"
                "}"

                "QWidget#subWidget{"
                f"background-color:rgb{styleDict['subWidget-background-color']};"
                "}"
            )
            if titleType in self._titleTypeColors.keys() and noneControl != False:
                qss = (
                    "QGroupBox{"
                    f"background-color:rgb{styleDict['background-color']};"
                    f"border-top:3px solid rgb{self._titleTypeColors[titleType]};"
                    f"font-size:{styleDict['font-size']}px;"
                    "margin-top: 10px;"
                    f"color:rgb{self._titleTypeColors[titleType]};"
                    "}"
                    "QGroupBox:title{"
                    "subcontrol-origin: margin;"
                    f"bottom: {int(styleDict['font-size']/5)}px;"
                    "padding: 5px 0px 5px 0px;"
                    "}"
                    "QLabel{"
                    f"font-size:{int(styleDict['font-size']*0.8)}px;"
                    f"color:rgb{styleDict['text-color']};"
                    "background-color:rgba(0,0,0,0);"
                    "border:hidden;"
                    "}"
                )
                return qss
            elif titleType not in self._titleTypeColors.keys() and noneControl != False:
                raise InvalidTitleType(titleType,self._titleTypeColors.keys())

            backgroundColor = styleDict['scrollBar-background-color']
            foregroundColor = styleDict['scrollBar-foreground-color']
                
            self.scrollBar(backgroundColor,foregroundColor,scrollBarWidget)
            return qss
        def scrollBar(self,background,foreground,widget):
            if isinstance(background,tuple):
                foreground = f'rgb{foreground}'
                background = f'rgb{background}'
            scrollBarQss = (   
                    "QScrollBar:vertical" "{"
                    f"border:hidden;"
                    f"background:{foreground};"
                    "width:14px;"
                    "margin: 0px 0px 0px 0px;"
                    "}"

                    "QScrollBar::handle:vertical {"
                    "background: qlineargradient(x1:0, y1:0, x2:1, y2:0,"
                    f"stop: 0 {foreground}, stop: 0.5 {foreground}, stop:1 {foreground});"
                    "min-height: 0px;"
                    "margin: 0px 0px 0px 0px;"
                    "width: 10px;"
                    "border-width:0px;"
                    "border-radius: 0px;"
                    "}"

                    "QScrollBar::add-line:vertical {"
                    "height: 0px;"
                    "subcontrol-position: bottom;"
                    "subcontrol-origin: margin;"
                    "}"

                    "QScrollBar::sub-line:vertical {"
                    "height: 0 px;"
                    "subcontrol-position: top;"
                    "subcontrol-origin: margin;"
                    "}"

                    "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical" "{"
                    f"background: {background};"
                    "border-radius: 0px;"
                    "}")
            widget.verticalScrollBar().setStyleSheet(scrollBarQss)

    def mousePressEvent(self, event):
        self.startpos = self.pos()
        self.__mousePressPos = None
        self.__mouseMovePos = None
        if event.button() == Qt.LeftButton:
            self.__mousePressPos = event.globalPos()
            self.__mouseMovePos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and event.y() <= 36:
            currPos = self.mapToGlobal(self.pos())
            globalPos = event.globalPos()
            diff = globalPos - self.__mouseMovePos
            newPos = self.mapFromGlobal(currPos + diff)
            self.move(newPos)

            self.__mouseMovePos = globalPos

            self.raise_()

    def mouseReleaseEvent(self, event):
        if self.__mousePressPos is not None:
            moved = event.globalPos() - self.__mousePressPos
            if moved.manhattanLength() > 3:
                event.ignore()
                return