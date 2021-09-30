import json2html
from json2html import *
import os, sys, json

if __name__ == '__main__':  
    path = os.getcwd()+"\\jsondata.json"
    dic = None
    with open(path,'r',encoding="mbcs") as f:
        dic = json.loads(f.read())
    htmlText = json2html.convert(json = dic,table_attributes='border="1"')
    # print(htmlText)
    base = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        {htmlText}
    </body>
    </html>
    """
    # print(base)
    # htmlPath = os.getcwd()+"\\index.html"
    # with open(htmlPath,'w') as ff:
    #     ff.write(base)
    print(htmlText)