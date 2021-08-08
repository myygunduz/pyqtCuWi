#          Custom Widgets For PyQt5 Module           #
#          GPL 3.0 - myygunduz - pyqtCuWi            #
#        https://github.com/myygunduz/pyqtCuWi       #

class InvalidStyleVariable(Exception):
    def __init__(self,invalidVariable,variableList): 
        
        self.message = f"\n\nError Message:\n'''\nStyle variable '{invalidVariable}' is invalid. Try using:\n{list(variableList)}\n'''"
        super().__init__(self.message)