import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import json
import os, sys

import _cadDataProcesses as CDP
from _cadDataProcesses import *
CDP.sayHello()

#------------------------#
#                        #
#      BIM DATA MODEL    #
#                        #
#------------------------#
askOpen = bimDirPath = ""
askOpen = input("""Do you:
1   Open BIM model existed
2   Create New BIM Model
--Your pick: """)

if askOpen == "1":
    bimDirPath = input("Path here:") #open BIM model existed
    #OPEN CAD DATA
    bimModel = BimModel()
    bimModel.openData()
    
if askOpen == "2":   
    bimModel = BimModel() #initiate BIM Model creation
    bimModel.start()
    bimModel.end()