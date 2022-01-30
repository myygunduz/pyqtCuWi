#          Custom Widgets For PyQt5 Module           #
#          GPL 3.0 - myygunduz - pyqtCuWi            #
#        https://github.com/myygunduz/pyqtCuWi       #

#iconButton
class NoIcon(Exception):
    def __init__(self,operation): 

        super().__init__(f"\n\nError Message:\n'''\n{operation}\n'''")

class NoIconSize(Exception):
    def __init__(self): 

        self.message = "\n\nError Message:\n'''\nIcon size not specified. Either enter the 'iconSize' parameter.\n'''"
        super().__init__(self.message)

class SizeError(Exception):
    def __init__(self,mainSize,inputSize): 

        self.message = f"\n\nError Message:\n'''\nThe icon size must be smaller than the main size. Try changing the size of the button. Button size = '{mainSize}', Size entered = '{inputSize}'\n'''"
        super().__init__(self.message)

class UndefinedDirection(Exception):
    def __init__(self): 

        self.message = "\n\nError Message:\n'''\nDirection value must be 'left' or 'right'.\n'''"
        super().__init__(self.message)

#popUp
class FailedToAddTitleType(Exception):
    def __init__(self): 

        self.message = f"\n\nError Message:\n'''\nFailed to add title type. The data you are trying to enter may have these problems.\n1-) The length of the tuple is longer or shorter than 3.\n2-) The key string is not a value.\n3-) The value is not a tuple.\n'''"
        super().__init__(self.message)

class InvalidStyleVariable(Exception):
    def __init__(self,invalidVariable,variableList): 

        self.message = f"\n\nError Message:\n'''\nStyle variable '{invalidVariable}' is invalid. Try using:\n{list(variableList)}\n'''"
        super().__init__(self.message)

#global
class pyqtCuWiInvaledType(Exception):
    def __init__(self,value_type,invalid_value,valid_values): 
        self.message = f"{value_type} type '{invalid_value}' is invalid. Try using:\n"+"".join(f"{valid_value}\n" for valid_value in valid_values)
        super().__init__(self.message)
    
class TupleSizeError(Exception):
    def __init__(self,trueSize, outerRadius = None):

        self.message = f"\n\nError Message:\n'''\nTuple length should not be longer than {trueSize}.\n'''"
        if outerRadius != None:
            self.message = f"\n\nError Message:\n'''\nTuple length must be {trueSize}.\n'''"
        super().__init__(self.message)