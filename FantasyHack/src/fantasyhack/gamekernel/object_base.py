# -*- coding: utf-8 -*-

'''
Created on Jun 13, 2012

@author: BanMido 
'''

import abc
import common
import copy
import uid


class MasterTagCatalogue (object):

    """
    
    """

    @staticmethod
    def genericTags ():
        return dict (
                        {
                        common.Tag.visible () : False,
                        common.Tag.consumable () : False,
                        common.Tag.container () : False,
                        common.Tag.destructible () : False,
                        common.Tag.immovable () : False,
                        common.Tag.equipable () : False,
                        common.Tag.monster () : False,
                        }
                    )


    @staticmethod
    def armorTags ():
        return dict (
                        {
                        common.Tag.corrodable () : False,
                        common.Tag.durable () : False,
                        }
                    )


    @staticmethod
    def weaponTags ():
        return dict (
                        {
                        common.Tag.oneHanded () : False,
                        common.Tag.twoHanded () : False,
                        common.Tag.balanced () : False,
                        common.Tag.holyDamage () : False,
                        common.Tag.fireDamage () : False,
                        common.Tag.frostDamage () : False,
                        }
                    )


    @staticmethod
    def monsterTags ():
        return dict (
                        {
                        common.Tag.hostile () : False,
                        common.Tag.peaceful () : False,
                        common.Tag.friendly () : False,
                        common.Tag.canSee () : False,
                        common.Tag.canFly () : False,
                        }
                    )



class MonsterStatus (object):
    def __init__ (self):
        self.__monsterStatus = \
            dict ({
                    common.MonsterAttributes.name ()               : "",
                    common.MonsterAttributes.title ()              : "",
                    common.MonsterAttributes.race ()               : None,
                    common.MonsterAttributes.alignment ()          : None,
                    common.MonsterAttributes.healthCurrent ()      : 0,
                    common.MonsterAttributes.healthMaximum ()      : 0,
                    common.MonsterAttributes.powerCurrent ()       : 0,
                    common.MonsterAttributes.powerMaximum ()       : 0,
                    common.MonsterAttributes.strength ()           : 0,
                    common.MonsterAttributes.dexterity ()          : 0,
                    common.MonsterAttributes.intelligence ()       : 0,
                    common.MonsterAttributes.armor ()              : 10,
                    common.MonsterAttributes.score ()              : 0,
                    common.MonsterAttributes.gold ()               : 0,
                 })


    def getMonsterStatus (self, attributes):
        if len (attributes) == 0:
            return copy.deepcopy (self.__monsterStatus)

        validAttributes = [attribute for attribute in attributes if attribute in common.MonsterAttributes.validValues ()]
        monStatus = [[attribute, self.__monsterStatus[attribute]] for attribute in validAttributes]

        return dict (monStatus)



class GameObject (object):

    """
    
    """

    __metaclass__ = abc.ABCMeta
 
 
    def __init__ (self, name, beatitude, **kwargs):
        super (GameObject, self).__init__ (**kwargs)
        self.__name = str (name)

        if beatitude in common.Beatitude.validValues ():
            self.__beatitude = beatitude
        else:
            errStr = "Expected a value from the following set (%s)" % (",".join ([repr (x) for x in common.Beatitude.validValues ()]))
            raise ValueError (errStr)

        self.__uid = uid.generateUid ()
        self.__tags = MasterTagCatalogue.genericTags ()


    @abc.abstractmethod
    def objectType (self):
        raise NotImplementedError ("Provide an implementation")


    @abc.abstractmethod
    def symbolMapIndex (self):
        raise NotImplementedError ("Provide an implementation")


    def uid (self):
        return self.__uid


    def name (self):
        return self.__name


    def beatitude (self):
        return self.__beatitude


    def tags (self):
        return self.__tags


    def setName (self, name):
        self.__name = str (name)


    def setBeatitude (self, beatitude):
        if beatitude in common.Beatitude.validValues ():
            self.__beatitude = beatitude
        else:
            errStr = "Expected a value from the following set (%s)" % (",".join ([repr (x) for x in common.Beatitude.validValues ()]))
            raise ValueError (errStr)


    def updateTags (self, tags):
        self.__tags = tags


    def setTag (self, tag, value):
        if tag in common.Tag.validValues ():
            self.__tags[tag] = bool (value)
        else:
            errStr = "Expected a value from the following set (%s)" % (",".join ([repr (x) for x in common.Tag.validValues ()]))
            raise ValueError (errStr)

