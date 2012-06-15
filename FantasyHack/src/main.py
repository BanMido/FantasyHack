# -*- coding: utf-8 -*-

import fantasyhack.gamekernel.common as gkCommon
import fantasyhack.gamekernel.utils as gkUtils
import fantasyhack.gamekernel.object_base as gkObjBase
import fantasyhack.gamekernel.object_implementation as gkObjImplementation
import fantasyhack.gamekernel.object_symbols as gkObjSymbols
import fantasyhack.gamekernel.level_base as gkLvlBase
import fantasyhack.gamekernel.world as gkWorld


gkCommon.GameConstants ()
o1 = gkCommon.Beatitude ()
#print o1.validValues ()
o2 = gkCommon.Alignment ()
#print o2.validValues ()
o3 = gkCommon.Tag ()
#print o3.validValues ()
gkCommon.ArmorClass ()
gkCommon.MonsterItemSlot ()
gkCommon.WeaponType ()
gkCommon.MonsterAttributes ()
gkCommon.MonsterRace ()
gkCommon.GameObjectType ()
gkCommon.PlayerCommand ()


gkObjBase.MasterTagCatalogue ()
#gkObjImplementation.Monster (name = "Aragorn", beatitude = None, status = gkObjBase.MonsterStatus (), inventory = set ())
#gkObjImplementation.Monster (name = "Aragorn", beatitude = gkCommon.Beatitude.unknown (), status = None, inventory = set ())
o3 = gkObjImplementation.Monster (name = "Aragorn",
                                  beatitude = gkCommon.Beatitude.unknown (),
                                  status = gkObjBase.MonsterStatus (),
                                  inventory = set ())
#o3.setTag ("hi", True)

o3 = gkObjImplementation.Wall (name = "",
                               beatitude = gkCommon.Beatitude.unknown (),
                               orientation = gkObjImplementation.WallOrientation.horizontal (),
                               isDiggable = True)
#print o3.symbolMapIndex ()

o3 = gkObjImplementation.Floor (name = "",
                                beatitude = gkCommon.Beatitude.unknown (),
                                isDiggable = True,
                                isCorridor = False,
                                pile = list ())
#print o3.symbolMapIndex ()


o4 = gkObjSymbols.SymbolMap ()
print o4.symbol (2)
print o4.symbol (3)
#o4.setSymbolMap ({})


gkUtils.GameTurnCounter ()

class T2 (gkLvlBase.Level):
    def __init__ (self, **kwargs):
        super (T2, self).__init__ (**kwargs)
    def levelBranch (self):
        return gkCommon.GameBranch.primaryBranch ()
    def levelNumber (self):
        return 2
    def isMagicMappable(self):
        return True
    def isTeleportable(self):
        return True
    def getRow(self, rowNumber):
        return None
    def getAllRows(self):
        return None
    def updateRow(self, row):
        pass
#o5.addLevel (T1 ())
gkWorld.addLevel (T2 ())

gkUtils.GameObjectPosition ()

