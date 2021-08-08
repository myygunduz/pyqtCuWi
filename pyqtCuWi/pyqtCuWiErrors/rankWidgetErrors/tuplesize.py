#          Custom Widgets For PyQt5 Module           #
#          GPL 3.0 - myygunduz - pyqtCuWi            #
#        https://github.com/myygunduz/pyqtCuWi       #

class TupleSizeError(Exception):
    def __init__(self,trueSize, outerRadius = None):
        self.message = f"\n\nError Message:\n'''\nTuple length should not be longer than {trueSize}.\n'''"
        if outerRadius != None:
            self.message = f"\n\nError Message:\n'''\nTuple length must be {trueSize}.\n'''"
        super().__init__(self.message)