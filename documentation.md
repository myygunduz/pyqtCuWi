# pyqtCuWi
<p>
  <img src="https://img.shields.io/badge/python-3.8%2B-informational?style=flat-square&logo=python">
  <img src="https://img.shields.io/badge/license-GPL%203.0-succes.svg?style=flat-square&logo=license">
  <img src="https://img.shields.io/badge/version-2.1.0-important?style=flat-square">
</p>

## Contents
 - [IconButton](https://github.com/myygunduz/pyqtCuWi/blob/main/documentation.md#iconbutton)
 - [Rank Widget](https://github.com/myygunduz/pyqtCuWi/blob/main/documentation.md#rank-widget)
 - [PopUp](https://github.com/myygunduz/pyqtCuWi/blob/main/documentation.md#pop-up)
 - [Outer Radius](https://github.com/myygunduz/pyqtCuWi/blob/main/documentation.md#outer-radius)
 - [Loading Screen](https://github.com/myygunduz/pyqtCuWi/blob/main/documentation.md#loading-screen)
 - [QFBoxLayout](https://github.com/myygunduz/pyqtCuWi/blob/main/documentation.md#qfboxlayout)
 - [Tag Area](https://github.com/myygunduz/pyqtCuWi/blob/main/documentation.md#tag-area)
 - [QHtmlTextEditor](https://github.com/myygunduz/pyqtCuWi/blob/main/documentation.md#qhtmltexteditor)
 - [QSyntaxHighlight](https://github.com/myygunduz/pyqtCuWi/blob/main/documentation.md#qsyntaxhighlight)

### IconButton
My first custom widget. To dynamically change the icon. 

#### Parameters


- `text` (str) : The text shown above the button. (No default)
- `icon` (str) : Icon shown above the button. (Default : None)
- `iconSize` (tuple) : Size of icon. (Default : None)
- `iconDirection ['left' or 'right']` (str) : Direction of the icon on the button. (Default : 'left')


#### Methods

- Get Info
    - `getText()` (str) : Returns the text of the button
    - `getIcons()` (dict) : Returns button icons 
- Set Info
    - `setText(text)` (str) : Sets the text of the button
    - `setIcon(filepath)` (str) : Sets the default icon of the button
    - `setHoverIcon(filepath)` (str) : Sets the hover icon of the button
    - `setPressIcon(filepath)` (str) : Sets the press icon of the button
    - `setIconSize(size) [width and height]` (tuple) : Sets size of the buttons icon
    - `setIconDirection(direction) ['left' or 'right']` (str) : Sets direction of the icon

#### Signals

- `hoverMouse` : Bool value returns when the mouse hovers over the button and leaves the button
- `pressMouse` : Bool value returns when mouse button is pressed

<details>
  <summary>Example</summary>

    from PyQt5.QtWidgets import QApplication, QVBoxLayout,QWidget
    from PyQt5.QtCore import QTimer
    from pyqtCuWi import IconButton

    class main(QWidget):
        def __init__(self):
            super().__init__()

            self.setWindowTitle('IconButton')

            self.layout = QVBoxLayout()
            self.iconButton = IconButton(text = "IconButton",icon='assets/number-9.png',iconSize=(100,100),iconDirection='left')
            self.iconButton.setHoverIcon('assets/number-8.png')
            self.iconButton.setPressIcon('assets/number-7.png')

            self.layout.addWidget(self.iconButton)
            self.setLayout(self.layout)

            self.iconButton.hoverMouse.connect(self.hoverSignal)
            self.iconButton.pressMouse.connect(self.pressSignal)

        def hoverSignal(self, boolValue):
            if boolValue:
                print("Mouse over button.")
                self.iconButton.setIconDirection('left')

            else:
                print("Mouse left button.")
                self.iconButton.setIconDirection('right')


        def pressSignal(self,boolValue):
            if boolValue:
                print("Button pressed.")
                QTimer.singleShot(1000,self.changeIcons)

        def changeIcons(self):
                icons = self.iconButton.getIcons()
                if '9' in icons['manualIcon']:
                    self.iconButton.setIcon('assets/number-6.png')
                    self.iconButton.setHoverIcon('assets/number-5.png')
                    self.iconButton.setPressIcon('assets/number-4.png')
                elif '6' in icons['manualIcon']:
                    self.iconButton.setIcon('assets/number-3.png')
                    self.iconButton.setHoverIcon('assets/number-2.png')
                    self.iconButton.setPressIcon('assets/number-1.png')
                elif '3' in icons['manualIcon']:
                    self.iconButton.setIcon('assets/number-9.png')
                    self.iconButton.setHoverIcon('assets/number-8.png')
                    self.iconButton.setPressIcon('assets/number-7.png')



    if __name__ == '__main__':
        app = QApplication([])
        main = main()
        main.show()
        app.exec_()
</details>

[File](https://github.com/myygunduz/pyqtCuwi/blob/main/example/exampleOfIconButton.py)

#### Output
<img src= "https://github.com/myygunduz/pyqtCuWi/blob/main/gifs/iconButton.gif" width="500">


### Rank Widget
To sort names.

#### Notes

StyledButton is used. [Click](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/documentation.md#StyledButton) for detailed information.

#### Parameters

- `main` (object) : Sets the main widget. (No default)
- `layout_type ['H' or 'V']` (str) : Sets the layout type. (Default : 'V')

#### Methods
- Get Info
    - `gettext(widget)` (object) : Returns the text of the widget.
- Set Info
    - `sethidebutton(value)` (bool) : Determines whether the icons appear initially. (Default : True)
    - `seticon(filepath, buttontype)` (str) : Changes the widget's icon.
    - `setstyledict(stylecode)` (tuple) : Sets the style of the up and down trash buttons.
    - `setstylesheet(stylecode)` (tuple) : Sets the style of the widget.
- Other
    - `addbutton(text)` (str) : Creates button and adds it to the layout.

#### Signals

- `clickedButton` : Returns button information when button is clicked.
- `deleteButton` : Returns the button's information when the button is deleted.

<details>
  <summary>Example</summary>

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
</details>

[File](https://github.com/myygunduz/pyqtCuwi/blob/main/example/exampleOfRankWidget.py)

#### Output
<img src="https://github.com/myygunduz/pyqtCuWi/blob/main/gifs/rankWidget.gif" width="500">



### Pop Up
To create a popup.

#### Notes

ImageBox is used. [Click](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/documentation.md#ImageBox) for detailed information.

#### Parameters

- `parent` (object) : Sets the main widget. (No default)
- `title` (str) : Sets the title of PopUp. (Default : None)
- `img` (str) : Picture settings to be displayed on the widget. (Default : None)
- `themeType ['dark', 'light' or 'custom']` (str) : Sets the theme type. (Default : 'dark')

#### Methods

- Get Info
    - `getInfos()` : Returns all information about the PopUp.
- Set Info
    - `setWidht(width)` (int) : Sets the width of PopUp.
    - `setHeight(height)` (int) : Sets the height of PopUp.
    - `setThemeType(themeType) ['dark', 'light' or 'custom']` (str) : Sets the theme type.
    - `setTitleText(title)` (str) : Sets the title of PopUp.
    - `setSubTitle(subTitle)` (str) : Sets the sub title of PopUp.
    - `setCustomQss(styleDict)` (dict) : Sets the custom qss code.
    - `setImage(filePath)` (str) : Sets the file path of the image.
- Other
    - `addCustomContentTitleType(titleType)` (tuple) : Adds content header type.
    - `addContent(title, content, titleType)` (str, tuple, str) : Adds content.
    - `themeUpdate()` : Updates theme.
    - `subLayout.addWidget()` : Adds widget to subLayout.
    - `closeWidget()` : Closes the widget.

#### Signals

- `closed` : Returns bool when PopUp is closed.
- `clickedContent` : Returns content information when content is clicked.

#### Example
[Click](https://github.com/myygunduz/pyqtCuWi/blob/main/documentation.md#example-3) for example.

#### Output
[Click](https://github.com/myygunduz/pyqtCuWi/blob/main/documentation.md#output-3) for output.

### Outer Radius
 Allows external radius to be added to both sides of a widget you want.

#### Parameters

- `widget` (object) : Sets the widget. (Default : QLineEdit)
- `direction ['left', 'right', 'up', 'down']` (str) : Sets the widget's direction. (Default : 'left')
- `width` (int) : Sets the widget's width. (Default : 300)
- `height` (int) : Sets the widget's height. (Default : 150)
- `objectName` (str) : Sets the widget's object name. (Default : 'widget')

#### Methods
- `addWidgetQss(qssCode, Type, objectName) [Type:['default', 'hover', 'press']]` (str, str, str) : Adds custom Qss for widget.
- `changeDefaultQss(qssCode) ['interiorColor', 'exteriorColor', 'radius']` (dict) : Changes default Qss.

#### Signals
Outer Radius has no signals, but you can generate signals via outerRadius.widget.



<details>
    <summary>Example</summary>

    #Notes example is for popUp and outerRadius

    from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QApplication
    from PyQt5.QtCore import Qt
    from PyQt5.QtGui import QCursor
    from pyqtCuWi import popUp,outerRadius
    class main(QWidget):
        def __init__(self):
            super().__init__()
            self.widgetWidget = QWidget()
            self.widgetWidget.setMinimumSize(400,600)

            self.widgetWidget.setStyleSheet("background-color:#212121;")
            self.mainLayout = QVBoxLayout()
            self.widgetsLayout = QVBoxLayout()
            self.widgetsLayout.setSpacing(0)
            self.widgetsLayout.setContentsMargins(0,0,0,0)
            self.widgetWidget.setLayout(self.widgetsLayout)
            self.mainLayout.addWidget(self.widgetWidget,alignment=Qt.AlignCenter)

            self.setStyleSheet("background-color:#2b2b2b;")
            self.setLayout(self.mainLayout)

            self.widgets()
        def widgets(self):
            self.title = outerRadius(QLabel,'up',width=300,height=50)
            self.title.addWidgetQss("font-size:15px; color:white; font-family: montserrat;")
            self.title.changeDefaultQss({'radius':25})
            self.title.widget.setAlignment(Qt.AlignCenter)
            self.title.widget.setText('REGISTER AREA')

            self.username = outerRadius(QLineEdit,'left')
            self.username.addWidgetQss("font-size:30px; color:white; font-family: montserrat;")
            self.username.widget.setPlaceholderText('Username')
            self.username.widget.setText('sdsd')

            self.mail = outerRadius(QLineEdit,'left')
            self.mail.addWidgetQss("font-size:30px; color:white; font-family: montserrat;")
            self.mail.widget.setPlaceholderText('Mail')

            self.password = outerRadius(QLineEdit,'right')
            self.password.addWidgetQss("font-size:30px; color:white; font-family: montserrat;")
            self.password.widget.setPlaceholderText('Password')
            self.password.widget.setEchoMode(QLineEdit.Password)

            self.verificationPassword = outerRadius(QLineEdit,'right')
            self.verificationPassword.addWidgetQss("font-size:30px; color:white; font-family: montserrat;")
            self.verificationPassword.widget.setPlaceholderText('Password Again')
            self.verificationPassword.widget.setEchoMode(QLineEdit.Password)

            self.registerButton = outerRadius(QPushButton,'down',width=300,height=50)
            self.registerButton.addWidgetQss("font-size:20px; color:white; font-family: montserrat;",'default')
            self.registerButton.addWidgetQss("background-color:white;font-size:20px; color:black; font-family: montserrat;",'hover')
            self.registerButton.addWidgetQss("background-color:gray;font-size:20px; color:white; font-family: montserrat;",'press')
            self.registerButton.widget.setCursor(QCursor(Qt.PointingHandCursor))
            self.registerButton.widget.setText('register')
            self.registerButton.widget.clicked.connect(self.clickButton)

            self.widgetsLayout.addWidget(self.title,alignment=Qt.AlignCenter)
            self.widgetsLayout.addWidget(self.username,alignment=Qt.AlignLeft)
            self.widgetsLayout.addSpacing(60)
            self.widgetsLayout.addWidget(self.mail,alignment=Qt.AlignLeft)
            self.widgetsLayout.addSpacing(60)
            self.widgetsLayout.addWidget(self.password,alignment=Qt.AlignRight)
            self.widgetsLayout.addSpacing(60)
            self.widgetsLayout.addWidget(self.verificationPassword,alignment=Qt.AlignRight)
            self.widgetsLayout.addSpacing(40)
            self.widgetsLayout.addWidget(self.registerButton,alignment=Qt.AlignCenter)

        def clickButton(self):
            self.documentation = popUp(self,'popUp Documents','assets/documentation.jpg','dark')
            self.documentation.show()
            contentOne = {
                "parent link(object)" : "Sets the main widget. (No default)",
                "title (str)" : "Sets the title of PopUp. (Default : None)",
                "img (str)" : "Picture settings to be displayed on the widget. (Default : None)",
                "themeType ['dark', 'light' or 'custom'] (str)" : "Sets the theme type. (Default : 'dark')"
            }
            
            contentTwo = {
                "getInfos()" : "Returns all information about the PopUp."
            }
            contentThree = {
                "setWidht(width) (int)" : "Sets the width of PopUp.",
                "setHeight(height) (int)" : "Sets the height of PopUp.",
                "setThemeType(themeType) ['dark', 'light' or 'custom'] (str)" : "Sets the theme type.",
                "setTitleText(title) (str)" : "Sets the title of PopUp.",
                "setSubTitle(subTitle) (str)": "Sets the sub title of PopUp.",
                "setCustomQss(styleDict) (dict)" : "Sets the custom qss code.",
                "setImage(filePath) (str)" : "Sets the file path of the image."
            }
            contentFour = {
                "addCustomContentTitleType(titleType) (tuple)" : "Adds content header type.",
                "addContent(title, content, titleType) (str, tuple, str)" : "Adds content.",
                "themeUpdate()" : "Updates theme.",
                "subLayout.addWidget()" : "Adds widget to subLayout.",
                "closeWidget()" : "Closes the widget."
            }

            contentFive = {
                "closed" : "Returns bool when PopUp is closed.",
                "clickedContent" : "Returns content information when content is clicked."
            }
            contentSix = {
                "":"ImageBox is used. <a href='https://github.com/kadir014/pyqt5-custom-widgets/blob/main/documentation.md#ImageBox' style = 'color:white;'>Click</a> for detailed information."
            }
            self.documentation.addContent('Parameters',contentOne)
            self.documentation.addContent('Get Methods',contentTwo)
            self.documentation.addContent('Set Methods',contentThree)
            self.documentation.addContent('Other Methods',contentFour)
            self.documentation.addContent('Signals',contentFive)
            self.documentation.addContent('Notes',contentSix,titleType='warning')
            

            button = QPushButton('Finished')

            button.setStyleSheet('QPushButton{'
                                'border:4px solid red;'
                                'color:red;'
                                'background-color:rgba(0,0,0,0);'
                                'font: 20px Times;}'
                                'QPushButton:hover{'
                                'border:4px solid rgba(0,0,0,0);'
                                'color:#212121;'
                                'background-color:red;'
                                'font: 20px Times;}'
                                'QPushButton:pressed{'
                                'border:4px solid rgba(0,0,0,10);'
                                'color:#212121;'
                                'background-color:rgba(255,0,0,80);'
                                'font: 20px Times;}')

            button.setFixedSize(100,50)
            button.clicked.connect(self.clicked)

            self.documentation.subLayout.addSpacing(500)
            self.documentation.subLayout.addWidget(button)
            self.documentation.subLayout.addSpacing(20)
        
        def clicked(self):
            self.documentation.closeWidget()
            self.widgetWidget.hide()
            
            label = QLabel("Operation Successfully Completed")
            label.setStyleSheet('QLabel{'
                            'color:white;'
                            'font:50px Times;}')
            label.setAlignment(Qt.AlignCenter)
            label.setFixedSize(self.width(),self.height())

            closeButton = QPushButton('CLOSE')
            closeButton.setStyleSheet('QPushButton{'
                                'border:4px solid red;'
                                'color:red;'
                                'background-color:rgba(0,0,0,0);'
                                'font: 30px Times;}'
                                'QPushButton:hover{'
                                'border:4px solid rgba(0,0,0,0);'
                                'color:#212121;'
                                'background-color:red;'
                                'font: 30px Times;}'
                                'QPushButton:pressed{'
                                'border:4px solid rgba(0,0,0,10);'
                                'color:#212121;'
                                'background-color:rgba(255,0,0,80);'
                                'font: 30px Times;}')
            closeButton.setFixedWidth(300)
            closeButton.clicked.connect(lambda: self.deleteLater())
            self.mainLayout.addWidget(label)
            self.mainLayout.addWidget(closeButton,alignment=Qt.AlignCenter)
            self.mainLayout.addSpacing(50)

    if __name__ == '__main__':
        app = QApplication([])
        main = main()
        main.show()
        app.exec_() 
</details>


[File](https://github.com/myygunduz/pyqtCuwi/blob/main/example/exampeOfPopUp%26OuterRadius.py)

#### Output:
<img src="https://github.com/myygunduz/pyqtCuWi/blob/main/gifs/popUp&outerRadius.gif">


### Loading Screen
A loading screen that appears before the main window.

#### Parameters

- `appName` (str) : The app name shown above the window. (No default)
- `time` (int) : Sets prograss bar time (Default : 100)
- `theme ['dark' or 'light']` (tuple) : Sets theme type. (Default : "dark")


#### Methods

 - `addSubTitle(subTitle)` (str or list) : Allows you to add subtitle texts.
 - `deleteDeveloper()` : Allows you to remove the text 'Developer by Mücahit Gündüz' in the lower right.
 - `setAppName(appName)` (str) : Sets the app name shown above the window.

#### Signals

- `finished` : It works when the program is finished.

<details>
  <summary>Example</summary>

    from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QPushButton
    from PyQt5.QtCore import Qt
    from pyqtCuWi import loadingScreen

    class main(QWidget):
        def __init__(self):
            super().__init__()

            self.setFixedSize(640,480)
            self.mainLayout = QVBoxLayout()
            self.setLayout(self.mainLayout)

            self.setStyleSheet("background-color:#212121;")

            self.text = QLabel("Operation Successfully Completed")
            self.text.setStyleSheet('QLabel{'
                            'color:white;'
                            'font:40px Times;}')
            self.text.setAlignment(Qt.AlignCenter)
            self.text.setFixedSize(self.width(),self.height())

            self.finishButton = QPushButton("Finished")
            self.finishButton.setStyleSheet('QPushButton{'
                                'border:4px solid red;'
                                'color:red;'
                                'background-color:rgba(0,0,0,0);'
                                'font: 30px Times;}'
                                'QPushButton:hover{'
                                'border:4px solid rgba(0,0,0,0);'
                                'color:#212121;'
                                'background-color:red;'
                                'font: 30px Times;}'
                                'QPushButton:pressed{'
                                'border:4px solid rgba(0,0,0,10);'
                                'color:#212121;'
                                'background-color:rgba(255,0,0,80);'
                                'font: 30px Times;}')
            self.finishButton.setFixedWidth(300)
            self.finishButton.clicked.connect(lambda: self.deleteLater())

            self.mainLayout.addWidget(self.text,alignment=Qt.AlignCenter)
            self.mainLayout.addWidget(self.finishButton,alignment=Qt.AlignCenter)

    def finishedFunction():
        main.show()
        loadingWindow.deleteLater()
    if __name__ == '__main__':
        app=QApplication([])
        main = main()
        loadingWindow=loadingScreen("Program",100)

        loadingText =["Is this Windows?",
                    "Adjusting flux capacitor...",
                    "Please wait until the sloth starts moving.",
                    "Don't break your screen yet!",
                    "I swear it's almost done.",
                    "Let's take a mindfulness minute...",
                    "Unicorns are at the end of this road, I promise.",
                    "Listening for the sound of one hand clapping...",
                    "Keeping all the 1's and removing all the 0's...",
                    "Putting the icing on the cake. The cake is not a lie...",
                    "Cleaning off the cobwebs..."]
        #For more message: https://gist.github.com/meain/6440b706a97d2dd71574769517e7ed32
        loadingWindow.addSubTitle(loadingText)
        loadingWindow.finished.connect(finishedFunction)
        loadingWindow.show()
        app.exec_()
</details>

[File](https://github.com/myygunduz/pyqtCuwi/blob/main/example/exampleOfLoadingScreen.py)

#### Output:
<img src="https://github.com/myygunduz/pyqtCuWi/blob/main/gifs/loadingScreen.gif">

### QFBoxLayout
QFreeBoxLayout. Widget but its name is layout. To show widgets as scattered images.
#### Methods

- `addWidget(widget)` (QObject) : Adds a widget.
- `removeWidget(widget)` (QObject) : Removes a widget.
- `clear()` : Clears all widget.
- `setSpacing(value)` (int) : Sets the value of spacing.
- `setAlignment(QT.Corner) [TopLeftCorner, TopRightCorner, BottomLeftCorner, BottomRightCorner]` : Sets the type of alignment.

<details>
  <summary>Example</summary>

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

    class main(QWidget):
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
        main = main()
        main.show()
        app.exec_()
</details>

[File](https://github.com/myygunduz/pyqtCuwi/blob/main/example/exampleOfQFBoxLayout.py)

#### Output:
<img src="https://github.com/myygunduz/pyqtCuWi/blob/main/gifs/QFBoxLayout.gif">

### Tag Area
A widget for tags.

#### Parameters

- `Type [oneLine, freeBox]` (str) : The app name shown above the window. (Default : "oneLine")

#### Methods

 - `add(tagText)` (str) : Adds a tag to tags area.
 - `addHint(hintText)` (str) : Adds a hint text to tags entry area.
 - `onlyHint(value)` (bool) : Sets whether the user can only use hint texts.
 - `setTagLimit(limitValue)` (int) : Sets the label limit. The tag limit prevents creating more tags than the set amount.
 - `getTags()` : Returns all entered tags.
 - `clearTags()` : Clears all tags.

<details>
    <summary>Example</summary>

    from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QTextEdit, QLineEdit, QPushButton

    from pyqtCuWi import  tagArea

    class main(QWidget):
        def __init__(self):
            super().__init__()

            self.mainLayout = QVBoxLayout()
            self.setLayout(self.mainLayout)
            
            self.title = QLabel("Create Post")
            self.mainLayout.addWidget(self.title)

            self.entryTitle = QLineEdit()
            self.entryTitle.setPlaceholderText("Title")
            self.mainLayout.addWidget(self.entryTitle)

            self.entryContent = QTextEdit()
            self.entryContent.setPlaceholderText("Entry content")
            self.mainLayout.addWidget(self.entryContent)

            self.entryTag = tagArea("freeBox")
            self.entryTag.setTagLimit(3)
            self.mainLayout.addWidget(self.entryTag)

            self.share = QPushButton("Share")
            self.share.clicked.connect(self.printPost)
            self.share.setObjectName("share")
            self.mainLayout.addWidget(self.share)
            self.__qss()
        def __qss(self):
            self.setStyleSheet("""
            QWidget{
                background-color:rgb(251, 249, 250);
            }
            QLabel{
                font: 30px Montserrat Black;
                color:rgb(253, 0, 84);
                
            }
            QLineEdit{
                font-family: Montserrat ;
                color:rgb(253, 0, 84);
                selection-background-color:rgb(253, 0, 84);
                selection-color:rgb(251, 249, 250);
            }
            QTextEdit{
                color:rgb(253, 0, 84);
                font-family: Montserrat;
                selection-background-color:rgb(253, 0, 84);
                selection-color:rgb(251, 249, 250);
            }
            QPushButton{
                font-family: Montserrat Black;
                color:#F9F9F9;
            }
            QPushButton#share{
                font: 20px Montserrat Black;
                background-color:rgb(253, 0, 84);
                color:rgb(251, 249, 250);
            }
            QPushButton#share:pressed{
                font: 20px Montserrat Black;
                background-color:rgb(251, 249, 250);
                color:rgb(253, 0, 84);
            }
            """)

        def printPost(self):
            tags = ""
            for i in self.entryTag.getTags():
                tags += ' '+i if i.startswith("#") else f' #{i}'
            text = (f"""
            ====================   POST   ====================        

            {self.entryTitle.text().strip().upper() if self.entryTitle.text().strip() != "" else "Title Empty"}:
                {self.entryContent.toPlainText().strip().capitalize() if self.entryContent.toPlainText().strip() != "" else "Post Empty"}

            Tags:
                {tags if tags != "" else "Tags Empty"}

                                                Created by myygunduz.
                    """)

            print(text)

    if __name__ == '__main__':
        app = QApplication([])
        main = main()
        main.show()
        app.exec_()
</details>

[File](https://github.com/myygunduz/pyqtCuwi/blob/main/example/exampleOfTagArea.py)

#### Output:
<img src="https://github.com/myygunduz/pyqtCuWi/blob/main/gifs/tagArea.gif">

### QHtmlTextEditor
The task of this widget is to convert your text to html code.

#### Parameters

- `parent` (QObject) : Define parent to change window title. (optional)

#### Methods

 - `getAllActionButton()` -> list : Returns all visible QActions.
 - `getSourceCode()` -> str : Returns source code.
 - `getFileName()` -> str : Returns file name.
 - `changeStatusChangeTitle(status)` (bool) -> None : Sets the permission for change window title.
 - `setDefaultStyle(style type)` (pyqtCuWi.pyqtCuWiColor.QTheme) -> None : Sets the widget style using preset styles.

#### Signals

- `file_saved`  : Filename returns when changes are saved to a file.
- `file_opened` : Filename returns when open a file.

<details>
    <summary>Example</summary>

    from PyQt5.QtWidgets import QApplication
    from pyqtCuWi import QHtmlTextEditor

    app = QApplication([])
    win = QHtmlTextEditor()
    win.setWindowTitle('PyQt5 Text Editor')
    win.show()
    app.exec_()
</details>

[File](https://github.com/myygunduz/pyqtCuwi/blob/main/example/exampleOfQHtmlTextEditor.py)

#### Output
<img src="https://github.com/myygunduz/pyqtCuWi/blob/main/gifs/qhtmltexteditor.gif">

### QSyntaxHighlight
The task of this widget is highlighting your code.

#### Parameters

- `parent` (QObject) : Define parent to change window title. (optional)

#### Methods

 - `changeStatusChangeTitle(status)` (bool) -> None : Sets the permission for change window title.
 - `setDefaultStyle(style type)` (pyqtCuWi.pyqtCuWiColor.QTheme) -> None : Sets the widget style using preset styles.

#### Signals

- `file_saved`  : Filename returns when changes are saved to a file.
- `file_opened` : Filename returns when open a file.
- `highlighted` : Html code returns when highlighted your code.

<details>
    <summary>Example</summary>

    from PyQt5.QtWidgets import QApplication
    from pyqtCuWi import QSyntaxHighlight, pyqtCuWiColor

    app = QApplication([])
    win = QSyntaxHighlight()
    win.setWindowTitle('Code Highlight')
    win.setDefaultStyle(pyqtCuWiColor.QTheme().DARK_RED)
    win.show()
    app.exec_()
</details>

[File](https://github.com/myygunduz/pyqtCuwi/blob/main/example/exampleOfQSyntaxHighlight.py)

#### Output
<img src="https://github.com/myygunduz/pyqtCuWi/blob/main/gifs/qsyntaxhighlight.gif">