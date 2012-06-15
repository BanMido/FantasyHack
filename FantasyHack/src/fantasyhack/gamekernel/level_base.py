# -*- coding: utf-8 -*-

'''
Created on Jun 13, 2012

@author: BanMido 
'''

import abc


class Level (object):

    """
    
    """

    __metaclass__ = abc.ABCMeta
 

    def __init__ (self, **kwargs):
        super (Level, self).__init__ (**kwargs)


    @abc.abstractmethod
    def levelBranch (self): 
        raise NotImplementedError ("Provide an implementation")


    @abc.abstractmethod
    def levelNumber (self):
        raise NotImplementedError ("Provide an implementation")


    @abc.abstractmethod
    def isMagicMappable (self):
        raise NotImplementedError ("Provide an implementation")


    @abc.abstractmethod
    def isTeleportable (self):
        raise NotImplementedError ("Provide an implementation")


    @abc.abstractmethod
    def getRow (self, rowNumber):
        raise NotImplementedError ("Provide an implementation")


    @abc.abstractmethod
    def getAllRows (self):
        raise NotImplementedError ("Provide an implementation")


    @abc.abstractmethod
    def updateRow (self, row):
        raise NotImplementedError ("Provide an implementation")

