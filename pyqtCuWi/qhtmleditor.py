#          Custom Widgets For PyQt5 Module           #
#          GPL 3.0 - myygunduz - pyqtCuWi            #
#        https://github.com/myygunduz/pyqtCuWi       #
#                                                    #
#                  QHtmlTextEditor                   #



from email import message
from PyQt5.QtWidgets import (QWidget,QVBoxLayout,
                             QTextEdit,QMenuBar,
                             QAction,QActionGroup,
                             QToolBar,QDialog,
                             QGridLayout,QLabel,
                             QCheckBox,QPushButton,
                             QFileDialog,QFontDialog,
                             QColorDialog,QInputDialog,
                             QApplication,QMessageBox)
from PyQt5.QtCore import pyqtSignal, QSize, Qt
from PyQt5.QtGui import QIcon, QTextDocumentFragment, QFont, QTextListFormat
from PyQt5.QtPrintSupport import QPrintDialog

import pyqtCuWi
from .pyqtCuWiModules import readJ,writeJ
from .pyqtCuWiErrors import pyqtCuWiInvaledType
from .qsyntaxhighlight import QSyntaxHighlight

from pathlib import Path
from qt_material import apply_stylesheet


class QHtmlTextEditor(QWidget):
    __SOURCE_CODE_SHOW    = True
    __CHANGE_TITLE_STATUS = True
    __SAVE_STATUS         = True
    __FILE_NAME           = 'Untitled'
    __PATH                = Path(__file__).parent
    __HTML_CODE           = ''
    __TEXT                = ''
    __SETTINGS_FILE       = readJ(str(Path(__PATH, 'pyqtCuWiDatabase', 'settings.json')))
    __SETTINGS            = __SETTINGS_FILE['QHtmlTextEditor']    
    __DEFAULT_STYLE       = None

    file_saved = pyqtSignal(str)
    file_opened = pyqtSignal(str)

    def __repr__(self):
        return f'<pyqtCuWi.QHtmlTextEditor(File = {self.__FILE_NAME})>'
    def __init__(self, parent = None):
        super().__init__()
        
        self.__PARENT = parent

        self._mainLayout = QVBoxLayout()
        self.setLayout(self._mainLayout)

        self.__widgets()
        self.__functions('update')
    def __widgets(self):
        try: 
            self.text_area.deleteLater()
            self.copy_button.deleteLater()
        except: pass
        self.text_area = QTextEdit()

        self.text_area.selectionChanged.connect(lambda : self.__functions('update'))

        @self.text_area.textChanged.connect
        def func():
            self.__HTML_CODE = self.text_area.toHtml()
            self.__TEXT = self.text_area.toPlainText()
            
            self.__setTitle(f'*{self.__FILE_NAME.split("/")[-1]}' if self.__FILE_NAME[0] != "*" else self.__FILE_NAME)
        self.__bars()
        self._mainLayout.addWidget(self.text_area)

        self.copy_button = QPushButton('Copy Source Code')
        self.copy_button.setCursor(Qt.PointingHandCursor)
        self._mainLayout.addWidget(self.copy_button)
        self.copy_button.hide()
        @self.copy_button.clicked.connect
        def func():
            clipboard = QApplication.clipboard()
            clipboard.setText(self.text_area.toPlainText())
    def __bars(self):
        try: 
            self.menu_Bar.deleteLater()
            self.tool_bar.deleteLater()
        except: pass

        self.menu_Bar = QMenuBar()
        
        self._mainLayout.addWidget(self.menu_Bar)

        self.tool_bar = QToolBar()
        self.tool_bar.setIconSize(QSize(16,16))
        self._mainLayout.addWidget(self.tool_bar)

        align_buttons = []
        self.action_buttons = []
        for menu_type in self.__SETTINGS['menuBar'].keys():

            self.tool_bar.addSeparator()
            menu = self.menu_Bar.addMenu(menu_type.capitalize())
            menu.setStatusTip(menu_type.capitalize())

            for menu_button in self.__SETTINGS['menuBar'][menu_type].keys():
                icon = self.__SETTINGS['menuBar'][menu_type][menu_button]['icon']
                
                button = QAction(QIcon(str(Path(self.__PATH, 'pyqtCuWiAssets', 'QHtmlTextEditor', f'{icon}.png'))), str(menu_button).replace("_"," ").title(), self)
                button.setShortcut(self.__SETTINGS['menuBar'][menu_type][menu_button]['shortcut'])
                button.triggered.connect(lambda params=None, button_type=menu_button :self.__functions(button_type))
                menu.addAction(button)
                if self.__SETTINGS['menuBar'][menu_type][menu_button]['show']: self.tool_bar.addAction(button)

                if self.__SETTINGS['menuBar'][menu_type][menu_button]['checkable']: button.setCheckable(True)
                if 'align' in icon:
                    align_buttons.append(button)
                self.action_buttons.append(button)
        self.tool_bar.addSeparator()
        format_group = QActionGroup(self)
        for align_button in align_buttons:
            format_group.addAction(align_button)

    def __setTitle(self, title:str) -> None: 
        if self.__CHANGE_TITLE_STATUS:
            if self.__PARENT is None:
                self.setWindowTitle(''.join(i for i in self.windowTitle().split('[')[0])+f'[{title}]')
            else:
                self.__PARENT.setWindowTitle(''.join(i for i in self.__PARENT.windowTitle().split('[')[0])+f'[{title}]')  

    def __functions(self, process_type:str):
        text_area_text = QTextDocumentFragment.toPlainText(self.text_area.textCursor().selection())
        text_area_html = QTextDocumentFragment.toHtml(self.text_area.textCursor().selection())
        text_area_html = text_area_html.partition('<!--StartFragment-->')[2].partition('<!--EndFragment-->')[0]
          
        if process_type == 'new':
            self.text_area.clear()
            self.__FILE_NAME = 'Untitled'
            self.__HTML_CODE = ''
            self.__TEXT = ''
            self.__setTitle(self.__FILE_NAME)
            self.__SAVE_STATUS = True
        elif process_type == 'open':
            dialog = self.__file_dialog('open')
            if dialog[0].strip() != "":self.__FILE_NAME = dialog[0]
            if dialog[1].strip() != "":
                self.__SAVE_STATUS = False
                with open(self.__FILE_NAME, 'r') as f :
                    if self.__FILE_NAME.endswith('.html'):
                        self.text_area.setHtml(f.read())
                    else:
                        self.text_area.setPlainText(f.read())
                self.__setTitle(self.__FILE_NAME.split('/')[-1])
                self.file_opened.emit(self.__FILE_NAME)
        elif process_type == 'save':
            control = ""
            if self.__SAVE_STATUS:
                dialog  = self.__file_dialog('save')
                if dialog[0].strip() != "":self.__FILE_NAME = dialog[0]
                control = dialog[1]
            if control.strip()!="":
                self.__SAVE_STATUS = False
                with open(self.__FILE_NAME, 'w') as f : 
                    if self.__FILE_NAME.endswith('.html'):
                        f.write(self.__HTML_CODE)  
                    else: 
                        f.write(self.__TEXT)
                self.__setTitle(self.__FILE_NAME.split('/')[-1])
                self.file_saved.emit(self.__FILE_NAME)
        elif process_type == 'save_as':
            self.__SAVE_STATUS = True
            self.__functions('save')
        elif process_type == 'print':
            dlg = QPrintDialog()
            if dlg.exec_() : 
                self.text_area.print_(dlg.printer())
        elif process_type == 'quit':
            if self.__PARENT is None:
                if "*" in self.windowTitle():
                    quit_control = self.__file_dialog('quit')
                    if quit_control == QMessageBox.No:
                        return ... 
                self.close()
            else:
                if "*" in self.__PARENT.windowTitle():
                    quit_control = self.__file_dialog('quit')
                    if quit_control == QMessageBox.No:
                        return ... 
                self.__PARENT.close()
        
        elif process_type == 'undo'            : self.text_area.undo()
        elif process_type == 'redo'            : self.text_area.redo()
        elif process_type == 'cut'             : self.text_area.cut()
        elif process_type == 'copy'            : self.text_area.copy()
        elif process_type == 'paste'           : self.text_area.paste()
        elif process_type == 'select_all'      : self.text_area.selectAll()
        
        elif process_type == "bold"            : self.text_area.setFontWeight(QFont.Bold) if "600;"       not in text_area_html else self.text_area.setFontWeight(QFont.Normal)
        elif process_type == "italic"          : self.text_area.setFontItalic(True)       if "italic;"    not in text_area_html else self.text_area.setFontItalic(False)
        elif process_type == "underline"       : self.text_area.setFontUnderline(True)    if "underline;" not in text_area_html else self.text_area.setFontUnderline(False)
        elif process_type == "align_left"      : self.text_area.setAlignment(Qt.AlignLeft)
        elif process_type == "align_center"    : self.text_area.setAlignment(Qt.AlignCenter)
        elif process_type == "align_right"     : self.text_area.setAlignment(Qt.AlignRight)
        elif process_type == "align_justify"   : self.text_area.setAlignment(Qt.AlignJustify)

        elif process_type == "font"            : self.text_area.setCurrentFont(self.__file_dialog('font'))
        elif process_type == "font_size"       : self.text_area.setCurrentFont(self.__file_dialog('font'))
        elif process_type == "font_color"      : self.text_area.setTextColor(self.__file_dialog("color").getColor())
        elif process_type == "background_color": self.text_area.setTextBackgroundColor(self.__file_dialog("color").getColor())
        elif process_type == "indent"          : self.text_area.insertPlainText(''.join([f'\t{i}\n' for i in text_area_text.split('\n')]))
        elif process_type == "outdent"         : self.text_area.insertPlainText(''.join(i[i.find('\t')+1:]+"\n" for i in text_area_text.split('\n')))
        elif process_type == "insert_link"     : 
            if "href" in text_area_html:
                self.text_area.insertHtml(text_area_html.replace(text_area_html, text_area_text))
            else:
                self.text_area.insertHtml(f'<a href="{self.__file_dialog("link")[0]}">{text_area_html}</a>')
        elif process_type == "insert_image"    : 
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Information)
            message_box.setWindowTitle("Insert Image")
            message_box.setText("Do you want to add an image from a file or from the internet?")
            message_box.addButton("File", QMessageBox.AcceptRole)
            message_box.addButton("Internet", QMessageBox.RejectRole)
            if message_box.exec_() == QMessageBox.AcceptRole:
                file_dialog = self.__file_dialog("image")
                if file_dialog.strip() != '':
                    self.text_area.insertHtml(f'<img src="{file_dialog}"><p></p>')
            else:
                file_dialog = self.__file_dialog("i_link")
                if file_dialog[1]:
                    self.text_area.insertHtml(f'<img src="{file_dialog[0]}"><p></p>')
        elif process_type == "bullet_list"     : self.text_area.textCursor().insertList(QTextListFormat.ListDisc)
        elif process_type == "number_list"     : self.text_area.textCursor().insertList(QTextListFormat.ListDecimal)
        elif process_type == "insert_code"     : self.__insert_code()

        elif process_type == "settings"        : self.__settings_window()
        elif process_type == "source_code"     : self.__source_code_window()

        settings = {}
        if process_type == "update" :
            
            settings['Bold'] = True if "600;" in text_area_html else False
            settings['Italic'] = True if "italic;" in text_area_html else False
            settings['Underline'] = True if "underline;" in text_area_html else False
            settings['Align Left'] = True if self.text_area.alignment() == Qt.AlignLeft else False
            settings['Align Center'] = True if self.text_area.alignment() == Qt.AlignCenter else False
            settings['Align Right'] = True if self.text_area.alignment() == Qt.AlignRight else False
            settings['Align Justify'] = True if self.text_area.alignment() == Qt.AlignJustify else False
            settings['Indent'] = True if text_area_text.startswith('\t') else False
            settings['Insert Link'] = True if "href" in text_area_html else False
            settings['Insert Image'] = True if "src" in text_area_html else False
            
            for button in self.action_buttons:
                if button.text() in settings.keys():
                    if settings[button.text()]: button.setChecked(True)
                    else: button.setChecked(False)
    def __settings_window(self):
        try   : self.insert_code_window.deleteLater()
        except: pass
        try   : self.settings_window.deleteLater()
        except: pass
        
        self.settings_window = QDialog(self)
        if self.__DEFAULT_STYLE is not None:apply_stylesheet(self.settings_window, self.__DEFAULT_STYLE)
        self.settings_window.setWindowIcon(QIcon(str(Path(self.__PATH, 'pyqtCuWiAssets', 'QHtmlTextEditor', 'settings.png'))))
        self.settings_window.setWindowTitle('Settings')
        self.settings_window.layout = QGridLayout()
        self.settings_window.setLayout(self.settings_window.layout)

        lens = []
        for menu_type in self.__SETTINGS['menuBar'].keys():
            lens.append(len(self.__SETTINGS['menuBar'][menu_type]))
            self.settings_window.layout.addWidget(QLabel(menu_type.capitalize()), 0, list(self.__SETTINGS['menuBar'].keys()).index(menu_type), alignment=Qt.AlignCenter)
            for button in self.__SETTINGS['menuBar'][menu_type].keys():
                checkBox = QCheckBox(self.__SETTINGS['menuBar'][menu_type][button]['text'])
                checkBox.setChecked(self.__SETTINGS['menuBar'][menu_type][button]['show'])
                checkBox.stateChanged.connect(lambda ch, checkBox=checkBox ,menu_type=menu_type, button=button: self.__change_settings(checkBox, menu_type, button)) 

                self.settings_window.layout.addWidget(checkBox, list(self.__SETTINGS['menuBar'][menu_type].keys()).index(button)+1, list(self.__SETTINGS['menuBar'].keys()).index(menu_type))
        
        apply_settings = QPushButton("Apply")
        apply_settings.clicked.connect(lambda: self.__apply_settings(self.__SETTINGS_FILE))
        self.settings_window.layout.addWidget(apply_settings, max(lens)+1, len(list(self.__SETTINGS['menuBar'].keys()))-1)
        
        self.settings_window.show()
    def __change_settings(self, checkBox, menu_type, button): 
        self.__SETTINGS['menuBar'][menu_type][button]['show'] = checkBox.isChecked()
    def __apply_settings(self, settings): 
        writeJ(settings, str(Path(self.__PATH, 'pyqtCuWiDatabase', 'settings.json')))
        self.__HTML_CODE = self.text_area.toHtml()
        self.__widgets()
        self.text_area.setHtml(self.__HTML_CODE)
    def __source_code_window(self):
        if self.__SOURCE_CODE_SHOW:
            try   : self.insert_code_window.deleteLater()
            except: pass
            try   : self.settings_window.deleteLater()
            except: pass
            self.text_area.setPlainText(self.__HTML_CODE)
            self.text_area.setReadOnly(True)
            self.__SOURCE_CODE_SHOW = False
            for button in self.action_buttons:
                if button.text() == 'Source Code':
                    button.setIcon(QIcon(str(Path(self.__PATH, 'pyqtCuWiAssets', 'QHtmlTextEditor', 'show_source_code.png'))))
                else:
                    button.setEnabled(False)
            self.copy_button.show()
        else:
            self.text_area.setHtml(self.__TEXT)
            self.text_area.setReadOnly(False)
            self.__SOURCE_CODE_SHOW = True
            for button in self.action_buttons:
                if button.text() == 'Source Code':
                    button.setIcon(QIcon(str(Path(self.__PATH, 'pyqtCuWiAssets', 'QHtmlTextEditor', 'hide_source_code.png'))))
                else:
                    button.setEnabled(True)
            self.copy_button.hide()
        
    def __insert_code(self):
        try   : self.insert_code_window.deleteLater()
        except: pass
        try   : self.settings_window.deleteLater()
        except: pass
        self.insert_code_window = QSyntaxHighlight(self)
        if self.__DEFAULT_STYLE is not None:apply_stylesheet(self.insert_code_window, self.__DEFAULT_STYLE)
        self.insert_code_window.setWindowTitle('Insert Code')
        self.insert_code_window.setWindowIcon(QIcon(str(Path(self.__PATH, 'pyqtCuWiAssets', 'QHtmlTextEditor', 'insert_code.png'))))
        self.insert_code_window.show()

        self.insert_code_window.copy.setText('Apply')
        @self.insert_code_window.copy.clicked.connect
        def func():
            html = self.insert_code_window.output.toHtml()
            html = html[:-14]+"\n<p></p>"+html[-14:]
            self.text_area.insertHtml(html)
            self.insert_code_window.deleteLater() 
    
    def __file_dialog(self, dialog_type):
        if   dialog_type == 'save'  : return QFileDialog.getSaveFileName(self, "Save", "", "Hypertext Markup Language (*.html);;" "Text Document (*.txt)")
        elif dialog_type == 'open'  : return QFileDialog.getOpenFileName(self, "Open Page", "","Hypertext Markup Language (*.html);;" "Text Document (*.txt)")
        elif dialog_type == 'font'  : return QFontDialog.getFont()[0]
        elif dialog_type == 'color' : return QColorDialog()
        elif dialog_type == 'link'  : return QInputDialog.getText(self, 'Insert Link', 'Link:')
        elif dialog_type == 'image' : return QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.jpg *.png *.bmp *.gif)")[0]
        elif dialog_type == 'i_link': return QInputDialog.getText(self, 'Insert Image Link', 'Image Link:')
        elif dialog_type == 'quit'  : return QMessageBox.question(self, 'Quit', 'Are you sure you want to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    
    def getAllActionButton(self)                   -> list : return self.action_buttons
    def getSourceCode(self)                        -> str  : return self.__HTML_CODE
    def getFileName(self)                          -> str  : return self.__FILE_NAME 
    def changeStatusChangeTitle(self, status:bool) -> None : self.__CHANGE_TITLE_STATUS = status
    def setDefaultStyle(self, style:'pyqtCuWi.pyqtCuWiColor.QTheme') -> None : 
        if style in pyqtCuWi.pyqtCuWiColor.QTheme().getAllThemes():
            apply_stylesheet(self, style)
            self.__DEFAULT_STYLE = style
        else:
            raise pyqtCuWiInvaledType("Theme",style, pyqtCuWi.pyqtCuWiColor.QTheme().getAllThemes())