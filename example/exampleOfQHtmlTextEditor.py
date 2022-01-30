from PyQt5.QtWidgets import QApplication
from pyqtCuWi import QHtmlTextEditor

app = QApplication([])
win = QHtmlTextEditor()
win.setWindowTitle('PyQt5 Text Editor')
win.show()
app.exec_()
        