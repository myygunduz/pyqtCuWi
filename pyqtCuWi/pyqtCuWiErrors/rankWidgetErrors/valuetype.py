#          Custom Widgets For PyQt5 Module           #
#          GPL 3.0 - myygunduz - pyqtCuWi            #
#        https://github.com/myygunduz/pyqtCuWi       #

class InvalidValueType(Exception):
    def __init__(self): 
        self.message = "\n\nError Message:\n'''\nValue type can be true, false, bool.\n'''"
        super().__init__(self.message)