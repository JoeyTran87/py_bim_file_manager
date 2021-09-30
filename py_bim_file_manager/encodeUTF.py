import sys, os, json
text = "R:\\BimESC\\01_PROJECTS\\MARUBENI SOLUBE\\01 INCOME\\210609- B\u1ea2N V\u1ebc B\u1ec2 N\u01af\u1edaC V\u00c0 B\u1ec2 XLNT\\1.WWT\\1.ARC\\200428-B\u1ea2N V\u1ebc KI\u1ebeN TR\u00daC WWT\\12\\12-001A-WWT-COVER-LIST.dwg"
text2 = r"R:\BimESC\01_PROJECTS\MARUBENI SOLUBE\01 INCOME\210609- BẢN VẼ BỂ NƯỚC VÀ BỂ XLNT"
# print(text2)
# print(sys.getdefaultencoding())

# print(text)
# print(text2)
# print(text.encode('utf-8'))


t = "\\"
# print (t)
# print(t.encode('utf-8'))
# print(t.encode('utf-8').decode())

tt = u"\\"
# print(tt)
ttt = b"\\"
# print(ttt)

a = '\\'
aa = a.replace('\\', 'a')
b =text2.encode('unicode_escape').decode().replace('\\\\', '\\')
# print(a)
# print(aa)
# print(b)

s = "\\"
raw_s = '{}'.format(s)
# print(s)
# print(raw_s)


res = text2
res2 = bytes(text2, 'utf-8')
txtpath = r"C:\Users\tvpduy\py_html_json\endcoder.json"

# print(res.encode().decode())
# print(res2.decode())
dic = {
    "Full Path 1": text2,
    "Full Path 2": text2
}
print (dic)
print(json.dumps(dic,ensure_ascii= False).replace("\\\\","\\"))
print('\u1234')
print(json.dumps('\u1234',ensure_ascii= False))













# with open(txtpath,'w') as f:
#     f.write(f"{text2.encode()}")
#     print("OK")
    # f.writelines(ttt) #TypeError: write() argument must be str, not int


# text = listDic[0]["Full Path"]
# res = text
# res2 = json.dumps(listDic[0]["Full Path"],ensure_ascii=False).replace("\\\\","\\")
# # print(res)
# txtpath = r"C:\Users\tvpduy\py_html_json\endcoder.txt"
# txtpath2 = r"C:\Users\tvpduy\py_html_json\endcoder2.txt"
# with open(txtpath,'w',encoding="utf-8") as f:
#     f.writelines(res)

# with open(txtpath2,'w',encoding="utf-8") as ff:
#     ff.writelines(res2)

# res2 = json.loads(json.dumps(listDic[0]))
# print(res2["Full Path"])

# print(listDic[0]["Full Path"].encode('utf-8'))