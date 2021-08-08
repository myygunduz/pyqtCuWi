#          Custom Widgets For PyQt5 Module           #
#          GPL 3.0 - myygunduz - pyqtCuWi            #
#        https://github.com/myygunduz/pyqtCuWi       #

class NoIconSize(Exception):
    def __init__(self): 
        self.message = "\n\nError Message:\n'''\nIcon size not specified. Either enter the 'iconSize' parameter.\n'''"
        super().__init__(self.message)