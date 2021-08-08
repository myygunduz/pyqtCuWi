#          Custom Widgets For PyQt5 Module           #
#          GPL 3.0 - myygunduz - pyqtCuWi            #
#        https://github.com/myygunduz/pyqtCuWi       #

class InvalidStyleType(Exception):
    def __init__(self,invalidType,typeList): 
        
        self.message = f"\n\nError Message:\n'''\nStyle type '{invalidType}' is invalid. Try using:\n{list(typeList)}\n'''"
        super().__init__(self.message)