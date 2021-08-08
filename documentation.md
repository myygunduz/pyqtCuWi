# pyqtCuWi

### IconButton

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

#### Example
```py
from PyQt5.QtWidgets import QApplication, QVBoxLayout,QWidget
from PyQt5.QtCore import QTimer
from pyqtCuWi import IconButton

class window(QWidget):
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
    window = window()
    window.show()
    app.exec_()
```
#### Output
<img src= "https://github.com/myygunduz/pyqtCuWi/blob/main/gifs/iconButton.gif" width="500">






### Rank Widget

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

#### Example 
```py
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
trying = main()
trying.show()
app.exec_()
```
#### Output
<img src="https://github.com/myygunduz/pyqtCuWi/blob/main/gifs/rankWidget.gif" width="500">



### Pop Up

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



#### Example 
`Notes example is for popUp and outerRadius`
```py

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt,QSize
from PyQt5.QtGui import QCursor
from pyqtCuWi import popUp,outerRadius
class window(QWidget):
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
    window = window()
    window.show()
    app.exec_() 
```
#### Output:
<img src="https://github.com/myygunduz/pyqtCuWi/blob/main/gifs/popUp&outerRadius.gif">
