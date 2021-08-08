#          Custom Widgets For PyQt5 Module           #
#          GPL 3.0 - myygunduz - pyqtCuWi            #
#        https://github.com/myygunduz/pyqtCuWi       #

class InvalidLayoutType(Exception):
    def __init__(self): 
        super().__init__(f"\n\nError Message:\n'''\nLayout type must be 'V' or 'H'.\n'''")