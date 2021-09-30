import os, sys, json
import pandas as pd

from fileMetadata import *



class FileDelete():
    def __init__(self,jsonPathSorted,deleteExts) -> None:
        #------------------------------------------------------#
        # LOAD DỮ LIỆU JSON THÀNH PANDAS DATAFRAME
        #------------------------------------------------------#
        self.data = pd.read_json(jsonPathSorted)
        self.deleteExts = deleteExts
    def delete(self):
        for i in self.data.index:
            if self.data['File Extension'][i] in self.deleteExts:
                try:
                    os.remove(self.data['Full Path'][i])
                except:
                    pass

# deleteExts = ['bak', 'zip', 'rar', 'pcp'
# , 'db', 'mpp', 'log', 'mat', 'rws', 'slog', 'dat'
# , 'vrmesh', 'tmp', 'vrlmap', 'vrmap', 'eps'
# , 'dropbox', 'ini', 'ctb', '7z', 'pc3', 'fmp', 'fas', 'dwl', 'err', 'skb']

# exts =['dwg', 'dwf','rvt', 'rfa', 'rte', 'skp','pdf', 'json', 'txt', 'xls', 'xlsx', 'xlsm', 'doc' , 'docx', 'ai', 'tif','jpg','png', 'gif','bmp','psd', 'jpeg', 'tga', 'ies', 'max']

def deleteZeroSizeFolder(dirpath):
    # print(os.listdir(dirpath))
    for d in os.listdir(dirpath):
        path = dirpath+"\\"+d
        stat = os.stat(path)
        size = round((float(stat.st_size)),3)     
        print(f"{path} : {size}")        
        if size == 0:
            try:           
                os.remove(path)
                print("---Thành công xóa thư mục Zero size: ",path)
            except Exception as ex:
                print(ex)
                pass



delete_exts = ['zip','rar','7z','bak','dwl','dwl2','db','pcp','pc3','tmp','skb','slog','log',
    'dat','ctb','fmp','dst','ds$','rws','err','exe','xmpses','m4v','aac','pek','fas','ini',
    'ds_store','exr','msg','his','axm','gxf','fas','prtl','swf','stb','partial','mtt','nzip','backup']

def delete_file_match_extension(path_root_delete,delete_exts):
    count = 0
    file_sizes_deleted = []
    for (path,dir,files) in os.walk(path_root_delete):
        try:            
            for f in files:
                try:
                    ext = f.split(".")[-1].lower()
                    file_path = f"{path}\\{f}"
                    if ext in delete_exts:
                        file_sizes_deleted.append(get_file_size(file_path))
                        # os.remove(file_path)
                        os.unlink(file_path)
                        count +=1
                except Exception as ex:
                    pass
        except Exception as ex:
            pass
    print(f"\t\t---Đã xóa: {count} đối tượng ---Tổng dung lượng: {round(sum(file_sizes_deleted))} MB")

#------------------------------------------------------#
#       NHẮC NHỞ VỂ CÁC EXTENSION CỦA TẬP TIN
#------------------------------------------------------#
def promp_extensions(delete_exts):
    df1 = pd.DataFrame(pd.Series(delete_exts[:round(len(delete_exts)/2)]))
    df2 = pd.DataFrame(pd.Series(delete_exts[round(len(delete_exts)/2):]))
    df = "----"+df1+"----"+df2+"----"
    df.columns = ['Extension']
    return df


#------------------------------------------------------#
#       XÓA FOLDER
#------------------------------------------------------#

def remove_dir(dir_path):
    if os.path.exists (dir_path):
        try:
            os.rmdir("myfolder")
            print(f"\t\tHoàn tất xóa folder {dir_path}")
        except:
            pass
