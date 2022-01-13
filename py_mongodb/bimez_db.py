import time,os
import pymongo  # install more dnspython for MongoClient
from pymongo.errors import ConnectionFailure
import pandas as pd
import bson
from bson.objectid import ObjectId
import datetime
import numpy as np

def access_database(my_Client):
    """truy cap database"""
    try:
        db_names = sorted(my_Client.list_database_names()) # ['cofico', 'admin', 'local']
        [print(db_names.index(dn)," : ",dn) for dn in db_names]
        while True:
            db = input("Vui lòng chọn số hiệu Database muốn truy cập: ")
            try:
                db = int(db)
                if db < len(db_names):
                    break
            except:
                print("Vui lòng thử lại !")
                pass    
        my_db = my_Client[db_names[int(db)]]
    except:
        ask_db_name = input(f"{indent}Có lỗi / hoặc bạn không có quyền Liệt kê Database name\n{indent}Vui lòng tự chọn tên Database: ")
        my_db = my_Client[ask_db_name]
    return my_db

def access_collection(my_db):
    """truy cap collection database"""
    col_names = sorted(my_db.list_collection_names())
    [print(col_names.index(cn)," : ",cn) for cn in col_names]
    while True:
        cl = input(f"{indent}Vui lòng chọn số hiệu Collection muốn truy cập: ")
        try:
            cl = int(cl)
            if cl < len(col_names):
                my_col = my_db[col_names[int(cl)]]
                break
        except:
            print(f"{indent}Vui lòng thử lại !")
            pass        
    return my_col

def access_document(my_db,my_col):
    """truy cap va xi li collection / document"""
    menu = ["Xem + Copy Clipboard tài liệu","Chèn tài liệu","Xóa tài liệu","Chọn Collection Khác","Tìm kiếm Object Id trong Document","Cập nhật tài liệu"]
    while True:
        try:
            [print(menu.index(mn)," : ",mn) for mn in menu]
            ask_col = input(f"{indent}Vui lòng cho số hiệu Thao Tác tại Collection :{my_col.name}: ")
            df = collection_to_df(my_col)
            # df.astype({'_id': 'string'})
            # list_objectid = df[df.columns[0]]
            # list_objectid = [str(i) for i in df[df.columns[0]]]
            # print("list Id: ",list_objectid)
            if ask_col == '0': 
                print(df)        
                # copy to clipboard
                df.to_clipboard(excel=True, sep=',')
                print(f"{'-'*4}Dữ liệu (dạng CSV - ngăn cách bởi dấu , )Đã được copy vào Clipboar\n{'-'*4}Bạn có thể Paste dữ liệu này vào Excel /các phần mềm khác\n{'-'*4}Với Excel, hãy thiết lập Text To Column dùng Deliemeter là dấu ,\n{indent*10}")
            if ask_col == '1': # insert data to collection
                time_insert = datetime.datetime.now()
                # load json Document cuối làm mẫu
                querry = {"_id": ObjectId(df.iloc[-1]["_id"])}
                last_doc = my_col.find(querry)[0]
                last_serie= df.iloc[-1]
                my_dict = last_serie.to_dict()# print(my_dict)

                # load Excel update data
                while True:
                    excel_path = input(f"{indent}Nhập path Excel dữ liệu\n{indent}(lưu ý File Excel cần theo mẫu thống nhất về Upload Database): ")
                    if os.path.isfile(excel_path):
                        break                
                excel = pd.ExcelFile(excel_path)
                excel_sheets = excel.sheet_names
                while True:
                    try:
                        [print(excel_sheets.index(n)," : ",n) for n in excel_sheets]
                        sheet = input(f"{indent}Chọn số hiệu sheet excel (Vd:0): ")
                        if int(sheet) < len(excel_sheets):
                            break
                    except:
                        pass
                
                df_new = pd.read_excel(excel,sheet_name=excel_sheets[int(sheet)],skiprows=1,)
                df_new.drop(df_new.columns[0:2],axis = 1, inplace = True)
                print(f"{indent}Tài liệu Excel đã được tải",df_new,sep="\n")
                columns = list(df_new.columns)
                while True:
                    try:
                        print(f"{indent}Danh sách các Cột dữ liệu:")
                        [print(columns.index(c),c,sep = " : ") for c in columns]
                        ask_view_column = input(f"{indent}Hãy chọn cột dữ liệu muốn xem\n{indent}(Enter = bỏ qua): ")
                        if columns[int(ask_view_column)]:
                            print(f"Cột {columns[int(ask_view_column)]}:",df_new[columns[int(ask_view_column)]],sep="\n")
                    except:
                        pass
                    if ask_view_column.lower() == "":
                        break
                # kiểm tra dữ liệu load với Database: đã tồn tại hay không
                list_existed = []
                list_non_existed = []
                list_fake_existed=[]
                for i in df_new.index:
                    id = df_new.iloc[i]["_id"]
                    if type(id) == float and np.isnan(id):
                        list_non_existed.append(i)
                        # print("Không có ID")
                    elif type(id) == str:
                        # print(id)
                        querry = {"_id": ObjectId(id)}
                        find = [f for f in my_col.find(querry)]
                        if not len(find)>0:
                            # Trường hợp có ID như KHÔNG tồn tại trong DB
                            list_fake_existed.append(i)
                            # print("Có ID như KHÔNG tồn tại trong DB")
                            pass
                        else:
                            # Trường hop ID đã có tồn tại trong DB
                            list_existed.append(i)
                            # print("Có ID tồn tại trong DB")
                            pass
                print("Data chưa tồn tại",list_non_existed,sep = " : ")
                print("Data chưa tồn tại có ID",list_fake_existed,sep = " : ")
                print("Data đã tồn tại",list_existed,sep = " : ")
                # thực hiện chèn document
                ask_insert = None
                while True:
                    menu_insert = ["Chèn mới document chưa tồn tại","Chèn mới document chưa tồn tại có ID","Cập nhật document đã tồn tại","Tất cả 0,1,2"]
                    [print(menu_insert.index(m),m,sep = " : ") for m in menu_insert]
                    ask_insert = input(f"{indent}Vui lòng chọn cách Insert Document (Q = thoát): ")
                    df_insert = df_new.copy()
                    df_insert.drop(["_id"],axis = 1, inplace = True)
                    try:
                        if menu_insert[int(ask_insert)]:
                            if ask_insert == "0": # chèn mới doc không ID
                                for i in list_non_existed:
                                    dic_doc = df_insert.iloc[i].to_dict()
                                    print(dic_doc)
                                    x = my_col.insert_one(my_dict)
                            if ask_insert == "1": # chèn mới doc có ID
                                for i in list_fake_existed:
                                    dic_doc = df_insert.iloc[i].to_dict()
                                    print(dic_doc)                  
                            if ask_insert == "2": # cập nhật doc đã tồn tại
                                for i in list_existed:
                                    dic_doc = df_insert.iloc[i].to_dict()
                                    print(dic_doc)
                            if ask_insert == "3": # 0,1,2
                                pass     
                    except:
                        pass
                    if ask_insert.lower() == "q":
                        break
            if ask_col == "2":
                pass
            if ask_col == "3":
                my_col = access_collection(my_db)
            if ask_col == "4":
                search_id = input(f"{indent}Vui lòng nhập Object Id muốn tìm kiếm: ")
                querry = {"_id":search_id}
                result = [r for r in my_col.find(querry)]
                # print(f"{indent}Kết quả tìm kiếm: ",search_id in list_objectid)
                if len(result)>0:
                    print(f"Đã tìm thấy Object iD: {search_id}")
                    print(result[0])
            
            if ask_col.lower() == "q":
                break
        except Exception as ex:
            print(f"{indent}Lỗi! {indent}{ex}")
            print(f"{indent}Vui lòng thử lại !")
            pass
def collection_to_df(my_col):
    my_doc = list(my_col.find())
    dic_ = {}
    # [print(d) for d in my_doc]
    for k in my_doc[-1]:
        dic_[k] = []
    for l in my_doc:
        for k in dic_:
            try:
                dic_[k].append(l[k])
            except:
                dic_[k].append(None)
    df = pd.DataFrame(dic_)
    return df

try:
    if __name__ == "__main__":
        indent = "-"*4
        db_v1_path = "mongodb+srv://coficoviewer:YEDbSU2Y2LAN3XBT@cluster0.amf85.mongodb.net/cofico?retryWrites=true&w=majority"
        db_v2_path = "mongodb+srv://tvpduy:l2MYl6FG0DxVgx2U@ezweb.sryaz.gcp.mongodb.net/b4pez?retryWrites=true&w=majority"

        bimez_vers = ["BIM ez Verion 1-Author: htphong","BIM ez Version 2-Author: luvo"]
        [print(bimez_vers.index(ez)," : ",ez) for ez in bimez_vers]
        while True:
            ask_ez = input(f"{indent}Vui lòng chọn Số hiệu Version BIM EZ Database: ")
            if ask_ez == "0":
                my_Client = pymongo.MongoClient(db_v1_path)
                break
            if ask_ez == "1":
                my_Client = pymongo.MongoClient(db_v2_path)
                break
        try:
            # The ping command is cheap and does not require auth.
            my_Client.admin.command('ping')
            print("Server available")
        except ConnectionFailure:
            print("Server not available")

        # truy cap database
        my_db = access_database(my_Client)

        menu_db = ["Tiếp tục access vào Collection cụ thể","Tìm kiếm Object Id trên toàn bộ các Collection"]
        while True:
            try:
                print(f"{indent}Các tác vụ với Database:")
                [print(menu_db.index(md)," : ",md) for md in menu_db]
                ask_db = input(f"{indent}Vui lòng chọn số hiệu Tác vụ: ")
                if ask_db =="0":
                    break
                if ask_db == "1":
                    search_id = input(f"{indent}Vui lòng nhập Object Id muốn tìm kiếm: ")
                    querry = {"_id":ObjectId(search_id)}
                    # print(ObjectId(search_id))
                    list_df = []
                    col_names = sorted(my_db.list_collection_names())
                    for n in col_names:
                        try:
                            print(f"{indent*2}{n}{indent*4}")
                            my_col = my_db[n]
                            # list_df.append(collection_to_df(my_col))
                            result = [r for r in my_col.find(querry)]
                            if len(result) > 0:
                                print(f"Đã tìm thấy Object iD: {search_id} trong collection {indent}{n}")
                                print(result[0])
                                break
                        except:
                            pass
                    # print(f"{indent}Số bảng Document đã xử lí: {len(list_df)}")
            except:
                pass
        
        # menu trên toàn Database


        # truy cap collection database
        my_col = access_collection(my_db)

        # truy cap va xi li collection / document
        access_document(my_db,my_col)
except KeyboardInterrupt:
    quit()

