#          Custom Widgets For PyQt5 Module           #
#          GPL 3.0 - myygunduz - pyqtCuWi            #
#        https://github.com/myygunduz/pyqtCuWi       #

class SizeError(Exception):
    def __init__(self,mainSize,inputSize): 
        self.message = f"\n\nError Message:\n'''\nThe icon size must be smaller than the main size. Try changing the size of the button. Button size = '{mainSize}', Size entered = '{inputSize}'\n'''"
        super().__init__(self.message)