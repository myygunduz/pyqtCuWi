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

