# -*- coding: utf-8 -*-

'''
Created on Jun 13, 2012

@author: BanMido 
'''

class GameConstants (object):

    """
    
    """

    __levelRows = 25
    __levelCols = 80
    __minRoomRows = 4
    __maxRoomRows = 8
    __minRoomCols = 4
    __maxRoomCols = 14


    @staticmethod
    def levelRows ():
        return GameConstants.__levelRows


    @staticmethod
    def levelCols ():
        return GameConstants.__levelCols


    @staticmethod
    def minRoomRows ():
        return GameConstants.__minRoomRows


    @staticmethod
    def maxRoomRows ():
        return GameConstants.__maxRoomRows


    @staticmethod
    def minRoomCols ():
        return GameConstants.__minRoomCols


    @staticmethod
    def maxRoomCols ():
        return GameConstants.__maxRoomCols



def isRowWithinBounds (row):
    rowValue = int (row)
    if rowValue >= 0 and rowValue < GameConstants.levelRows ():
        return True

    return False



def isColumnWithinBounds (col):
    colValue = int (col)
    if colValue >= 0 and colValue < GameConstants.levelCols ():
        return True

    return False



class Beatitude (object):

    """
    
    """

    __unknown, __blessed, __uncursed, __cursed = range (4)


    @staticmethod
    def validValues ():
        return (Beatitude.__unknown,
                Beatitude.__blessed,
                Beatitude.__uncursed,
                Beatitude.__cursed)


    @staticmethod
    def unknown ():
        return Beatitude.__unknown


    @staticmethod
    def blessed ():
        return Beatitude.__blessed


    @staticmethod
    def uncursed ():
        return Beatitude.__uncursed


    @staticmethod
    def cursed ():
        return Beatitude.__cursed



class Alignment (object):

    """
    
    """

    __loyalist, __neutral, __renegade = range (3)


    @staticmethod
    def validValues ():
        return (Alignment.__loyalist,
                Alignment.__neutral,
                Alignment.__renegade)


    @staticmethod
    def loyalist ():
        return Alignment.__loyalist


    @staticmethod
    def neutral ():
        return Alignment.__neutral


    @staticmethod
    def renegade ():
        return Alignment.__renegade



class GameBranch (object):

    """
    
    """

    __primaryBranch, __questBranch = range (2) 
  
 
    @staticmethod
    def validValues ():
        return (GameBranch.__primaryBranch, GameBranch.__questBranch)

 
    @staticmethod
    def primaryBranch ():
        return GameBranch.__primaryBranch
 
 
    @staticmethod
    def questBranch ():
        return GameBranch.__questBranch


 
class Tag (object):

    """
    
    """

    # generic tags
    __visible, __consumable, __container, __destructible, __immovable,  \
    __equipable, __monster = range (0, 7)
    # armor tags
    __corrodable, __durable = range (7, 9)
    # weapon tags
    __oneHanded, __twoHanded, __balanced, __holyDamage, __fireDamage,   \
    __frostDamage = range (9, 15)
    # monster tags
    __hostile, __peaceful, __friendly, __canSee, __canFly = range (15, 20)


    @staticmethod
    def validValues ():
        return (
                Tag.__visible,
                Tag.__consumable,
                Tag.__container,
                Tag.__destructible,
                Tag.__immovable,
                Tag.__equipable,
                Tag.__monster,
                Tag.__corrodable,
                Tag.__durable,
                Tag.__oneHanded,
                Tag.__twoHanded,
                Tag.__balanced,
                Tag.__holyDamage,
                Tag.__fireDamage,
                Tag.__frostDamage,
                Tag.__hostile,
                Tag.__peaceful,
                Tag.__friendly,
                Tag.__canSee,
                Tag.__canFly,
               )


    @staticmethod
    def genericTags ():
        return (
                Tag.__visible,
                Tag.__consumable,
                Tag.__container,
                Tag.__destructible,
                Tag.__immovable,
                Tag.__equipable,
                Tag.__monster,
               )


    @staticmethod
    def armorTags ():
        return (
                Tag.__corrodable,
                Tag.__durable,
               )


    @staticmethod
    def weaponTags ():
        return (
                Tag.__oneHanded,
                Tag.__twoHanded,
                Tag.__balanced,
                Tag.__holyDamage,
                Tag.__fireDamage,
                Tag.__frostDamage,
               )


    @staticmethod
    def monsterTags ():
        return (
                Tag.__hostile,
                Tag.__friendly,
                Tag.__canSee,
                Tag.__canFly,
               )


    @staticmethod
    def visible ():
        return Tag.__visible


    @staticmethod
    def consumable ():
        return Tag.__consumable


    @staticmethod
    def container ():
        return Tag.__container


    @staticmethod
    def destructible ():
        return Tag.__destructible


    @staticmethod
    def immovable ():
        return Tag.__immovable


    @staticmethod
    def equipable ():
        return Tag.__equipable


    @staticmethod
    def monster ():
        return Tag.__monster


    @staticmethod
    def corrodable ():
        return Tag.__corrodable


    @staticmethod
    def durable ():
        return Tag.__durable


    @staticmethod
    def oneHanded ():
        return Tag.__oneHanded


    @staticmethod
    def twoHanded ():
        return Tag.__twoHanded


    @staticmethod
    def balanced ():
        return Tag.__balanced


    @staticmethod
    def holyDamage ():
        return Tag.__holyDamage


    @staticmethod
    def fireDamage ():
        return Tag.__fireDamage


    @staticmethod
    def frostDamage ():
        return Tag.__frostDamage


    @staticmethod
    def hostile ():
        return Tag.__hostile


    @staticmethod
    def peaceful ():
        return Tag.__peaceful


    @staticmethod
    def friendly ():
        return Tag.__friendly


    @staticmethod
    def canSee ():
        return Tag.__canSee


    @staticmethod
    def canFly ():
        return Tag.__canFly



class ArmorClass (object):

    """
    
    """

    __generic, __cloth, __leather, __mail, __plate = range (5)


    @staticmethod
    def validValues ():
        return (ArmorClass.__generic,
                ArmorClass.__cloth,
                ArmorClass.__leather,
                ArmorClass.__mail,
                ArmorClass.__plate)


    @staticmethod
    def generic ():
        return ArmorClass.__generic


    @staticmethod
    def cloth ():
        return ArmorClass.__cloth


    @staticmethod
    def leather ():
        return ArmorClass.__leather


    @staticmethod
    def mail ():
        return ArmorClass.__mail


    @staticmethod
    def plate ():
        return ArmorClass.__plate



class MonsterItemSlot (object):

    """
    
    """

    __head, __neck, __chest, __forearm, __hands, __rightRingFinger, \
    __leftRingFinger, __belt, __legs, __feet = range (10)


    @staticmethod
    def validValues ():
        return (
                MonsterItemSlot.__head,
                MonsterItemSlot.__neck,
                MonsterItemSlot.__chest,
                MonsterItemSlot.__forearm,
                MonsterItemSlot.__hands,
                MonsterItemSlot.__rightRingFinger,
                MonsterItemSlot.__leftRingFinger,
                MonsterItemSlot.__belt,
                MonsterItemSlot.__feet,
                MonsterItemSlot.__legs,
               )


    @staticmethod
    def head ():
        return MonsterItemSlot.__head


    @staticmethod
    def neck ():
        return MonsterItemSlot.__neck,


    @staticmethod
    def chest ():
        return MonsterItemSlot.__chest


    @staticmethod
    def forearm ():
        return MonsterItemSlot.__forearm,


    @staticmethod
    def hands ():
        return MonsterItemSlot.__hands


    @staticmethod
    def rightRingFinger ():
        return MonsterItemSlot.__rightRingFinger,


    @staticmethod
    def leftRingFinger ():
        return MonsterItemSlot.__leftRingFinger,


    @staticmethod
    def belt ():
        return MonsterItemSlot.__belt,


    @staticmethod
    def legs ():
        return MonsterItemSlot.__legs


    @staticmethod
    def feet ():
        return MonsterItemSlot.__feet



class WeaponType (object):

    """
    
    """

    __dagger, __short_sword, __long_sword, __claymore, __axe, __battleAxe,  \
    __bow, __arrow = range (8)


    @staticmethod
    def validValues ():
        return (WeaponType.__dagger,
                WeaponType.__short_sword,
                WeaponType.__long_sword,
                WeaponType.__claymore,
                WeaponType.__axe,
                WeaponType.__battleAxe,
                WeaponType.__bow,
                WeaponType.__arrow)


    @staticmethod
    def dagger ():
        return WeaponType.__dagger


    @staticmethod
    def shortSword ():
        return WeaponType.__short_sword


    @staticmethod
    def longSword ():
        return WeaponType.__long_sword


    @staticmethod
    def claymore ():
        return WeaponType.__claymore


    @staticmethod
    def axe ():
        return WeaponType.__axe


    @staticmethod
    def battleAxe ():
        return WeaponType.__battleAxe


    @staticmethod
    def bow ():
        return WeaponType.__bow


    @staticmethod
    def arrow ():
        return WeaponType.__arrow




class MonsterAttributes (object):

    """
    
    """

    __attrName, __attrTitle, __attrRace, __attrAlignment, __attrHpCurr,         \
    __attrHpMax, __attrPwCurr, __attrPwMax, __attrStr, __attrDex, __attrInt,    \
    __attrArmor, __attrScore, __attrGold = range (14)


    @staticmethod
    def validValues ():
        return (MonsterAttributes.__attrName,
                MonsterAttributes.__attrTitle,
                MonsterAttributes.__attrRace,
                MonsterAttributes.__attrAlignment,
                MonsterAttributes.__attrHpCurr,
                MonsterAttributes.__attrHpMax,
                MonsterAttributes.__attrPwCurr,
                MonsterAttributes.__attrPwMax,
                MonsterAttributes.__attrStr,
                MonsterAttributes.__attrDex,
                MonsterAttributes.__attrInt,
                MonsterAttributes.__attrArmor,
                MonsterAttributes.__attrScore,
                MonsterAttributes.__attrGold)


    @staticmethod
    def name ():
        return MonsterAttributes.__attrName
 

    @staticmethod
    def title ():
        return MonsterAttributes.__attrTitle


    @staticmethod
    def race ():
        return MonsterAttributes.__attrRace


    @staticmethod
    def alignment ():
        return MonsterAttributes.__attrAlignment


    @staticmethod
    def healthCurrent ():
        return MonsterAttributes.__attrHpCurr


    @staticmethod
    def healthMaximum ():
        return MonsterAttributes.__attrHpMax


    @staticmethod
    def powerCurrent ():
        return MonsterAttributes.__attrPwCurr


    @staticmethod
    def powerMaximum ():
        return MonsterAttributes.__attrPwMax


    @staticmethod
    def strength ():
        return MonsterAttributes.__attrStr


    @staticmethod
    def dexterity ():
        return MonsterAttributes.__attrDex


    @staticmethod
    def intelligence ():
        return MonsterAttributes.__attrInt


    @staticmethod
    def armor ():
        return MonsterAttributes.__attrArmor


    @staticmethod
    def score ():
        return MonsterAttributes.__attrScore


    @staticmethod
    def gold ():
        return MonsterAttributes.__attrGold



class MonsterRace (object):

    """
    
    """

    __human, __dwarf = range (2)


    @staticmethod
    def validValues ():
        return (MonsterRace.__human, MonsterRace.__dwarf)


    @staticmethod
    def human ():
        return MonsterRace.__human


    @staticmethod
    def dwarf ():
        return MonsterRace.__dwarf



class GameObjectType (object):

    """
    
    """

    __objTypeOpenspace, __objTypeWall, __objTypeFloor, __objTypeStair,      \
    __objTypeDoor, __objTypeTrap, __objTypeMonster, __objTypeArtifact,      \
    __objTypeArmor, __objTypeWeapon, __objTypeComestible, __objTypeScroll,  \
    __objTypePotion = range (13)


    @staticmethod
    def validValues ():
        return (GameObjectType.__objTypeOpenspace,
                GameObjectType.__objTypeWall,
                GameObjectType.__objTypeFloor,
                GameObjectType.__objTypeStair,
                GameObjectType.__objTypeDoor,
                GameObjectType.__objTypeTrap,
                GameObjectType.__objTypeMonster,
                GameObjectType.__objTypeArtifact,
                GameObjectType.__objTypeArmor,
                GameObjectType.__objTypeWeapon,
                GameObjectType.__objTypeComestible,
                GameObjectType.__objTypeScroll,
                GameObjectType.__objTypePotion)


    @staticmethod
    def openSpace ():
        return GameObjectType.__objTypeOpenspace


    @staticmethod
    def wall ():
        return GameObjectType.__objTypeWall


    @staticmethod
    def floor ():
        return GameObjectType.__objTypeFloor


    @staticmethod
    def stair ():
        return GameObjectType.__objTypeStair


    @staticmethod
    def door ():
        return GameObjectType.__objTypeDoor


    @staticmethod
    def trap ():
        return GameObjectType.__objTypeTrap


    @staticmethod
    def monster ():
        return GameObjectType.__objTypeMonster


    @staticmethod
    def artifact ():
        return GameObjectType.__objTypeArtifact


    @staticmethod
    def armor ():
        return GameObjectType.__objTypeArmor


    @staticmethod
    def weapon ():
        return GameObjectType.__objTypeWeapon


    @staticmethod
    def comestible ():
        return GameObjectType.__objTypeComestible


    @staticmethod
    def scroll ():
        return GameObjectType.__objTypeScroll


    @staticmethod
    def potion ():
        return GameObjectType.__objTypePotion



class PlayerCommand (object):

    """
    
    """

    __moveDownLeft, __moveLeft, __moveUpLeft, __moveUp, __moveUpRight,  \
    __moveRight, __moveDownRight, __moveDown, __exitGame = range (9)


    @staticmethod
    def validValues ():
        return (PlayerCommand.__moveDownLeft,
                PlayerCommand.__moveLeft,
                PlayerCommand.__moveUpLeft,
                PlayerCommand.__moveUp,
                PlayerCommand.__moveUpRight,
                PlayerCommand.__moveRight,
                PlayerCommand.__moveDownRight,
                PlayerCommand.__moveDown,
                PlayerCommand.__exitGame)


    @staticmethod
    def moveDownLeft ():
        return PlayerCommand.__moveDownLeft


    @staticmethod
    def moveLeft ():
        return PlayerCommand.__moveLeft


    @staticmethod
    def moveUpLeft ():
        return PlayerCommand.__moveUpLeft


    @staticmethod
    def moveUp ():
        return PlayerCommand.__moveUp


    @staticmethod
    def moveUpRight ():
        return PlayerCommand.__moveUpRight


    @staticmethod
    def moveRight ():
        return PlayerCommand.__moveRight


    @staticmethod
    def moveDownRight ():
        return PlayerCommand.__moveDownRight


    @staticmethod
    def moveDown ():
        return PlayerCommand.__moveDown


    @staticmethod
    def exitGame ():
        return PlayerCommand.__exitGame

