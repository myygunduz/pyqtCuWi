#          Custom Widgets For PyQt5 Module           #
#          GPL 3.0 - myygunduz - pyqtCuWi            #
#        https://github.com/myygunduz/pyqtCuWi       #
#                                                    #
#                   QFreeBoxLayout                   #


from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt

# QFreeBoxLayout. Widget but its name is layout.
class QFBoxLayout(QWidget):
    def __init__(self):
        super().__init__()
        self._widgets = {}
        self._spacing = 2
        self._Alignment = Qt.TopLeftCorner

    def __repr__(self):
        return '<pyqtCuWi.QFBoxLayout()>'
    def addWidget(self, widget:QWidget) -> None:
        """
        TopLeftCorner = 0 # type: Qt.Corner
        TopRightCorner = 1 # type: Qt.Corner
        BottomLeftCorner = 2 # type: Qt.Corner
        BottomRightCorner = 3 # type: Qt.Corner
        """
        if self._Alignment == 0 : # self._Alignment == Qt.TopLeftCorner
            start_position_x = 0
            start_position_y = 0

        elif self._Alignment == 1: # self._Alignment == Qt.TopRightCorner
            start_position_x = (self.width()-widget.sizeHint().width())
            start_position_y = 0
        
        elif self._Alignment == 2: # self._Alignment == Qt.BottomLeftCorner
            start_position_x = 0
            start_position_y = (self.height()-widget.sizeHint().height())
        
        elif self._Alignment == 3: # self._Alignment == Qt.BottomRightCorner
            start_position_x = (self.width()-widget.sizeHint().width())
            start_position_y = (self.height()-widget.sizeHint().height())

        if self._widgets == {}:
            """
                If it is the first widget to show on the screen without doing math.
            """
            self._widgets[widget] = {
                'lu':(start_position_x, start_position_y),
                'ld':(start_position_x, widget.sizeHint().height() + start_position_y),
                'ru':(widget.sizeHint().width() + start_position_x, start_position_y),
                'rd':(widget.sizeHint().width() + start_position_x, widget.sizeHint().height() + start_position_y),
                'column': 0
            }
            widget.move(start_position_x, start_position_y)
            widget.show()
        else:
            last_Widget = self._widgets[list(self._widgets.keys())[-1]]

            widget_Height = widget.geometry().height()
            widget_Width = widget.sizeHint().width()
            position_Y = last_Widget['lu'][1]
            left_position = last_Widget['ru'][0]+self._spacing if self._Alignment == 0 or self._Alignment == 2 else (last_Widget['lu'][0]-self._spacing)-widget_Width
            right_position = widget_Width+last_Widget['ru'][0]+self._spacing if self._Alignment == 0 or self._Alignment == 2 else (last_Widget['lu'][0]-self._spacing)
            self._widgets[widget] = {
                                    'lu':(left_position, position_Y),
                                    'ld':(left_position, (widget_Height+position_Y)),
                                    'ru':(right_position, position_Y),
                                    'rd':(right_position, (widget_Height+position_Y)),
                                    'column':last_Widget['column']
                                    }


            position_X = last_Widget['ru'][0] + self._spacing if self._Alignment == 0 or self._Alignment == 2 else last_Widget['lu'][0]-widget.sizeHint().width()-self._spacing
            check_number = self.width() if self._Alignment == 0 or self._Alignment == 2 else 0

            if position_X <= check_number <= widget_Width + position_X:
                """
                    If the button does not fit in the widget, it can be added to a bottom or a top.

                    The purpose of 'yList' is to keep the height of all widgets in the old column.
                    The maximum of these heights will determine the starting point of the new column.
                """
                positions_Y = []
                for i in self._widgets:
                    if self._widgets[i]['column'] == last_Widget['column']:
                        
                        if self._Alignment == 0 or self._Alignment == 1:
                            # If alignment equals TopLeftCorner or TopRightCorner. Height positions of bottom left are added to ylist.
                            positions_Y.append(self._widgets[i]['ld'][1])
                        else:
                            # If alignment equals BottomLeftCorner or BottomRightCorner. Height positions of top left are added to ylist.
                            positions_Y.append(self._widgets[i]['lu'][1])
                        
                position_Y = max(positions_Y) + self._spacing if self._Alignment == 0 or self._Alignment == 1 else (max(positions_Y) - self._spacing) - widget_Height
                
                self._widgets[widget] = {
                                        'lu':(start_position_x, position_Y),
                                        'ld':(start_position_x, (widget_Height + position_Y)),
                                        'ru':(widget_Width + start_position_x, position_Y),
                                        'rd':(widget_Width + start_position_x, (widget_Height + position_Y)),
                                        'column':last_Widget['column']+1
                                        }

                position_X = start_position_x
        
            widget.move(position_X,position_Y)

            widget.show()

    def removeWidget(self, widget:QWidget) -> None:
        #   Delete Widget
        del self._widgets[widget]
        widget.deleteLater()
        self.__reflesh()

    def setSpacing(self, value:int) ->  None:
        #    Sets value of spacing.
        self._spacing = value

    def setAlignment(self, flag:Qt.Corner) -> None:

        if type(flag) == Qt.Corner:
            self._Alignment = flag
            self.__reflesh()
        else:
            raise  TypeError("Use Qt.Corner")

    def resizeEvent(self, event):
        #    If the size of the widget changes, it will be placed according to its new size.
        self.__reflesh()

    def __reflesh(self):
        #    Relocation
        widgets = list(self._widgets.keys())
        self._widgets = {}
        for i in widgets:
            self.addWidget(i)

    def __developerNotes(self):
        pass
    """
                widget frame
    lu ->   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   <- ru
            █                 █
            █                 █
            █                 █
            █                 █
            █                 █
            █                 █
            █                 █
    ld ->   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀   <- rd

    lu = left up        ru = right up
    ld = left down      rd = right down    
    example : 'first widget info'

    if self._Alignment == Qt.TopLeftCorner:
        self._widgets = {"widget":{"lu":(0, 0),
                                    "ld":(0, widget.height()),
                                    "ru":(widget.width(), 0),
                                    "rd":(widget.width(), widget.height()),
                                    'column': 0
                                    }
                        }
    elif self._Alignment == Qt.TopRightCorner:
        self._widgets = {"widget":{"lu":(self.width() - widget.width(), 0),
                                    "ld":(self.width() - widget.width(), widget.height()),
                                    "ru":(self.width(), 0),
                                    "rd":(self.width(), widget.height()),
                                    'column': 0
                                    }
                        }
    elif self._Alignment == Qt.BottomLeftCorner:
        self._widgets = {"widget":{"lu":(0, widget.height() - self.height()),
                                    "ld":(0, self.height()),
                                    "ru":(widget.width(), widget.height() - self.height()),
                                    "rd":(widget.width(), self.height()),
                                    'column': 0
                                    }
                        }
    elif self._Alignment == Qt.BottomRightCorner:
        self._widgets = {"widget":{"lu":(self.width() - widget.width(), widget.height() - self.height()),
                                    "ld":(self.width() - widget.width(), self.height()),
                                    "ru":(self.width(), widget.height() - self.height()),
                                    "rd":(self.width(), self.height()),
                                    'column': 0
                                    }
                        }
    """