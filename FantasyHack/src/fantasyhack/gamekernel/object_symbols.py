# -*- coding: utf-8 -*-

'''
Created on Jun 13, 2012

@author: BanMido
'''

class SymbolMap (object):

    """
    
    """

    __numSymbols = 25
    __defaultSymbolMap = (
                            {
                            0  : u" ",      # Empty space
                            1  : u"@",      # Player
                            2  : u".",      # Empty floor space
                            3  : u"#",      # Empty corridor space
                            4  : u"\u2500", # Vertical wall
                            5  : u"\u2502", # Horizontal wall
                            6  : u"\u250c", # Upper left corner wall
                            7  : u"\u2510", # Upper right corner wall
                            8  : u"\u2514", # Lower left corner wall
                            9  : u"\u2518", # Lower right corner wall
                            10 : u"\u251c", # Vertical and right intersecting wall
                            11 : u"\u2524", # Vertical and left intersecting wall
                            12 : u"\u252c", # Horizontal and down intersecting wall
                            13 : u"\u2534", # Horizontal and up intersecting wall
                            14 : u"\u253c", # Horizontal and vertical intersecting wall
                            15 : u"\u2592", # Open door
                            16 : u"\u2573", # Closed door
                            17 : u"[",
                            18 : u"(",
                            19 : u"%",
                            20 : u">",
                            21 : u"<",
                            22 : u"",
                            23 : u"",
                            24 : u"",
                            }
                         )


    def __init__ (self, **kwargs):
        super (SymbolMap, self).__init__ (**kwargs)
        self.__symbolMap = SymbolMap.__defaultSymbolMap


    def symbol (self, idx):
        i = int (idx)
        sym = self.__symbolMap[i]

        return sym


    def setSymbolMap (self, symbolMap):
        if len (symbolMap) != SymbolMap.__numSymbols:
            errStr = "Expected mapping type object with exactly %s entries" % (SymbolMap.__numSymbols)
            raise ValueError (errStr)

        for key in symbolMap:
            self.__symbolMap[key] = symbolMap[key]

