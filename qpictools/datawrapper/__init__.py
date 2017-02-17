#
#  QuickPICTools
#  + DataWrapper Module
#    + Init File
#

import logging as logger

from os           import path
from qpictools    import *
from .datawrapper import *

def loadQPicData(dataPath):

    if not path.isdir(dataPath):
        logger.error("Path not found %s" % dataPath)
        return None

    qpData = DataWrapper()
    qpData.setPath(dataPath)
    qpData.loadDataSets()

    return qpData
