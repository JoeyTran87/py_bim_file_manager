"""Tạo text json , copy to clipboard để Add Document bằng Robo 3T hay Studio 3T"""

from tkinter.font import Font
import pandas as pd

import json
import os,time,sys
from pandas.io.formats.format import return_docstring
import pyperclip
import tkinter
from tkinter.constants import *
from tkinter import *
from tkinter import ttk
indent = "-"*4
# ask_form = input(f"{indent}Nhập mẫu JSON: ")
# print(ask_form)

def get_json():
    global textBox_json , textBox_promp, json_text
    json_text = textBox_json.get(1.0,END)
    textBox_promp.insert(0.0,f"{time.strftime('%y%m%d %H:%M:%S',time.localtime(time.time()))} GET JSON\n")
def clear(textBox):
    global textBox_promp
    textBox.delete(1.0,END)
    textBox_promp.insert(0.0,f"{time.strftime('%y%m%d %H:%M:%S',time.localtime(time.time()))} CLEAR\n")
def copy(textBox_res):
    global textBox_promp,copy_text
    copy_text = textBox_res.get(1.0,END)
    textBox_promp.insert(0.0,f"{time.strftime('%y%m%d %H:%M:%S',time.localtime(time.time()))} COPY\n")
    pyperclip.copy(copy_text)
    
def form_data_builder_from_excel(title = "Form Nhập Liệu"):
    global textBox_input,json_text, textBox_promp,textBox_res,textBox_json
    global menu_options,menu_clicked
    global excel,sheet
    
    screen = Tk()
    screen.geometry("540x600")
    screen.iconbitmap(__file__[:-len(__file__.split("\\")[-1])-1]+"\\cofico.ico")
    screen.title(title)

    heading1 = Label(text="Nhập Mẫu JSON",fg="black",height="2",width="30")
    heading1.grid(row=0,column=0,padx=5,pady=5)

    textBox_json = Text(screen, height=5, width=60,pady=5,padx=5)
    textBox_json.grid(row=1,column=0,padx=5,pady=5)

    button_json = Button(screen, height=1, width=15, text= "Get Json", command=lambda: get_json()) 
    button_json.grid(row=2,column=0,padx=5,pady=5)

    button_json_clear = Button(screen, height=1, width=15, text= "Clear Json", command=lambda: clear(textBox_json)) 
    button_json_clear.grid(row=3,column=0,padx=5,pady=5)

    heading2 = Label(text="Nhập PATH Excel",fg="black",height="2",width="30")
    heading2.grid(row=4,column=0,padx=5,pady=5)

    textBox_input=Text(screen, height=2, width=60,pady=5,padx=5)
    textBox_input.grid(row=5,column=0,padx=5,pady=5)

    button_read = Button(screen, height=1, width=15, text= "Read Excel", command=lambda: read_excel(root = screen)) 
    button_read.grid(row=6,column=0,padx=5,pady=5)

    button_Clear = Button(screen, height=1, width=15, text="Clear Path", command=lambda:clear(textBox_input))
    button_Clear.grid(row=7,column=0,padx=5,pady=5)

    textBox_promp=Text(screen, height=5, width=60,pady=5,padx=5)
    textBox_promp.grid(row=8,column=0,padx=5,pady=5)       

    # row 9,10 : select sheet

    button_process = Button(screen, height=1, width=15, text="Process", command=lambda:process_excel())
    button_process.grid(row=11,column=0,padx=5,pady=5)

    textBox_res=Text(screen, height=10, width=60,pady=5,padx=5)
    textBox_res.grid(row=12,column=0,padx=5,pady=5)

    button_copy = Button(screen, height=1, width=15, text="Copy Result", command=lambda:copy(textBox_res))
    button_copy.grid(row=13,column=0,padx=5,pady=5)
    
    mainloop()
    return

def form_select_menu(root= None):
    global menu_options,menu_clicked
    global excel,sheet
    if menu_options:
        label_select = Label(text="Hạy chọn Sheet name",fg="black",height="2",width="30")
        label_select.grid(row=9,column=0,padx=5,pady=5)
        menu_clicked = StringVar()
        menu_clicked.set(menu_options[0])
        drop = OptionMenu(root,menu_clicked,*menu_options)
        drop.grid(row=10,column=0,padx=5,pady=5)
        sheet = menu_clicked.get()

def read_excel(root = None):
    global textBox_input,textBox_promp,textBox_res
    global menu_options,menu_clicked
    global excel,sheet
    excel_path = textBox_input.get("1.0","end-1c")
    # print(excel_path)
    if os.path.isfile(excel_path):
        textBox_promp.insert(0.0,f"{time.strftime('%y%m%d %H:%M:%S',time.localtime(time.time()))} File Excel có tồn tại\n")
        excel = pd.ExcelFile(excel_path)
        menu_options = list(excel.sheet_names)
        print(menu_options)
        form_select_menu(root = root)
    else:
        textBox_promp.insert(0.0,f"{time.strftime('%y%m%d %H:%M:%S',time.localtime(time.time()))} File Excel KHÔNG tồn tại\n")

def process_excel():
    global textBox_input,textBox_promp,textBox_res
    global menu_options,menu_clicked
    global excel, sheet          
    try:
        df = pd.read_excel(excel,sheet_name = sheet,skiprows=1)
        df.drop(df.columns[0:2],axis=1,inplace=True)
        # print(df)
        # df.to_clipboard()
        # df.iloc[-1].to_clipboard()
        # text = pd.read_clipboard()
        text = df.iloc[-1].to_json()
        textBox_promp.insert(0.0,f"{time.strftime('%y%m%d %H:%M:%S',time.localtime(time.time()))} Read Excel\n")
        textBox_res.insert(0.0,f"{text}\n")
    except Exception as ex:
        textBox_promp.insert(0.0,f"{time.strftime('%y%m%d %H:%M:%S',time.localtime(time.time()))} Có lỗi {ex}\n")


if __name__ == "__main__":
    json_text = ""
    copy_text = ""
    textBox_json = None
    textBox_input = None
    textBox_promp = None
    textBox_res = None
    json_sample = None
    menu_options = None
    menu_clicked = None
    excel = None
    sheet = None

    # NHẬP FILE EXCEL:
    form_data_builder_from_excel(title = "Form Nhập Liệu")