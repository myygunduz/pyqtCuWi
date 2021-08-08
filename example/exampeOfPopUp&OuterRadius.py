
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
    