import webbrowser

path = r"F:\_NGHIEN CUU\_Github\py_bim_file_manager\py_BIM_4_html-210709\base.html"
# webbrowser.get("google-chrome").open(path)
# webbrowser.get("firefox").open(path)
# webbrowser.open('http://google.com')

url = "file:///"+ path
webbrowser.open(url,new=2)