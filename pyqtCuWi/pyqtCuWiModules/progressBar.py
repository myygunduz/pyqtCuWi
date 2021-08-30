#          Custom Widgets For PyQt5 Module           #
#          GPL 3.0 - myygunduz - pyqtCuWi            #
#        https://github.com/myygunduz/pyqtCuWi       #


from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtCore import pyqtSignal, QTimer

class ProgressBar(QProgressBar):
    signal = pyqtSignal()
    finished = pyqtSignal()
    def __init__(self, *args, **kwargs):
        super(ProgressBar, self).__init__(*args, **kwargs)
        self.setValue(0)
        if self.minimum() != self.maximum():
            self.timer = QTimer(self, timeout=self.onTimeout)
            self.timer.start(1 * 1000)

    def onTimeout(self):
        if self.value() >= self.maximum():
            self.finished.emit()
            self.timer.stop()
            self.timer.deleteLater()
            del self.timer
            return
        self.setValue(self.value() + 1)
        self.signal.emit()