#                  Custom Widgets For PyQt5 Module                   #
#                   GPL 3.0 - myygunduz - pyqtCuWi                   #
#                https://github.com/myygunduz/pyqtCuWi               #
# https://gist.github.com/myygunduz/3a7c4bb459ce6b059d667ea17e59f033 #

def clearOfList(InputList:list) -> list :
    Output = []
    def operation(lista:list):
        for i in lista:
            if isinstance(i,list):
                operation(i)
            else:
                Output.append(i)
    operation(InputList)
    return Output