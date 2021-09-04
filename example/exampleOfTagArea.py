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