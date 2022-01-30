#          Custom Widgets For PyQt5 Module           #
#          GPL 3.0 - myygunduz - pyqtCuWi            #
#        https://github.com/myygunduz/pyqtCuWi       #
#                                                    #
#                 QSyntaxHighlight                   #

from PyQt5.QtWidgets import (QWidget,QVBoxLayout,
                             QHBoxLayout,QPushButton,
                             QLabel,QTextEdit,
                             QMenuBar,QComboBox,
                             QListWidget,QApplication,
                             QFileDialog)
from PyQt5.QtCore import pyqtSignal,Qt

from pygments.formatters.html import HtmlFormatter
from pygments.styles import get_all_styles
from pygments import highlight
from pygments import lexers
from bs4 import BeautifulSoup

from pathlib import Path
from qt_material import apply_stylesheet 

import pyqtCuWi
from .pyqtCuWiModules import readJ
from .pyqtCuWiErrors import pyqtCuWiInvaledType

def parse(css:str) -> dict:
    res = dict()
    for i in css.split(";"):
        if i.strip() != "":
            try: res[i.split(":")[0]] = i.split(":")[1] 
            except: pass
    return res

class QSyntaxHighlight(QWidget):
    __CHANGE_TITLE_STATUS = True
    __SAVE_STATUS         = True
    __FILE_NAME           = 'Untitled'
    __THEME               = "default"
    __LANGUAGE            = "python"
    __PARENT              = None
    __ALL_EXTENSION       =  readJ(Path(Path(__file__).parent, 'pyqtCuWiDatabase', 'extensions.json'))

    highlighted = pyqtSignal(tuple)
    file_saved = pyqtSignal(str)
    file_opened = pyqtSignal(str)

    def __init__(self, parent = None):
        super().__init__() 
        self.__PARENT = parent

        self._mainLayout = QVBoxLayout()
        self.setLayout(self._mainLayout)

        self._layout = QHBoxLayout()
        self._mainLayout.addLayout(self._layout)
        
        self.__menu_bar()
        self.__widgets()
    def __repr__(self) -> str:
        return f'<pyqtCuWi.QSyntaxHighlight(File = {self.__FILE_NAME})>'
    def __menu_bar(self):
        self.menu_bar = QMenuBar()
        self._mainLayout.insertWidget(0,self.menu_bar)

        file = self.menu_bar.addMenu('File')
        new = file.addAction('New', lambda: self.__functions('new'), "Ctrl+N")
        open = file.addAction('Open', lambda: self.__functions('open'), "Ctrl+O")
        save = file.addAction('Save', lambda: self.__functions('save'), "Ctrl+S")
        save_as = file.addAction('Save As', lambda: self.__functions('save_as'), "Ctrl+Shift+S")
        exit = file.addAction('Exit', lambda: self.__functions('exit'), "Ctrl+Q")
    def __widgets(self):

        self._setting_area = QVBoxLayout()
        self._setting_area.setContentsMargins(0,0,0,0)
        self._setting_area.setSpacing(0)
        self._layout.addLayout(self._setting_area)

        self._setting_area.addWidget(QLabel('Please Select Language'))

        self.languages = QComboBox()
        for lexer in lexers.get_all_lexers():
            self.languages.addItem(lexer[0])
        self.languages.setCurrentIndex(self.languages.findText('Python'))
        self._setting_area.addWidget(self.languages)

        @self.languages.currentIndexChanged.connect
        def change_language():
            self.__LANGUAGE = self.languages.currentText()

        self._setting_area.addSpacing(10)
        self._setting_area.addWidget(QLabel('Please Select Style'))

        self.listWidget = QListWidget()
        self._setting_area.addWidget(self.listWidget)

        self.listWidget.addItems(get_all_styles())
        self.listWidget.setCurrentItem(self.listWidget.findItems(self.__THEME, Qt.MatchExactly)[0])

        @self.listWidget.itemClicked.connect
        def change_style():
            self.__THEME = self.listWidget.currentItem().text()

        self._input_area = QVBoxLayout()
        self._input_area.setContentsMargins(0,0,0,0)
        self._layout.addLayout(self._input_area)

        self._input_area.addWidget(QLabel('Input'))
        self.input = QTextEdit()
        @self.input.textChanged.connect
        def func():
            self.__SAVE_STATUS = True

        self._input_area.addWidget(self.input)

        self._input_area.addWidget(QLabel('Output'))
        self.output = QTextEdit()
        self._input_area.addWidget(self.output)

        self._buttons_area = QHBoxLayout()
        self._buttons_area.setContentsMargins(0,0,0,0)
        self._input_area.addLayout(self._buttons_area)

        self.preview = QPushButton('Preview')
        self._buttons_area.addWidget(self.preview)
        self.preview.clicked.connect(lambda: self.__functions('preview'))


        self.copy = QPushButton('Copy Code')
        self._buttons_area.addWidget(self.copy)        
        self.copy.clicked.connect(lambda: self.__functions('copy'))

    def __setTitle(self, title:str) -> None: 
        if self.__CHANGE_TITLE_STATUS:
            if self.__PARENT is None:
                self.setWindowTitle(''.join(i for i in self.windowTitle().split('[')[0])+f'[{title}]')
            else:
                self.__PARENT.setWindowTitle(''.join(i for i in self.__PARENT.windowTitle().split('[')[0])+f'[{title}]')  
        
    def __functions(self, process_type):
        if process_type == 'preview' : self.__highlight_code()
        elif process_type == 'copy'  : QApplication.clipboard().setText(self.output.toHtml())
        
        elif process_type == 'new':
            self.input.clear()
            self.output.clear()
            self.__setTitle('Untitled')
            self.__FILE_NAME = 'Untitled'

        elif process_type == 'open':
            dialog = self.__file_dialog('open')
            self.__FILE_NAME = dialog[0]
            if dialog[1]:
                self.__SAVE_STATUS = False
                with open(self.__FILE_NAME, 'r') as f :
                    self.input.setPlainText(f.read())
                self.__setTitle(self.__FILE_NAME.split('/')[-1])
                self.file_opened.emit(self.__FILE_NAME)
                
                self.languages.setCurrentIndex(self.languages.findText(self.__ALL_EXTENSION[self.__FILE_NAME.split('.')[-1]]))
        elif process_type == 'save':
            control = True
            if self.__SAVE_STATUS:
                dialog  = self.__file_dialog('save')
                self.__FILE_NAME = dialog[0]
                control = dialog[1]
            if control:
                self.__SAVE_STATUS = False
                with open(self.__FILE_NAME, 'w') as f : 
                    f.write(self.output.toHtml())
                self.__setTitle(self.__FILE_NAME.split('/')[-1])
                self.file_saved.emit(self.__FILE_NAME)
        elif process_type == 'save_as':
            self.__SAVE_STATUS = True
            self.__functions('save')
        elif process_type == 'exit':
            if self.__PARENT is None:
                self.close()
            else:
                self.__PARENT.close()
    
    def __file_dialog(self, dialog_type):
        if   dialog_type == 'save' : return QFileDialog.getSaveFileName(self, "Save", "", "Hypertext Markup Language (*.html)")
        elif dialog_type == 'open' : return QFileDialog.getOpenFileName(self, "Open Page", "")
    
    def __highlight_code(self):
        formatter = HtmlFormatter(style=self.__THEME, noclasses=True)
        lex = lexers.get_lexer_by_name(self.__LANGUAGE)
        html_code = highlight(self.input.toPlainText(), lex, formatter)


        soup = BeautifulSoup(html_code, 'html.parser')
        
        div = soup.find("div", attrs={"class": "highlight"})
        
        bground = div['style']
        style = parse(div["style"])
        div['style'] = div['style'] + ";border-radius: 12px;over;"

        
        pre = div.find('pre')
        pre['style'] = pre['style'] + f'background : {style["background"]};margin: 5px, 20px; border-radius: 12px; padding: 20px;'
        

        self.output.setStyleSheet(bground)
        self.output.setHtml(str(soup.prettify()))
        self.highlighted.emit((str(soup.prettify()), self.__THEME, self.__LANGUAGE))

    def changeStatusChangeTitle(self, status:bool) -> None : self.__CHANGE_TITLE_STATUS = status
    def setDefaultStyle(self, style:'pyqtCuWi.pyqtCuWiColor') -> None : 
        if style in pyqtCuWi.pyqtCuWiColor.QTheme().getAllThemes():
            apply_stylesheet(self, style)
        else:
            raise pyqtCuWiInvaledType("Theme",style, pyqtCuWi.pyqtCuWiColor.QTheme().getAllThemes())