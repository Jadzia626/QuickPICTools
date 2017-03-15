#
#  QuickPICTools
#  + DataWrapper Module
#    + DataWrapper Class
#

import logging as logger

from os import path, listdir

class DataWrapper():

    def __init__(self):

        self.dataPath  = ""
        self.dataSets  = {}
        self.dataFiles = []

        emptyDict = {"All":None,"XY":None,"XZ":None,"YZ":None}

        self.dataSets["BField"]  = emptyDict
        self.dataSets["EField"]  = emptyDict
        self.dataSets["Current"] = emptyDict
        self.dataSets["PSI"]     = emptyDict
        self.dataSets["Beam"]    = emptyDict
        self.dataSets["Plasma"]  = emptyDict

        return

    ##
    #  Setters
    ##

    def setPath(self, dataPath):
        if path.isdir(dataPath):
            self.dataPath = dataPath
        else:
            logger.error("Path not found %s" % dataPath)
        return

    ##
    #  Actions
    ##

    def loadDataSets(self):
        logger.info("Loading from %s" % self.dataPath)

        dicType = {
            "FBX" : ["BField","FB","X"],
            "FBY" : ["BField","FB","Y"],
            "FBZ" : ["BField","FB","Z"],
            "FEX" : ["EField","FE","X"],
            "FEY" : ["EField","FE","Y"],
            "FEZ" : ["EField","FE","Z"],
            "JPX" : ["Current","JP","X"],
            "JPY" : ["Current","JP","Y"],
            "JPZ" : ["Current","JP","Z"],
            "PSI" : ["PSI","PSI","S"],
            "QEB" : ["Beam","Q","S"],
            "QEP" : ["Plasma","Q","S"],
        }

        dirContent = listdir(self.dataPath)
        for listItem in dirContent:
            itemPath = path.join(self.dataPath,listItem)
            if path.isdir(itemPath):
                listBits = listItem.split("-")
                logger.info("Dataset %s %d" % (listItem,len(listBits)))
                dataName = listBits[0]
                dataNum  = ""
                if dataName[:3] == "QEP":
                    dataNum  = dataName[3:]
                    dataName = "QEP"


                if listBits[0] == "FBX":
                    if len(listBits) == 1:
                        self.dataSets["BField"]["All"] = DataSet(
                            "FBX",itemPath,"FB","X","All"
                        )
                    else:
                        self.dataSets["BField"][listBits[0]] = DataSet(
                            "FBX",itemPath,"FB","X",listBits[0]
                        )



            else:
                self.dataFiles.append(listItem)

        return

# End Class DataWrapper


class DataSet():

    def __init__(self, dataName, dataPath, dataType, dataAxis, dataSlice):

        self.dataName  = dataName
        self.dataPath  = dataPath
        self.dataType  = dataType
        self.dataAxis  = dataAxis
        self.dataSlice = dataSlice
        self.dataCount = 0
        self.dataTimes = []

        return

# End Class DataSet
