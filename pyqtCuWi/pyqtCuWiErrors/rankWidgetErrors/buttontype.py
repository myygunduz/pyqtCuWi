#          Custom Widgets For PyQt5 Module           #
#          GPL 3.0 - myygunduz - pyqtCuWi            #
#        https://github.com/myygunduz/pyqtCuWi       #

class InvalidButtonType(Exception):
    def __init__(self): 
        self.message = "\n\nError Message:\n'''\nButton type can be upArrow, downArrow, rightArrow, leftArrow, trash.\n'''"
        super().__init__(self.message)