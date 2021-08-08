#          Custom Widgets For PyQt5 Module           #
#          GPL 3.0 - myygunduz - pyqtCuWi            #
#        https://github.com/myygunduz/pyqtCuWi       #

class InvalidTitleType(Exception):
    def __init__(self,invalidVariable,typeList): 
        
        self.message = f"\n\nError Message:\n'''\nTitle type '{invalidVariable}' is invalid. Try using:\n{typeList}\n'''"
        super().__init__(self.message)