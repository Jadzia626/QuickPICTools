#!/usr/bin/env python3
# -*- coding: utf-8 -*

from qpictools import generator as gen

inDir    = "/scratch/Temp/JobFiles/Input"
outDir   = "/scratch/Temp/JobFiles/Output"
repMask  = ["%EMIT%","%SIGR%"]
repData  = [
    ["  0.1   ","  1.1729"],
    ["  0.2   ","  1.6587"],
    ["  0.5   ","  2.6227"],
    ["  1.0   ","  3.7091"],
    ["  2.0   ","  5.2454"],
    ["  5.0   ","  8.2937"],
    [" 10.0   "," 11.7291"],
    [" 20.0   "," 16.5875"],
    [" 50.0   "," 26.2271"],
    ["100.0   "," 37.0907"],
]
nameMask = "PPE-Q02%"
nameData = ["A","B","C","D","E","F","G","H","I","J"]
jobFile  = "JobScript.sh"

gen.generateInputs(inDir, outDir, repMask, repData, nameMask, nameData, jobFile)
