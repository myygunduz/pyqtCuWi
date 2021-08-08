#          Custom Widgets For PyQt5 Module           #
#          GPL 3.0 - myygunduz - pyqtCuWi            #
#        https://github.com/myygunduz/pyqtCuWi       #

class InvalidValue(Exception):
    def __init__(self,falseValue,trueValue): 
        self.message = f"\n\nError Message:\n'''\nValue type '{falseValue}' is invalid. Must be '{trueValue}'\n'''"
        super().__init__(self.message)