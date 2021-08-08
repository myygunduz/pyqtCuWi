#          Custom Widgets For PyQt5 Module           #
#          GPL 3.0 - myygunduz - pyqtCuWi            #
#        https://github.com/myygunduz/pyqtCuWi       #

class FailedToAddTitleType(Exception):
    def __init__(self): 
        
        self.message = f"\n\nError Message:\n'''\nFailed to add title type. The data you are trying to enter may have these problems.\n1-) The length of the tuple is longer or shorter than 3.\n2-) The key string is not a value.\n3-) The value is not a tuple.\n'''"
        super().__init__(self.message)