import qrcode,time
import os
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
#----------------------------------------------------------------------------#
def png_convert_jpg(file_path):
    if file_path.split(".")[-1].lower() == "png":
        with Image.open(file_path) as im:
            print(im.format, im.size, im.mode)
            # im.show()
            oim = file_path[:-len(file_path.split(".")[-1])-1]+".jpg"
            im.save(oim)
def qr_generate(data,data_tag,font_path = r"C:\Windows\Fonts\arial.ttf",font_size = 20,fn_prefix = None,save_dir = "",show_im = False):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    time_ =time.strftime("%y%m%d%H%M%S",time.localtime(time.time()))
    if fn_prefix == None:
        fn_prefix = "QR_file"
    
    if not save_dir == "" and os.path.isdir(save_dir):
        save_dir = f"{save_dir}\\"
    img_path = f"{save_dir}{fn_prefix}-{time_}.png"
    img.save(f"{save_dir}{fn_prefix}-{time_}.png")

    if os.path.isfile(img_path):
        qr_write_tag(img_path,data_tag,font_path = font_path,font_size = font_size,show_im = show_im)
    return img_path

def qr_write_tag(img_path,data_tag,font_path = r"C:\Windows\Fonts\arial.ttf",font_size = 20,show_im = False):
    time_ =time.strftime("%y%m%d%H%M%S",time.localtime(time.time()))
    save_im_path = "{0}-{1}-{2}{3}".format(img_path[:-len(img_path.split(".")[-1])-1],"writetext",time_,".png")
    with Image.open(img_path) as im:
        # im.show()
        draw = ImageDraw.Draw(im)
        textfont = ImageFont.truetype(font_path,font_size)
        draw.text((5,5),data_tag,fill="black",font=textfont)        
        im.save(save_im_path)
    if os.path.isfile(save_im_path):
        os.remove(img_path)
        os.rename(save_im_path,img_path)
    if show_im:
        with Image.open(img_path) as im2:
            print(im.format, im.size, im.mode)
            im2.show()
def excel_data_to_qr(row = 2):
    while True:
        try:
            excel_path = input("Đường dẫn file excel: ")#r"D:\OneDrive - COFICO\+WFH\py_qr_code\BIMEZ - Danh mục theo dõi và kiểm soát thiết bị tại Văn phòng.xlsx"
            if os.path.isfile(excel_path):
                break
        except Exception as ex:
            print(ex)
            print("!!!  Nhập sai, vui lòng nhập lại")
            pass

    excel = pd.ExcelFile(excel_path)
    print(f"Excel file:\n\t{excel_path}\nSheet name list:")
    [print("\t",shn) for shn in excel.sheet_names]
    while True:
        try:
            sheet_name = "DATA"#input("Tên Sheet: ")
            if sheet_name in excel.sheet_names:
                break
        except Exception as ex:
            print(ex)
            print("!!!  Nhập sai, vui lòng nhập lại")

    df = pd.read_excel(excel,sheet_name = sheet_name)
    print("Excel Sheet Data:\n")
    print(df)

    print("Column list:\n")
    columns = list(df.columns)
    print("\tSố hiệu\t Tên Cột")
    [print("\t",columns.index(c),":",c) for c in columns]

    while True:
        try:
            qr_value_col = int(input("[Số hiệu] cột cho Dữ liệu Mã QR:"))
            if qr_value_col:
                break
        except Exception as ex:
            print(ex)
            print("!!!  Nhập sai, vui lòng nhập lại")
            pass
    while True:
        try:
            qr_tag_cols = [int(i) for i in input("[Các Số hiệu] cột cho Tag QR:(ex: 1,2,11,12)").split(",")]
            if qr_tag_cols.__class__.__name__ == "list":
                break
        except Exception as ex:
            print(ex)
            print("!!!  Nhập sai, vui lòng nhập lại")
            pass

    qr_values = list(df[columns[qr_value_col]])
    if row == 1:
        qr_tags = ["__".join([df.iloc[i][columns[c]] for c in qr_tag_cols]) for i in list(df.index)]
    if row > 1:
        try:
            div = int(len(qr_tag_cols)/row)
            qr_tags = ["\n".join(["__".join([df.iloc[i][columns[qr_tag_cols[c+d]]] for d in range(div)]) for c in range(0,len(qr_tag_cols),div)]) for i in list(df.index)]
        except:
            qr_tags = ["__".join([df.iloc[i][columns[c]] for c in qr_tag_cols]) for i in list(df.index)]

    print("\tQR Value\tQR Text Tag")
    [print(f"\t{v}\t{qr_tags[qr_values.index(v)]}") for v in qr_values]
    # print(", ".join(qr_values))
    # [print(t) for t in qr_tags]

    while True:
        try:
            save_dir = input("Đường dẫn folder lưu file anh QR: ") #r"D:\OneDrive - COFICO\+WFH\py_qr_code"
            if os.path.isdir(save_dir):
                break
        except Exception as ex:
            print(ex)
            print("!!!  Nhập sai, vui lòng nhập lại")
            pass

    if len(qr_values) == len(qr_tags):
        im_paths = []
        count_done = 0
        count_total = len(qr_values)
        for data in qr_values:
            try:
                data_tag = qr_tags[qr_values.index(data)]
                im_path = qr_generate(data,data_tag,font_size = 10,fn_prefix = data,save_dir=save_dir)
                im_paths.append(im_path)
                count_done +=1
                print(f"Tạo thành công: {count_done}/{count_total}")
            except Exception as ex:
                print(ex)
                pass
        return im_paths

def merge_im(im_paths, col = 2, row = 3,prefix = "Merge",time_ = None,save_dir_path = None):
    # dir_path = r"D:\OneDrive - COFICO\+WFH\py_qr_code\qrcode_im" #input("Đường dẫn: ")
    # im_paths = [f"{dir_path}\\{d}" for d in os.listdir(dir_path)]#[d for d in os.listdir(dir_p)]#
    groups = []
    if time_ == None:
        time_ =time.strftime("%y%m%d%H%M%S",time.localtime(time.time()))    
    if save_dir_path == None:
        while True:
            try:
                save_dir_path = input("Đường dẫn lưu Merge Image: ")
                if os.path.isdir(save_dir_path):
                    break
            except:
                pass    
    for p in range(0,len(im_paths),col*row):
        groups.append(im_paths[p:p+col*row])    

    with Image.open(im_paths[0]) as first_im:
        w,h = first_im.size

    count_done = 0
    count_total = len(groups)
    for g in groups:
        try:
            save_im_p = f"{save_dir_path}\\{prefix}-{time_}-{groups.index(g)}.png"
            im_merge = Image.new("RGBA",(w*col,h*row),"white")
            for r in range(0,len(g),col):
                im_p = g[r]
                with Image.open(im_p) as imr:
                    im_merge.paste(imr,(0,int(h*(r/col))))
                    # im_merge.save(save_im_p)
                for c in range(1,col):
                    im_p_c = g[r+c]
                    with Image.open(im_p_c) as imrc:
                        im_merge.paste(imrc,(int(w*c),int(h*(r/col))))
                        # im_merge.save(save_im_p)
            im_merge.save(save_im_p)
            count_done += len(g)
            print(f"Tạo thành công: {count_done}/{count_total}")
        except Exception as ex:
            print(ex)
            pass

    return groups


#----------------------------------------------------------------------------#

if __name__ == "__main__":
    # data = """Stt	1
    # Tên thiết bị	Máy Lạnh
    # Quy cách	Panasonic 2HP
    # """
    # data_tag = """May Lanh__Panasonic 2HP__MLA001__Phong Tai Xe__06/12/21"""    
    # qr_generate(data,data_tag,font_size=15)
    im_paths = excel_data_to_qr(row=2)    
    print(merge_im(im_paths,col = 2, row = 3))

