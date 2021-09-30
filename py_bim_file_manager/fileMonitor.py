import os, shutil,time






#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
if __name__ == '__main__':  
    dirpath = r"C:\Users\USER\Documents\GitHub\cofico\cofico\FROM BIM MASTER TEMP 210412\Python\py_html_json\organizer"#r"C:\Users\tvpduy\py_html_json\organizer"
    listExt = []
    needExts = ['csv']#['txt','json','xls','csv','xml']
    if os.path.isdir(dirpath):
        try:
            for (path,dir,files) in os.walk(dirpath):
                for f in files:
                    # print (f)
                    ext = f.split(".")[1]
                    if ext in needExts:
                        # print(ext)
                        extFolder = ext[0:].upper()
                        extFolderDir = dirpath + "\\" + extFolder
                        # print(extFolderDir)
                        filePath = dirpath+"\\"+f                    
                        newFilePath = extFolderDir+"\\"+f
                        # print(newFilePath)
                        if not os.path.exists(newFilePath):                        
                            copyTime = time.strftime("%y%m%d %H%M%S",time.localtime(time.time()))
                            renamedFilePath = extFolderDir+"\\"+f.split(".")[0]+"-"+copyTime+"."+ext
                            # print(newFilePath)
                            # print(renamedFilePath)
                            if os.path.exists(extFolderDir):
                                shutil.copy(filePath,extFolderDir)                            
                                os.rename(newFilePath,renamedFilePath)
                            else:                    
                                os.mkdir(extFolderDir)
                                shutil.copy(filePath,extFolderDir)
                                os.rename(newFilePath,renamedFilePath)
                        else:
                            pass
        except Exception as ex:
            print(ex)
            pass