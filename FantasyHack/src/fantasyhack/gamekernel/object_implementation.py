# -*- coding: utf-8 -*-

'''
Created on Jun 13, 2012

@author: BanMido 
'''

import common 
import copy
import object_base
import world


class WallOrientation (object):

    """
    
    """

    __orientationVertical, __orientationHorizontal,                             \
    __orientationUpperLeftCorner, __orientationUpperRightCorner,                \
    __orientationLowerLeftCorner, __orientationLowerRightCorner,                \
    __orientationVerticalRightIntersect, __orientationVerticalLeftIntersect,    \
    __orientationHorizontalDownIntersect, __orientationHorizontalUpIntersect,   \
    __orientationHorizontalVerticalIntersect = range (11)


    @staticmethod
    def validValues ():
        return (WallOrientation.__orientationVertical,
                WallOrientation.__orientationHorizontal,
                WallOrientation.__orientationUpperLeftCorner,
                WallOrientation.__orientationUpperRightCorner,
                WallOrientation.__orientationLowerLeftCorner,
                WallOrientation.__orientationLowerRightCorner,
                WallOrientation.__orientationVerticalRightIntersect,
                WallOrientation.__orientationVerticalLeftIntersect,
                WallOrientation.__orientationHorizontalDownIntersect,
                WallOrientation.__orientationHorizontalUpIntersect,
                WallOrientation.__orientationHorizontalVerticalIntersect,
               )


    @staticmethod
    def vertical ():
        return WallOrientation.__orientationVertical


    @staticmethod
    def horizontal ():
        return WallOrientation.__orientationHorizontal


    @staticmethod
    def upperLeftCorner ():
        return WallOrientation.__orientationUpperLeftCorner


    @staticmethod
    def upperRightCorner ():
        return WallOrientation.__orientationUpperRightCorner


    @staticmethod
    def lowerLeftCorner ():
        return WallOrientation.__orientationLowerLeftCorner


    @staticmethod
    def lowerRightCorner ():
        return WallOrientation.__orientationLowerRightCorner


    @staticmethod
    def verticalRightIntersect ():
        return WallOrientation.__orientationVerticalRightIntersect


    @staticmethod
    def verticalLeftIntersect ():
        return WallOrientation.__orientationVerticalLeftIntersect


    @staticmethod
    def horizontalDownIntersect ():
        return WallOrientation.__orientationHorizontalDownIntersect


    @staticmethod
    def horizontalUpIntersect ():
        return WallOrientation.__orientationHorizontalUpIntersect


    @staticmethod
    def horizontalVerticalIntersect ():
        return WallOrientation.__orientationHorizontalVerticalIntersect



class Wall (object_base.GameObject):

    """
    
    """

    def __init__ (self, orientation, isDiggable, **kwargs):
        super (Wall, self).__init__ (**kwargs)

        if orientation in WallOrientation.validValues () == False:
            errStr = "Expected a value from the following set (%s)" % \
                (",".join ([repr (x) for x in WallOrientation.validValues ()]))
            raise ValueError (errStr)

        self.__orientation = orientation
        self.setTag (common.Tag.destructible (), bool (isDiggable))


    def objectType (self):
        return common.GameObjectType.wall ()


    def symbolMapIndex (self):
        return ObjectSymbolMap.symbolWall (self.__orientation)


    def orientation (self):
        return self.__orientation



class Floor (object_base.GameObject):

    """
    
    """

    def __init__ (self, isDiggable, isCorridor, pile, **kwargs):
        super (Floor, self).__init__ (**kwargs)
        self.setTag (common.Tag.destructible (), bool (isDiggable))
        self.__isCorridor = bool (isCorridor)
        self.__pile = copy.deepcopy (pile)


    def objectType (self):
        return common.GameObjectType.floor ()


    def symbolMapIndex (self):
        return ObjectSymbolMap.symbolFloor (self.__pile, self.__isCorridor)


    def isCorridor (self):
        return self.__isCorridor


    def pile (self):
        return copy.deepcopy (self.__pile)


    def clearPile (self):
        del self.__pile[:]


    def removeFromPile (self, uid):
        self.__pile.remove (int (uid))




class StairOrientation (object):

    """
    
    """

    __stairDown, __stairUp = range (2)


    @staticmethod
    def validValues ():
        return (StairOrientation.__stairDown, StairOrientation.__stairUp)


    @staticmethod
    def stairDown ():
        return StairOrientation.__stairDown


    @staticmethod
    def stairUp ():
        return StairOrientation.__stairUp



class Stair (object_base.GameObject):

    """
    
    """

    def __init__ (self, orientation, **kwargs):
        super (Stair, self).__init__ (**kwargs)

        if orientation in StairOrientation.validValues () == False:
            errStr = "Expected a value from the following set (%s)" % \
                (",".join ([repr (x) for x in StairOrientation.validValues ()]))
            raise ValueError (errStr)

        self.__orientation = orientation


    def objectType (self):
        return common.GameObjectType.stair ()


    def symbolMapIndex (self):
        return ObjectSymbolMap.symbolStair (self.__orientation)


    def orientation (self):
        return self.__orientation



class Monster (object_base.GameObject):

    """
    
    """

    def __init__ (self, status, inventory, **kwargs):
        super (Monster, self).__init__ (**kwargs)

        if isinstance(status, object_base.MonsterStatus) == False:
            errStr = "Expecting an instance of 'MonsterStatus', got an instance of %s" % repr (type (status))
            raise TypeError (errStr)

        if isinstance (inventory, set) == False:
            errStr = "Expecting an instance of 'set', got an instance of %s" % \
                repr (type (status))
            raise TypeError (errStr)

        self.__status = copy.deepcopy (status)
        self.__inventory = copy.deepcopy (inventory)


    def objectType(self):
        return common.GameObjectType.monster ()


    def symbolMapIndex(self):
        return ObjectSymbolMap.symbolMonster ()



class ObjectSymbolMap (object):

    """
    
    """

    @staticmethod
    def symbolWall (orientation):
        if orientation == WallOrientation.vertical ():
            return 4
        elif orientation == WallOrientation.horizontal ():
            return 5
        elif orientation == WallOrientation.upperLeftCorner ():
            return 6
        elif orientation == WallOrientation.upperRightCorner ():
            return 7
        elif orientation == WallOrientation.lowerLeftCorner ():
            return 8
        elif orientation == WallOrientation.lowerRightCorner ():
            return 9
        elif orientation == WallOrientation.verticalRightIntersect ():
            return 10
        elif orientation == WallOrientation.verticalLeftIntersect ():
            return 11
        elif orientation == WallOrientation.horizontalDownIntersect ():
            return 12
        elif orientation == WallOrientation.horizontalUpIntersect ():
            return 13
        elif orientation == WallOrientation.horizontalVerticalIntersect ():
            return 14
        else:
            return 0


    @staticmethod
    def symbolFloor (pile, isCorridor):
        if len (pile) != 0:
            return world.lookupMasterObjectInventory(pile[-1]).symbolMapIndex ()
        else:
            if bool (isCorridor) == False:
                return 2
            else:
                return 3

        return 0


    @staticmethod
    def symbolStair (orientation):
        if orientation == StairOrientation.stairDown ():
            return 20

        if orientation == StairOrientation.stairUp ():
            return 21

        return 0


    @staticmethod
    def symbolMonster ():
        return 1

