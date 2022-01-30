from PyQt5.QtWidgets import QApplication
from pyqtCuWi import QSyntaxHighlight, pyqtCuWiColor

app = QApplication([])
win = QSyntaxHighlight()
win.setWindowTitle('Code Highlight')
win.setDefaultStyle(pyqtCuWiColor.QTheme().DARK_RED)
win.show()
app.exec_()
        