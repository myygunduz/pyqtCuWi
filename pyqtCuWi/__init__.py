#          Custom Widgets For PyQt5 Module           #
#          GPL 3.0 - myygunduz - pyqtCuWi            #
#        https://github.com/myygunduz/pyqtCuWi       #


__version__ = '1.4.0'

# version 0.0.0
from .iconbutton import iconButton 
from .rankwidget import rankWidget
from .popup import  popUp
from .outerradius import  outerRadius

# version 1.0.0
from .loadingscreen import  loadingScreen
from .qfboxlayout import  QFBoxLayout
from .tagarea import  tagArea
from .qhtmleditor import QHtmlTextEditor
from .qsyntaxhighlight import QSyntaxHighlight


class pyqtCuWiColor:
    def __init__(self) -> None:
        self.QTheme = self.QTheme()
    def __repr__(self):
        return 'pyqtCuWiColor'
    class QTheme():
        DARK_AMBER = "dark_amber.xml"
        DARK_BLUE = "dark_blue.xml"
        DARK_CYAN = "dark_cyan.xml"
        DARK_LIGHTGREEN = "dark_lightgreen.xml"
        DARK_PINK = "dark_pink.xml"
        DARK_PURPLE = "dark_purple.xml"
        DARK_RED = "dark_red.xml"
        DARK_TEAL = "dark_teal.xml"
        DARK_YELLOW = "dark_yellow.xml"
        LIGHT_AMBER = "light_amber.xml"
        LIGHT_BLUE = "light_blue.xml"
        LIGHT_CYAN = "light_cyan.xml"
        LIGHT_CYAN_500 = "light_cyan_500.xml"
        LIGHT_LIGHTGREEN = "light_lightgreen.xml"
        LIGHT_PINK = "light_pink.xml"
        LIGHT_PURPLE = "light_purple.xml"
        LIGHT_RED = "light_red.xml"
        LIGHT_TEAL = "light_teal.xml"
        LIGHT_YELLOW = "light_yellow.xml"

        def getAllThemes(self):
            return [
                self.DARK_AMBER,
                self.DARK_BLUE,
                self.DARK_CYAN,
                self.DARK_LIGHTGREEN,
                self.DARK_PINK,
                self.DARK_PURPLE,
                self.DARK_RED,
                self.DARK_TEAL,
                self.DARK_YELLOW,
                self.LIGHT_AMBER,
                self.LIGHT_BLUE,
                self.LIGHT_CYAN,
                self.LIGHT_CYAN_500,
                self.LIGHT_LIGHTGREEN,
                self.LIGHT_PINK,
                self.LIGHT_PURPLE,
                self.LIGHT_RED,
                self.LIGHT_TEAL,
                self.LIGHT_YELLOW
                ]   
    