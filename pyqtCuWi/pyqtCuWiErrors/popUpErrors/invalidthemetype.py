#          Custom Widgets For PyQt5 Module           #
#          GPL 3.0 - myygunduz - pyqtCuWi            #
#        https://github.com/myygunduz/pyqtCuWi       #

class InvalidThemeType(Exception):
    def __init__(self,invalidVariable,themeList): 
        
        self.message = f"\n\nError Message:\n'''\Theme type '{invalidVariable}' is invalid. Try using:\n{themeList}\n'''"
        super().__init__(self.message)