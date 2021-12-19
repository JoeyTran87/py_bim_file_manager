from typing import overload
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import json
import os, sys
import tkinter as tk

import _plotVisual
from _plotVisual import *

def sayHello():
    print("Module:","_cadDataProcesses.py---IMPORTED")

def txtToDic(pathTxt,dataType,colIndex,targetProperties,region,level,translateCs,category,project,disciptline):
    iniCount = 0
    resCount = 0
    res = []
    targetCol = []
    with open(pathTxt, "r",encoding="mbcs") as f:
        keys = f.readline().split('\t')
        targets = targetProperties.split(",")
        for ii in range(len(keys)):
            for prop in targets:
                if prop ==  keys[ii]:
                    targetCol.append(ii)            
        lenKey = len(keys)
        for line in f.readlines()[1:]:
            dic = {}
            iniCount +=1
            try:
                dic["ProjectNumber"] = project
                dic["Discipline"] = disciptline
                dic["TranslateCoordinateSystem"] = translateCs
                dic["BuildingRegion"] = region
                dic["BuildingLevel"] = level
                dic["DataType"] = dataType
                dic["Category"] = category
                atts = line.split('\t')      
                lenAtt = len(atts)
                if lenKey == lenAtt and atts[int(colIndex)] == dataType:
                    for cii in targetCol:
                        dic[keys[cii]] = atts[cii]
                    res.append(dic)
                    resCount +=1
            except :
                pass
    return res

def writeTxtToJson(path,data):
	with open(path,'w',encoding="mbcs") as f:				
		f.write(json.dumps(data,indent=4))
	return "Succeeded"

#------------------------#
#                        #
#      FORM INPUT        #
#                        #
#------------------------#
class AppInput(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.inputText = tk.Entry()
        self.inputText.pack()        
        self.contents = tk.StringVar()# Create the application variable.        
        self.contents.set("<Input Here>")# Set it to some value.        
        self.inputText["textvariable"] = self.contents# Tell the entry widget to watch this variable. 
        # self.inputText.bind('<Key-Return>',self.print_contents)# Define a callback for when the user hits return.# It prints the current value of the variable.
        self.quit = tk.Button(self, text="QUIT", fg="red",command=self.master.destroy)
        self.quit.pack(side="bottom")
    def print_contents(self, event):
        promp = """---Your Input is:
        """
        print("",
              self.contents.get())

# root = tk.Tk()
# myapp = App(root)
# myapp.mainloop()
#========================#
#                        #
#      BIM DATA MODEL    #
#                        #
#========================#
class BimModel:
    dirPath=dataType=colIndex=targetColIndices=declareRegion=declareLevel=translateCs=category=project=disciptline=askAuto=askCombine=""
    p_briefInfo = [] #PROJECT INFOMATION
    b_Info = [] #BUILDING INFORMATION
    def __init__(self,dataPoints):
        self.DataPoint = dataPoints
        pass
    def start(self):
        print(promp1)
        pass
    def end(self):
        print(prompEnd)
        pass
    def askDirPath(self):
        _dirPath = input("""Step (1) Directory of **BIM** Model
        --Your path: """)
        if os.path.isdir(_dirPath):
            self.dirPath = _dirPath
            return
    def columnData(self,template):
        print("---Please input by Popup **Form Window**")
        root = tk.Tk()
        myapp = AppInput(root)
        myapp.mainloop()
        names = myapp.contents.get()
        
        for n in names:
            col = template
            col["ColumnName"] = n
            self.columns.append(col)

        print("---There are {0} element created".format(len(self.columns)))
        askRegister = input ("Do you want to create these data? (y/n):")
#========================#
#                        #
#      CAD DATA MODEL    #
#                        #
#========================#
prompStart = """
#------------------------#
#         START          #
#------------------------#
"""
prompEnd = """
#------------------------#
#          END           #
#------------------------#
"""
prompAction = """Please choose your action:
*-------------------------------------*
| 0    Build BUILDING DATUM            |
| 001  Build BUILDING BOUNDING ZONE    |
| 0011 Plot BUILDING BOUNDING ZONE     |
| 1    Build FOUNDATIONs data          |
| 2    Build COLUMNS data              |
| 3    Build FRAMING data              |
| U2   Update COLUMNS data             |
*-------------------------------------*
---Your action: """
prompActionFraming = """---Choose your acction:
*-------------------------------------*
| 300  FRAMING NAMING / DECLARATION   
| 301  FRAMING LOCATION                           
*-------------------------------------*
"""
prompFilter = """---Filterer START WITH:"""
prompSave = """Do you want to **model these data? (y/n):"""
#CLASS OF CAD DATA - MODELED FOR BIM DATA MODEL
class CadData:
    #--------------------------#
    # MODEL ATTRIBUTES         #
    #--------------------------#
    dirPath=dataType=colIndex=targetColIndices=declareRegion=declareLevel=translateCs=category=project=disciptline=askAuto=askCombine=""
    dataFilePaths = dataFileNames = templateFiles=[] # FILE DIRECTORY AND PATHS
    building = {} #BUILDING INFORMATION
    foundations = columns = framings = walls=floors=[] # BUILDING ELEMENT GROUPS
    buildingTemplate = foundationTemplate = columnTemplate = framingTemplate = {} #template Dictionary
    bbZMin = bbZMax = None # BUILDING BOUNDING ZONE MIN MAX
    subDirWip = "1_WIP"
    subDirShare = "2_SHARE"
    subDirPublic = "3_PUBLISH"
    subDirArchive = "4_ARCHIVE"
    #--------------------#
    # INITIATION         #
    #--------------------#
    def __init__(self):
        self.askDirPath()
        self.initTemplates() 
    #---------------#
    # START         #
    #---------------#
    def start(self):
        self.askFunction()
        print("Root Directory: ",self.dirPath)
    def end(self):
        print(prompEnd)
    #---------------#
    # ASK ACTION    #
    #---------------#
    def askFunction(self):
        self.functionNumber = input(prompAction)
    #-----------------------#
    # ASK DIRECTORY PATH    #
    #-----------------------#
    def askDirPath(self):
        _dirPath = input("""Step (1) Directory of **CAD** Data Model
---Your path: """)
        if os.path.isdir(_dirPath):
            self.dirPath = _dirPath
            return
    #-----------------------#
    # MODELING COLUMNS DATA #
    #-----------------------#
    def columnData(self):
        print("---Please INPUT to Popup **Form Window**")
        root = tk.Tk()
        myapp = AppInput(root)
        myapp.mainloop()
        names = myapp.contents.get().split("\n") # GER DATA FROM FORM INPUTS , DATA FROM MULTI ROWS FROM EXCEL FILE
        print (names)
        for n in names:
            col = {}
            try:
                if not n == "\n" and not " " in n and not "\t" in n:
                    col = self.columnTemplate.copy()
                    col["ColumnName"] = n
                    self.columns.append(col)
                    col = {}
            except:
                pass

        print("---There are {0} element created".format(len(self.columns)))
        askModel = input ("Do you want to **model these data? (y/n):")
        if askModel.lower() == "y":
            jsonPath = self.dirPath + "\\" + self.subDirWip + "\\column.json"
            print(jsonPath)
            self.createJson(jsonPath,self.columns)
    #------------------------#
    # MODELING FRAMINGS DATA #
    #------------------------#  
    def framingData(self):        
        jsonPath = self.dirPath + "\\" + self.subDirWip + "\\framing.json"
        if True:#not os.path.isfile(jsonPath):
            askActionFraming = input(prompActionFraming)
            if askActionFraming == "301":
                print("---Please INPUT to Popup **Form Window**")
                root = tk.Tk()
                myapp = AppInput(root)
                myapp.mainloop()
                names = myapp.contents.get().split("\n") # GER DATA FROM FORM INPUTS , DATA FROM MULTI ROWS FROM EXCEL FILE
                print (names)
                for n in names:
                    frame = {}
                    try:
                        if not n == "\n" and not " " in n and not "\t" in n:
                            frame = self.framingTemplate.copy()
                            frame["FramingName"] = n
                            self.framings.append(frame)
                            frame = {}
                    except:
                        pass
                print("---There are {0} element created".format(len(self.framings)))
                askModel = input (prompSave)
                if askModel.lower() == "y":
                    print(jsonPath)
                    self.createJson(jsonPath,self.framings)
            if askActionFraming == "300":
                print("---Please INPUT to Popup **Form Window**")            
                root = tk.Tk()
                myapp = AppInput(root)
                myapp.mainloop()
                names = myapp.contents.get().split("\n") # GER DATA FROM FORM INPUTS , DATA FROM MULTI ROWS FROM EXCEL FILE
                print (names)
                filterer = input(prompFilter)

                for n in names:
                    frame = {}
                    try:
                        flagFilter = filterer in n[:len(filterer)]
                        if not n == "\n" and not " " in n and not "\t" in n and flagFilter:
                            frame = self.framingTemplate.copy()
                            frame["FramingName"] = n
                            self.framings.append(frame)
                            frame = {}
                    except:
                        pass

                print("---There are {0} element created".format(len(self.framings)))
                askModel = input (prompSave)
                if askModel.lower() == "y":
                    print(jsonPath)
                    self.createJson(jsonPath,self.framings)
        else:
            pass
    #------------------------#
    # BUILDING BOUNDING ZONE   #
    #------------------------#
    def buildingBoundingZone(self):
        jsonPath = self.dirPath + "\\" + self.subDirWip + "\\building.json"
        if not os.path.isfile(jsonPath):
            self.bbZMin = input("------X Y Boundingbox MIN point:")#.split(" ") # -18000 -74000
            self.bbZMax= input("------X Y Boundingbox MAX point:")#.split(" ") # 116000 105000
            # self.plotScale = float(input("Plot Scale (1/x):"))
            # print("Bounding Zone Min:", self.bbZMin)
            # print("Bounding Zone Max:", self.bbZMax)
            self.building = self.buildingTemplate.copy()
            # print("BUILDING INFORMATION: ",self.building)
            self.building["BuildingBoundingZone"] = BBRectange(self.bbZMin.split(" "),self.bbZMax.split(" "))
            print("---Succeeded create BUILDING BOUNDING ZONE data")
            askModel = input ("---Do you want to **model these data? (y/n):")
            if askModel.lower() == "y":                
                print(jsonPath)
                self.createJson(jsonPath,self.building)
                self.printBuildingBoundingZone()
        else:
            
            askChange = input ("Do you want to CHANGE existed BUILDING BOUNDING ZONE information? (y/n):")
            if askChange.lower() == "y":
                with open(jsonPath,"r",encoding="mbcs") as bd:
                    self.building = json.loads(bd.read())
                # print("BUILDING INFORMATION: ",self.building)
                self.bbZMin = input("------X Y Boundingbox MIN point:")#.split(" ") # -18000 -74000
                self.bbZMax= input("------X Y Boundingbox MAX point:")#.split(" ") # 116000 105000
                # print("Bounding Zone Min:", self.bbZMin)
                # print("Bounding Zone Max:", self.bbZMax)
                self.building["BuildingBoundingZone"] = BBRectange(self.bbZMin.split(" "),self.bbZMax.split(" "))
                print("---Succeeded create BUILDING BOUNDING ZONE data")
                askModel = input ("---Do you want to **model these data? (y/n):")
                if askModel.lower() == "y":
                    print(jsonPath)
                    self.createJson(jsonPath,self.building)
                    self.printBuildingBoundingZone()

    def printBuildingBoundingZone(self):
        jsonPath = self.dirPath + "\\" + self.subDirWip + "\\building.json"
        if os.path.isfile(jsonPath):
            self.plotScale = float(input("Plot Scale (1/x):"))
            plotRectange(self.bbZMin,self.bbZMax,self.plotScale)
        
        
    #------------------------#
    # CREATE JSON            #
    #------------------------# 
    def createJson(self,_path,_data):
        with open(_path,'w',encoding="mbcs") as f:				
            f.write(json.dumps(_data,indent=4))
        return "Succeeded"

    #------------------------#
    # OPEN DATA MODEL CREATED#
    #------------------------# 
    def openModel(self):
        self.traceData ()        
        for file in self.dataFilePaths:
            fileName = file.split("\\")[-1].lower()
            if "foundation" in fileName and ".json" in fileName:
                print("------",file)
                with open(file,'r',encoding="mbcs") as rjd0:
                    self.foundations = json.loads(rjd0.read())
                    print("---------Element Count: ",len(self.foundations))
            if "column" in fileName and ".json" in fileName:
                print("------",file)
                with open(file,'r',encoding="mbcs") as rjd1:
                    self.columns = json.loads(rjd1.read())
                    print("---------Element Count: ",len(self.columns))
            if "framing" in fileName and ".json" in fileName:
                print("------",file)
                with open(file,'r',encoding="mbcs") as rjd2:
                    self.framings = json.loads(rjd2.read())
                    print("---------Element Count: ",len(self.framings))
    
    #------------------------#
    # FIND ALL DATA FILES    #
    #------------------------# 
    def traceData(self):
        for f in os.listdir(self.dirPath+"\\"+self.subDirWip):
            try:
                self.dataFilePaths.append(self.dirPath+"\\"+self.subDirWip+"\\"+f)
                # if ".json" in f:
                #     self.dataFileNames.append(f)                    
            except:
                pass
    
    #--------------------------------#
    # INPUT INFORMATION TEMPLATE     #
    #--------------------------------# 
    def initTemplates(self):
        if self.dirPath:
            jsonTemplatePath = self.dirPath + r"\Template"
            for f in os.listdir(jsonTemplatePath):
                fp = jsonTemplatePath + "\\" + f
                print(fp)
                if "building" in f and ".json" in f:
                    self.templateFiles.append(fp)
                    with open(fp,'r',encoding="mbcs") as bt:
                        self.buildingTemplate = json.loads(bt.read())
                if "foundation" in f and ".json" in f:
                    self.templateFiles.append(fp)
                    with open(fp,'r',encoding="mbcs") as rtj0:
                        self.foundationTemplate = json.loads(rtj0.read())
                if "column" in f and ".json" in f:
                    self.templateFiles.append(fp)
                    with open(fp,'r',encoding="mbcs") as rtj1:
                        self.columnTemplate = json.loads(rtj1.read())
                if "framing" in f and ".json" in f:
                    self.templateFiles.append(fp)
                    with open(fp,'r',encoding="mbcs") as rtj2:
                        self.framingTemplate = json.loads(rtj2.read())
        print("---All template loaded")