#          Custom Widgets For PyQt5 Module           #
#          GPL 3.0 - myygunduz - pyqtCuWi            #
#        https://github.com/myygunduz/pyqtCuWi       #

class UndefinedDirection(Exception):
    def __init__(self): 
        self.message = "\n\nError Message:\n'''\nDirection value must be 'left' or 'right'.\n'''"
        super().__init__(self.message)