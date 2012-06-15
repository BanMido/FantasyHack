# -*- coding: utf-8 -*-

'''
Created on Jun 13, 2012

@author: BanMido 
'''

_uid_module_variables = {"uid" : 500}

def generateUid ():
    _uid_module_variables["uid"] = _uid_module_variables["uid"] + 1
    return _uid_module_variables["uid"]

