import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import json
import os, sys

import _cadDataProcesses as CDP
from _cadDataProcesses import *
CDP.sayHello()

#initial Declaration
dirTxt=dataType=colIndex=targetColIndices=declareRegion=declareLevel=translateCs=category=project=disciptline=askAuto = askCombine=""
combData = []
pathTxts = []


# input director
dirTxt = input("""START-----------START----------START------------START----------START
Step (1) Directory of text Files: """)
if os.path.isdir(dirTxt): # verify Director existed
    for f in os.listdir(dirTxt):
        try:
            if ".txt" in f:#validate TXT file type
                if len(f.split("_")) >= 6:# validate BIM File name code
                    pathTxts.append(f)
        except:
            pass
# print (pathTxts)
combineJsonPath = dirTxt + "\\Combine"+".json"
# print (combineJsonPath)
#verify if need Auto and combine
askAuto = input("Do you want Auto Generate (y/n):")
askCombine = input("Do you want create more Combine Json File (y/n):")

if askAuto.lower() == "n":
    dataType = input("""---------------------
    Step (2) Data Type 
    (with no Input, DEFAULT will be applied)
    Ex: Text, Multitext, Line, Polyline
    , Hatch, Block, Solid, Leader
    , Circle, Rectangle, Elipse
    ------Type here: """)

    colIndex = input("""----------------------
    (3) Column Index of Data Type (must be Integer)
    (with no Input, DEFAULT will be applied)
    ------Type here: """)

    targetColIndices = input("""---------------------
    (4) Properties of Targeted Data 
    (with no Input, DEFAULT will be applied)
    (Must be list of Name)
    Ex: Layer,Position X,Position Y,Position Z,Rotation,Value: 
    ------Type here: """)

    declareRegion= input("""----------------------
    (5) BUILDInG REGION Abbreviation of Data:
    (with no Input, DEFAULT will be applied)
    Ex:
    BA (Basement), 
    PD (Podium),
    LS (Landscape),
    A (Tower A),
    B (Tower B)
    ------Type here: """)

    declareLevel = input("""----------------------
    (6) Building LEVEL Abbreviation of Data:
    (with no Input, DEFAULT will be applied)
    Ex: 02B, 01B, GF, 01F 01FM
    ------Type here: """)

    translateCs = input("""----------------------
    (7) Data Coordianate Translate X & Y & Z & Rotation at New Coordinate:
    (with no Input, DEFAULT will be applied)
    (Should be distance measured to translate CAD Data Coordiate to BIM model Coordinate
    and rotation angle at BIM Model Coordinate
    Unit is Milimeter and Degree, seperator is 1 space)
    Ex: 375 65553 0 0
    ------Type here: """)

    category = input("""----------------------
    (8) Information Code 
    (with no Input, DEFAULT will be applied)
    Ex: 
    CL (column)
    BM (Beam)
    FD (Foundation)
    ------Type here: """)

if askAuto.lower() == "y":
    for path in pathTxts:
        try:
            ext = ".txt"
            nameWithNotExt = path.split(ext)[0]
            fileDir = dirTxt +"\\" 
            nameCodes = nameWithNotExt.split("_")
            pathTxt = fileDir + path
            #AUTO PROCESS DATA
            dataType = "Text"
            colIndex = "1"
            targetColIndices = "Layer,Position X,Position Y,Position Z,Rotation,Value"
            project = nameCodes[0]
            disciptline = nameCodes[1]
            declareRegion = nameCodes[2]
            declareLevel = nameCodes[3]
            category = nameCodes[4]
            translateCs = nameCodes[5] 
            jsonPath = fileDir + nameWithNotExt+"-"+dataType+".json"
            data = txtToDic(pathTxt,dataType,colIndex,targetColIndices,declareRegion,declareLevel,translateCs,category,project,disciptline)
            writeJson = writeTxtToJson(jsonPath,data)
            print(pathTxt)
            if askCombine.lower() == "y":
                # print(combineJsonPath)
                try:
                    combData += data            
                    combineJson = writeTxtToJson(combineJsonPath,combData)
                except:
                    pass
        except:
            pass


print("SUCCEEDED TRANSFER JSON FILE at:\n",dirTxt)
print("""END----------END------------END------------END----------END""")
