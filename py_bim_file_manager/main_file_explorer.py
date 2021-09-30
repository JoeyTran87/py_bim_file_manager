import os, shutil, json
import pandas as pd

class fileExplorer():
    #------------------------------------------------------#
    # THIẾT LẬP ĐIỀU KIỆN
    #------------------------------------------------------#    
    exts =['dwg', 'dwf','rvt', 'rfa', 'rte', 'skp','pdf', 'json', 'txt', 'xls', 'xlsx', 'xlsm', 'doc' , 'docx', 'ai', 'tif','jpg','png', 'gif','bmp','psd', 'jpeg', 'tga', 'ies', 'max']
    needExts = " ".join(exts).lower()
    dic = {"Full Path": None,
            "File Name": None,
            "Pure File Name": None,
            "File Extension": None,
            "Parent Name": None}    
    
    def __init__(self) -> None:
        pass
    def start(self):
        #------------------------------------------------------#
        # INPUT
        #------------------------------------------------------#
        self.dirPath = input("---Nhập đường dẫn:")
        noti1 =f"""---Folder == {self.dirPath} ==Có tồn tại"""
        if os.path.isdir(self.dirPath):
            print(noti1)
            print(f"---Tiến hành duyệt các file có đuôi: ",self.needExts)
        #------------------------------------------------------#
        # DUYỆT FILE
        #------------------------------------------------------#
        for (path,dr,file) in os.walk(self.dirPath):    
            for f in file:
                try:
                    ext = f.split(".")[-1].lower()
                    self.dicExt[ext.lower()] = ""
                    fp = path+"\\"+f
                    self.filePaths.append(fp)                            
                except:
                    pass
        self.fileExts = [d for d in self.dicExt]
        self.stringFileExt = " ".join(self.fileExts)
        print(f"---Tổng số tập tin = {len( self.filePaths)}")
        print(f"---Có Phần mở rộng: { self.fileExts}")
        #------------------------------------------------------#
        # TẠO DICTIONARY
        #------------------------------------------------------#      
        
        for p in self.filePaths:
            try:        
                dicF = self.dic.copy()
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
                
                if et.lower() in self.needExts:
                    dicF["isSorted"] = 'True'
                    self.listDic.append(dicF)
                else:
                    dicF["isSorted"] = 'False'  
                    self.dicExtUnsort[et.lower()] = ""
                    self.listDicUnsort.append(dicF)

            except Exception as ex:
                self.excepts.append(f"====Đã có lỗi: {ex}: {p}")
                pass
        self.listExtUnsort = [d for d in self.dicExtUnsort]
        self.count = len(self.filePaths)
        self.countTrue = len(self.listDic)
        self.countFalse = len(self.listDicUnsort)

        print (f"---Tổng số tập tin Khớp Extension = {self.countTrue}/ Tổng số {self.count} tập tin ban đầu --> Tiến hành ghi dữ liệu JSON")
        print (f"---Tổng số tập tin không Khớp Extension = {self.countFalse} / Tổng số {self.count} tập tin ban đầu")
        print (f"---Phần mở rộng không Khớp = {self.listExtUnsort}")

        #------------------------------------------------------#
        # GHI DỮ LIỆU JSON
        #------------------------------------------------------#

        self.jsonPathSorted = self.dirPath + "\\fileExplorer-sorted.json"
        self.jsonPathUnsort= self.dirPath + "\\fileExplorer-unsorted.json"
        self.jsonPathFull = self.dirPath + "\\fileExplorer.json"
        flagWritten = False

        with open(self.jsonPathSorted,'w') as jfs:
            jfs.write(json.dumps(self.listDic,indent=4,sort_keys=True))
        with open(self.jsonPathUnsort,'w') as jfus:
            jfus.write(json.dumps(self.listDicUnsort,indent=4,sort_keys=True))
        with open(self.jsonPathFull,'w') as jf:
            jf.write(json.dumps(self.listDic + self.listDicUnsort,indent=4,sort_keys=True))

        print(f"""\tThành công ghi tập tin danh sách File tại: \n\t\t{self.jsonPathSorted}\n\t\t{self.jsonPathUnsort}\n\t\t{self.jsonPathFull}""")
        self.data = pd.read_json(self.jsonPathSorted)
        print(self.data.head(5))
        

if __name__ == "__main__":
    """"""
    manager = fileExplorer()
    manager.start()






