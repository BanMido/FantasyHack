# -*- coding: utf-8 -*-

'''
Created on Jun 13, 2012

@author: BanMido
'''

import collections
import common
import copy
import level_base
import object_base
import utils


_gameWorld = collections.defaultdict (dict)
_levelsGenerated = collections.defaultdict (set)
_masterObjectInventory = dict ()
_currPlayerPosition = utils.GameObjectPosition ()
_prevPlayerPosition = utils.GameObjectPosition ()
_playerStatus = object_base.MonsterStatus ()
_turnCounter = utils.GameTurnCounter ()
_currPlayerLevel = 1


def getLevel (gameBranch, levelNumber):
    if gameBranch not in common.GameBranch.validValues ():
        errStr = "Expected a value from the following set (%s)" % (",".join ([repr (x) for x in common.GameBranch.validValues ()]))
        raise ValueError (errStr)

    return _gameWorld [gameBranch][int (levelNumber)]


def addLevel (level):
    if isinstance (level, level_base.Level) == False:
        errStr = "Expecting an instance of 'Level', got an instance of %s" % repr (type (level))
        raise TypeError (errStr)

    levelObj = copy.deepcopy (level)
    lvlBranch = levelObj.levelBranch ()

    if lvlBranch not in common.GameBranch.validValues ():
        errStr = "Expected a value from the following set (%s)" % (",".join ([repr (x) for x in common.GameBranch.validValues ()]))
        raise ValueError (errStr)
 
    if lvlBranch in _gameWorld and levelObj.levelNumber () in _gameWorld[lvlBranch]:
        errStr = "Attempt to add duplicate entry, branch %s and level number '%s' into GameWorld" % (lvlBranch, levelObj.getLevelNumber ())
        raise RuntimeError (errStr)

    _gameWorld [lvlBranch][levelObj.levelNumber ()] = levelObj
    _levelsGenerated[lvlBranch].add (levelObj.levelNumber ())


def lookupMasterObjectInventory (uid):
    return _masterObjectInventory[uid]
 
def updateMasterObjectInventory (gameObject):
    if isinstance (gameObject, object_base.GameObject) == False:
        errStr = ""
        raise TypeError (errStr)

    _masterObjectInventory[gameObject.uid ()] = gameObject


def currPlayerPosition ():
    return _currPlayerPosition


def prevPlayerPosition ():
    return _prevPlayerPosition


def playerStatus ():
    return _playerStatus

