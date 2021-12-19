import os, time
from PIL import Image
#---------------------------------------------#
def lowsize_png(file_paths):    
    while True:
        try:
            percentage = float(input("Tỉ lệ % muốn giảm: (%)"))/100
            if percentage <= 1:
                break
        except:
            pass
    while True:
        try:
            max_size = float(input("Dung lượng tối da mong muốn: (Mb) "))*1024*1024
            if max_size > 0:
                break
        except:
            pass
    count_done = 0
    for file_path in file_paths:
        if file_path.split(".")[-1].lower() in ["png","jpg"]:
            try:
                if os.path.isfile(file_path):
                    file_size = os.path.getsize(file_path) # byte
                    # if file_size > max_size:
                    with Image.open(file_path) as im:
                        w,h = im.size
                        pipeline_loop = 1
                        while True:
                            lower_im = im.resize(
                                    (   int(w*(1-percentage*pipeline_loop)),
                                        int(h*(1-percentage*pipeline_loop))
                                    )
                                )
                            print(im.format, im.size, im.mode)
                            print(lower_im.format, lower_im.size, lower_im.mode)
                            time_ =time.strftime("%y%m%d",time.localtime(time.time()))
                            
                            lower_im_path = "{0}-{1}{2}".format(file_path[:-len(file_path.split(".")[-1])-1],time_,".png")
                            lower_im.save(lower_im_path)
                    
                            if os.path.isfile(lower_im_path) and os.path.getsize(lower_im_path) > max_size:
                                os.remove(lower_im_path)
                                pipeline_loop += 1  
                            else:
                                break
                count_done += 1
            except Exception as ex:
                print(ex)
                pass
        print(f"Succcessfull resize {count_done}/{len(file_paths)}")

#---------------------------------------------#

if __name__ == "__main__":
    while True:
        dir_path = input("Đường dẫn folder: ")        
        if os.path.isdir(dir_path):
            break

    file_paths = [f"{dir_path}\\{p}" for p in os.listdir(dir_path) if p.split(".")[-1].lower() in ["jpg","png"]]
    [print (f) for f in file_paths]

    lowsize_png(file_paths)