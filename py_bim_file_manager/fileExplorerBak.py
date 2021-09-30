
import os, shutil, json
import pandas as pd




#------------------------------------------------------#
# INPUT
#------------------------------------------------------#
dirPath = input("---Nhập đường dẫn:")#r"R:\BimESC\01_PROJECTS\MARUBENI SOLUBE\01 INCOME\210609- BẢN VẼ BỂ NƯỚC VÀ BỂ XLNT"
#------------------------------------------------------#
# THIẾT LẬP ĐIỀU KIỆN
#------------------------------------------------------#
noti1 =f"""---Folder == {dirPath} ==Có tồn tại"""
exts =['dwg','rvt','pdf','jpg','png','bmp']
needExts = " ".join(exts).lower()

if os.path.isdir(dirPath):
    print(noti1)
    print(f"---Tiến hành duyệt các file có đuôi: ",needExts)
filePaths = []
fileExtUnsort = [] # DANH SACH ĐƯỜNG DẪN FULL TÊN FILE VÀ DS TÊN FILE KHÔNG CÓ DIRECTORY
dicExt = {}
#------------------------------------------------------#
# DUYỆT FILE
#------------------------------------------------------#
for (path,dr,file) in os.walk(dirPath):    
    for f in file:
        try:
            ext = f.split(".")[-1].lower()
            dicExt[ext.lower()] = ""
            fp = path+"\\"+f
            filePaths.append(fp)                      
        except:
            pass

fileExts = [d for d in dicExt]
stringFileExt = " ".join(fileExts)

print(f"---Tổng số tập tin = {len(filePaths)}")
print(f"---Có Phần mở rộng: {fileExts}")

#------------------------------------------------------#
# TẠO DICTIONARY
#------------------------------------------------------#
listDic = []
listDicUnsort = [] #DANH SÁCH DICTIONARY
listExtUnsort = []
dicExtUnsort ={}
dic = {"Full Path": None,
        "File Name": None,
        "Pure File Name": None,
        "File Extension": None,
        "Parent Name": None}
excepts = [] # DANH SÁCH LỖI
for p in filePaths:
    try:        
        dicF = dic.copy()
        spliter = p.split("\\")
        fn = spliter[-1] #FILE NAME
        et = fn.split(".")[-1]# EXENTIONS
        pfn = fn.replace("."+et,"")  # PURE FILE NAME
        pr = spliter[-1]#PARENT
        prp = '\\'.join(spliter[:-1])
        
        dicF["Full Path"] = p
        dicF["File Name"] = fn
        dicF["Pure File Name"] = pfn
        dicF["File Extension"] = et
        dicF["Parent Name"] = pr
        dicF["Parent Path"] = prp
        
        if et.lower() in needExts:
            dicF["isSorted"] = 'True'
            listDic.append(dicF)
        else:
            dicF["isSorted"] = 'False'  
            dicExtUnsort[et.lower()] = ""
            listDicUnsort.append(dicF)

    except Exception as ex:
        excepts.append(f"====Đã có lỗi: {ex}: {p}")
        pass
listExtUnsort = [d for d in dicExtUnsort]
print (f"---Tổng số tập tin Khớp Extension = {len(listDic)}/ Tổng số {len(filePaths)} tập tin ban đầu --> Tiến hành ghi dữ liệu JSON")
print (f"---Tổng số tập tin không Khớp Extension = {len(listDicUnsort)} / Tổng số {len(filePaths)} tập tin ban đầu")
print (f"---Phần mở rộng không Khớp = {listExtUnsort}")

#------------------------------------------------------#
# GHI DỮ LIỆU JSON
#------------------------------------------------------#

jsonPathSorted = dirPath + "\\fileExplorer-sorted.json"
jsonPathUnsort= dirPath + "\\fileExplorer-unsorted.json"
jsonPathFull = dirPath + "\\fileExplorer.json"

flagWritten = False

with open(jsonPathSorted,'w') as jfs:
    jfs.write(json.dumps(listDic,indent=4,sort_keys=True))
    flagWritten = True
with open(jsonPathUnsort,'w') as jfus:
    jfus.write(json.dumps(listDicUnsort,indent=4,sort_keys=True))
with open(jsonPathFull,'w') as jf:
    jf.write(json.dumps(listDic + listDicUnsort,indent=4,sort_keys=True))
#------------------------------------------------------#
# LOAD DỮ LIỆU THÀNH PANDAS DATAFRAME
#------------------------------------------------------#
data = None
if flagWritten:
    print(f"""\tThành công ghi tập tin danh sách File tại: \n\t\t{jsonPathSorted}\n\t\t{jsonPathUnsort}\n\t\t{jsonPathFull} ==""")
    # with open(jsonPath,'r') as jr:
    #     load = json.loads(jr.read())
    #     print(load[0]['Full Path'])
    data = pd.read_json(jsonPathSorted)
    print(data.head(5))
# print(data['File Name'][0:10])

#------------------------------------------------------#
# SẮP XẾP
#------------------------------------------------------#

dicFolder = {}
listFolder = []
for name in data['Pure File Name']:
    try:
        folder = name.split("-")[2]
        dicFolder[folder] = ""
    except:
        pass
listFolder = [d for d in dicFolder]

def createFolders(data,dataColumnName,splitter,splitCount,maxChar):
    dicFolder = {}
    listFolder = []
    for name in data[dataColumnName]:
        try:
            folder = name.split(splitter)[splitCount]
            dicFolder[folder] = ""
        except:
            pass
    listFolder = [d for d in dicFolder if len(d)<=maxChar]
    print("---Tên thư mục được sàng lọc = ",listFolder)
    return dicFolder,listFolder


listFolder1 = createFolders(data,"Pure File Name","-",0,3)
listFolder2 = createFolders(data,"Pure File Name","-",2,3)