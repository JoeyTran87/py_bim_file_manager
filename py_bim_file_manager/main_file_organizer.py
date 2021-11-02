
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#

import os, shutil,time
# from main_file_explorer import *
from fileDelete import *
from fileDelete import delete_exts

from fileMetadata import *

#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#

#-------------------------------------------------#
# TẠO FOLDER CHỨA CÁC LOẠI ĐUÔI FILE TRONG TỪNG CHILD CỦA ROOT
#-------------------------------------------------#
def createEXTfolders (dirpath,needExts):
    for e in needExts:
        try:
            extFolderDir = dirpath + "\\" + e.upper()
            if not os.path.exists(extFolderDir):
                os.mkdir(extFolderDir)
        except:
            pass
    print("\t\t---Hoàn tất tạo Folder chứa tập tin")
def createEXTfolders2 (extFolderDir):
    try:
        if not os.path.exists(extFolderDir):
            os.mkdir(extFolderDir)
            print("\t\t---Hoàn tất tạo Folder: ",extFolderDir)
    except:
        pass
    
def handleFiles(newFp,newDir,fp,copyFp,ask_move):
    """
        TRÌNH XỬ LÍ TÂP TIN: XÉT TẬP TIN CÓ TỒN TẠI THÌ THỰC HIỆN COPY
        NẾU ĐƯỢC YẾU CẦU XÓA TẬP TIN THÌ SẼ XÓA FILE SAU KHI COPY
    """
    if not os.path.exists(newFp): # NẾU FILE CHƯA TỒN TAI --> THỰC HIEN COPY TẬP TIN + THÔNG TIN NGÀY MODIFIED CUỐI CÙNG
        if os.path.exists(newDir):
            try:
                modTimeNameField = fp.split("\\")[-1].split("-")[-1].split(".")[0]
                if len(modTimeNameField) == 12:
                    newFp = copyFp                    
            finally:
                shutil.copy(fp,newDir)
                os.rename(copyFp,newFp)
                try:
                    if ask_move == "y":
                        os.remove(fp)
                except:
                    pass

def deleteZeroSizeFolder(dirpath):
    """
        XỬ LÍ XÓA FOLDER TRỐNG
    """
    pass
def organizer(dirpath,ask_move):
    """
        TRÌNH XỬ LÍ SẮP XẾP
    """
    flagIsDir = False
    count_done = 0
    sum_size = []
    if os.path.isdir(dirpath):
        flagIsDir = True
        print (f"\t\t---Thư mục có tồn tại {dirpath}")
    if flagIsDir:
        # createEXTfolders (dirpath,exts)
        for (path,dir,files) in os.walk(dirpath):         
            for f in files:
                try:
                    ext = f.split(".")[-1] # ĐUÔI FILE - EXTENSION                    
                    prp = path.split("\\")[-2]# TÊN FOLDER CHỨA (PARENT)        
                    flagNoNeed = prp == ext.upper()
                    fp = path + "\\" + f # FULL TÊN FILE + PATH      
                    nfn = f[:-len(ext)-1]+"-"+time.strftime("%y%m%d%H%M%S",time.localtime(float(os.stat(fp).st_mtime)))+"."+ext # TÊN MỚI + THỜI GIAN LƯU LAST
                    newDir = dirpath + "\\" + ext.upper() #TÊN FOLDER MỚI THEO EXT
                    createEXTfolders2 (newDir) # TAO FOLDER
                    copyFp = newDir + "\\" + f # TÊN CŨ TRONG FOLDER MỚI
                    newFp =  newDir + "\\" + nfn # TÊN MỚI TRONG FOLDER MỚI
                    if flagNoNeed == False: # NẾU FOLDER DANG CHỨA KHÔNG PHẢI TÊN DUÔI FILE UPPER
                        handleFiles(newFp,newDir,fp,copyFp,ask_move)
                        count_done += 1
                        sum_size.append(get_file_size(newFp))
                    else:
                        pass
                # else:
                except Exception as exx:
                    print(f"======LỖI: {exx}")  
                    if not "are the same file" in f"{exx}":
                        unsortDir = dirpath + "\\" + "UNSORT"
                        createEXTfolders2 (unsortDir)
                        copyFp = unsortDir + "\\" + f # TÊN CŨ TRONG FOLDER MỚI
                        newFp =  unsortDir + "\\" + nfn # TÊN MỚI TRONG FOLDER MỚI
                        handleFiles(newFp,unsortDir,fp,copyFp,ask_move)
                    else:
                        pass
                finally:
                    pass
    print(f"\t\tHoàn tất sắp xếp file: {count_done} - tập tin - {round(sum(sum_size))} MB - đã được sắp xếp")

def main():
    promp_menu = """
    ------------------------------------------------------------------------------------------------
                            MENU CHƯƠNG TRÌNH SẮP XẾP TẬP TIN / DỮ LIỆU
    ------------------------------------------------------------------------------------------------
    \t1.\tXóa tập tin không cần thiết           1.1 Xóa các tập tin theo Extension tùy chỉnh
                                                1.2 Xóa các tên file theo Bộ tìm kiếm Tên file
    \t2.\tSắp xếp tập tin                       
    
    """
    """
    \t3.\tThiết lập chương trình                3.1 Thiết lập Bộ xóa file tự động
                                                3.2 Thiết lập Bộ sắp xếp file tự động    
    \t4.\tTra cứu tập tin                       4.1 Tra cứu theo Xu hướng thông tin
    \t0.\tThoát chương trình

    \t---Vui lòng chọn số hiệu thao tác: """
    promp_back_to_menu = "\t\t---Thao tác hoàn tất , hoặc không thể tiếp tục, Bạn đang trở lại Menu---"
    promp_delete = "\t---Đường dẫn ROOT(để tiến hành Xóa file): "
    promp_organize = "\t---Đường dẫn ROOT (để xắp xếp tập tin): "
    promp_move_file = "\t---Bạn có muốn Di dời file? (y/n): "
    promp_mode_orgnaize = "\t---MODE Tạo thư mục dữ liệu mới tại (0 = tại Folder ROOT, 1 = tại cấp folder CON thứ 1st trong ROOT): "
    promp_skip_delete = "\t\t---Bạn chưa thực hiện Xóa tập tin, bạn muốn bỏ qua thao tác xóa (y/n): "

    promp_trend_lookup = """\t Hiện có các Xu hướng tìm kiếm thông tin sau, bạn có thể lựa chọn:
    \tSOW   
    \t
    \t
    \t    
    """
    print("\t----------Chào mừng bạn đến với Chương trình sắp xếp Tập tin dữ liệu---------".upper())
    flag_deleted_already = False
    ask_menu = input(promp_menu)
    path_root = ""

    while True:
        if ask_menu == "1":
            #----------------------------------#
            # DELETE FILE
            #----------------------------------#
            askDelete = input(f"\t---Bạn muốn xóa các tập tin có Extension trong Bảng danh sách sau?\n\t\t---{promp_extensions(delete_exts)}\n\t---(y/n): ").lower()
            if askDelete == "y":
                path_root = input(promp_delete)
                delete_file_match_extension(path_root,delete_exts)
                flag_deleted_already = True  
        if ask_menu == "2":
            #----------------------------------#
            # SẮP XẾP FILES
            #----------------------------------#
            ask_skip_delete = "n"
            if not flag_deleted_already:
                ask_skip_delete = input(promp_skip_delete).lower()
            if flag_deleted_already or ask_skip_delete == "y":
                ask_confirm_path_root = "n"                
                if len(path_root) == 0:
                    path_root = input(promp_organize)
                if len(path_root) > 0:
                    ask_confirm_path_root = input(f"\t---Path Root = {path_root}, vui lòng xác nhận sử dụng Path Root này(y/n): ").lower()
                    if ask_confirm_path_root == "n":
                        path_root = input(promp_organize)
                if ask_confirm_path_root == "y":
                    childLevel = int(input(promp_mode_orgnaize))
                    ask_move = input(promp_move_file).lower()
                    #THỰC HIỆN SẮP XẾP
                    if childLevel == 0:
                        organizer(path_root,ask_move)
                    if childLevel == 1:
                        for d in os.listdir(path_root):
                            organizer(path_root+"\\"+d,ask_move)
        
        if ask_menu == "0":
            time_end = time.strftime("%H:%M:%S %a %d %b %Y ",time.localtime(time.time()))
            print(f"---Bạn đang thoát chương trình vào lúc {time_end}")
            quit()

        print("\t\t---Bạn vừa thực hiện Mã hiệu lệnh: ",ask_menu,"\n",promp_back_to_menu)        
        ask_menu = input(promp_menu)



#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        time_end = time.strftime("%H:%M:%S %a %d %b %Y ",time.localtime(time.time()))
        print(f"---Bạn đang thoát chương trình vào lúc {time_end}")
        quit()