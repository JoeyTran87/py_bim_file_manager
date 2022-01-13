#! python3
# scap_bim_ez.py - Something here...
# command line or clipboard

import webbrowser,sys,pyperclip
import requests
import bs4

# 1 --- truy cập web b4p

address = None
if len(sys.argv) > 1:
    address = "".join(sys.argv[1]) #dùng đối số System
else:
    address = pyperclip.paste() # dùng clipboard
print(address)
webbrowser.open(address)#"https://b4p.cofico.com.vn/")

# 2 --- đăng nhập nếu chưa đăng nhập

res = requests.get(address)
try:
    res.raise_for_status()
except Exception as ex:
    print('There was a problem: %s' %(ex))
html_text = res.text
print("RESPONSE TYPE: ",type(res))
print("RESPONSE CODE: ",res.status_code) # code 200 = succeeded
print("HTML TEXT LENGTH: ",len(html_text))
# print(html_text)

soup = bs4.BeautifulSoup(html_text,'html.parser')
print("SOUP TYPE: ",type(soup))

# 3 --- vào dự án

#