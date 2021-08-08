#          Custom Widgets For PyQt5 Module           #
#          GPL 3.0 - myygunduz - pyqtCuWi            #
#        https://github.com/myygunduz/pyqtCuWi       #

class InvalidButtonStyleType(Exception):
    def __init__(self): 
        super().__init__(f"\n\nError Message:\n'''\nButton style type must be 'default', 'hover' or 'press'.\n'''")