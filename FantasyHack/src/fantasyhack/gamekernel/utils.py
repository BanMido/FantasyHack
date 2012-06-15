# -*- coding: utf-8 -*-

'''
Created on Jun 13, 2012

@author: BanMido
'''

import common


class GameTurnCounter (object):

    """
    
    """

    def __init__ (self, **kwargs):
        super (GameTurnCounter, self).__init__ (**kwargs)
        self.__turnCount = 0


    def incrementTurnCount (self, **kwargs):
        if "increment" in kwargs and int (kwargs["increment"]) > 0:
            self.__turnCount = self.__turnCount + int (kwargs["increment"])
        else:
            self.__turnCount = self.__turnCount + 1


    def turnCount (self):
        return self.__turnCount



class GameObjectPosition (object):

    """
    
    """

    def __init__ (self, **kwargs):
        super (GameObjectPosition, self).__init__ (**kwargs)
        self.__position = dict ({"row" : 0, "col" : 0})


    def row (self):
        return self.__position["row"]


    def column (self):
        return self.__position["col"]


    def update (self, **kwargs):
        if "row" in kwargs and common.isRowWithinBounds (kwargs["row"]):
            self.__position["row"] = int (kwargs["row"])

        if "col" in kwargs and common.isColumnWithinBounds (kwargs["col"]):
            self.__position["col"] = int (kwargs["col"])


    def setPosition (self, r, c):
        if common.isRowWithinBounds (r) and common.isColumnWithinBounds (c):
            self.update (row=r)
            self.update (col=c)

