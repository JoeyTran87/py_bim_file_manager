import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import json
import os, sys
import tkinter as tk

import _cadDataProcesses as CDP
from _cadDataProcesses import *
CDP.sayHello()
#------------------------#
#      INFO TEMPLATE     #
#------------------------#
# jsonTemplatePath = "./BimProjectDir/Template/_column.json"
# # print(jsonTemplatePath," is file? -->",os.path.isfile(jsonTemplatePath))
# columnJsonTemplate = None
# with open(jsonTemplatePath,'r',encoding="mbcs") as rj:
#     columnJsonTemplate = json.loads(rj.read())
# print(columnJsonTemplate)
#------------------------#
#      CAD DATA MODEL    #
#------------------------#
print(prompStart)
askOpen = cadDataPath = ""
askOpen = input("""Do you:
1   Open CAD data model existed
2   Create New CAD data Model
--Your pick: """)

if askOpen == "1":
    #OPEN CAD DATA
    cadData = CadData()

    cadData.start()
    cadData.initTemplates()
    cadData.openModel()
    
if askOpen == "2":   
    cadData = CadData() #initiate BIM Model creation
    cadData.start()
    if cadData.functionNumber == "001":
        cadData.buildingBoundingZone()
    # if cadData.functionNumber == "0011":
    #     cadData.printBuildingBoundingZone()
    if cadData.functionNumber == "2":
        cadData.columnData()
    if cadData.functionNumber == "3":
        cadData.framingData()
    cadData.end()