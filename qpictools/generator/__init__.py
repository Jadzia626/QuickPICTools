#
#  QuickPICTools
#  + Generator Module
#    + Init File
#

import logging as logger

from os         import path, mkdir, listdir
from shutil     import copyfile
from qpictools  import *

def generateInputs(inDir, outDir, repMask, repData, nameMask, nameData, jobFile, execFile=""):
    """generateInputs
    inDir    : Directory to scan. The function will open all subdirectories, and read the rpinput
               file, do a replace of the value in repMask with the value in repData. The file
               will then be put in a folder based on nameMask and nameData. If a jobFile is
               specified, a replace of the new name will replace any instance of %NAME%
    outDir   : Directory to output files.
    repMask  : Array of masks in the input file to be replaced with a value.
    repData  : A vector of size(repMask) string vectors of N replace values to repla the repMask
               with.
    nameMask : The job name structure where % will be replaced by the nameData entry.
    nameData : A N length (column number of repData) of names for the individual datasets.
    jobFile  : Opional name of jobfile where the name of the job will be replaced.
    """

    print("")
    if not path.isdir(inDir):
        logger.error("Input folder does not exist.")
        return False
    if not path.isdir(outDir):
        logger.error("Output folder does not exist.")
        return False

    nRep  = len(repMask)
    nData = len(nameData)
    if not len(repData) == nData:
        logger.error("Input mismatch between repData and nameData")
        return False
    for repRow in repData:
        if not len(repRow) == nRep:
            logger.error("Input mismatch between repData and repMask")
            return False

    dirContent = listdir(inDir)
    for subDir in dirContent:

        if subDir == "." or subDir == "..":
            continue

        inPath = path.join(inDir,subDir)
        if not path.isdir(inPath):
            logger.debug("Skipping element '%s'. Not a directory" % subDir)
            continue

        inFile = path.join(inDir,subDir,"rpinput")
        if not path.isfile(inFile):
            logger.debug("Skipping element '%s'. Does not contain a QuickPIC input file" % subDir)
            continue

        print("Processing file: %s" % inFile)

        fileObj = open(inFile,encoding="utf-8",mode="r")
        inData  = fileObj.read()
        fileObj.close()

        jobInFile  = path.join(inPath,jobFile)
        execInFile = path.join(inPath,execFile)
        if path.isfile(jobInFile):
            fileObj   = open(jobInFile,encoding="utf-8",mode="r")
            jobInData = fileObj.read()
            fileObj.close()

        for rowIdx in range(nData):
            outData = inData
            outName = nameMask.replace("%",nameData[rowIdx])
            print("Processing output %s" % outName, end="")

            outPath = path.join(outDir,outName)
            if not path.isdir(outPath):
                mkdir(outPath)

            for colIdx in range(nRep):
                outData = outData.replace(repMask[colIdx],repData[rowIdx][colIdx])

            outFile = path.join(outPath,"rpinput")
            fileObj = open(outFile,encoding="utf-8",mode="w")
            fileObj.write(outData)
            fileObj.close()

            if path.isfile(jobInFile):
                jobOutFile = path.join(outPath,jobFile)
                fileObj    = open(jobOutFile,encoding="utf-8",mode="w")
                fileObj.write(jobInData.replace("%NAME%",outName))
                fileObj.close()

            if path.isfile(execInFile):
                execOutFile = path.join(outPath,execFile)
                copyfile(execInFile,execOutFile)

            print(" – Done")

    print("")
    return True
