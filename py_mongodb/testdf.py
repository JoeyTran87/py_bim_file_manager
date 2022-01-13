import pandas as pd
import pymongo
from bson import *
df = None

list_ = [{'_id': ObjectId('61b81c268b072789cf9b86a4'), 'vendorName': 'Công Ty TNHH TM-DV Kỹ Nghệ Đại Đông Dương', 'vendorWebsiteUrl': None, 'vendorContactUrl': None, 'vendorPhone': None},
{'_id': ObjectId('61c2e171e13c087d9d1f805d'), 'vendorName': 'Cơ sở Tam Nhất- Bán lẻ đồ điện gia dụng', 'vendorWebsiteUrl': None, 'vendorContactUrl': None, 'vendorPhone': None} ,
{'_id': ObjectId('61c2e175e13c087d9d1f805e'), 'vendorName': 'Hộ Kinh Doanh Cửa Hàng Thiết Bị Điện Thành Đạt', 'vendorWebsiteUrl': None, 'vendorContactUrl': None, 'vendorPhone': None},
{'_id': ObjectId('61c2e17ce13c087d9d1f805f'), 'vendorName': 'Thiết Bị Điện Tuấn Yến', 'vendorWebsiteUrl': None, 'vendorContactUrl': None, 'vendorPhone': None},
{'_id': ObjectId('61c2e1c8e13c087d9d1f8060'), 'vendorName': 'Công ty Cổ Phần Nodare', 'vendorWebsiteUrl': None, 'vendorContactUrl': None, 'vendorPhone': None},
{'_id': ObjectId('61c2e1cbe13c087d9d1f8061'), 'vendorName': 'Cơ sở trang thiết bị PCCC Thăng Long', 'vendorWebsiteUrl': None, 'vendorContactUrl': None, 'vendorPhone': None} ,
{'_id': ObjectId('61d65ed338d50600565a2c1c'), 'vendorName': 'Công ty CFC', 'vendorWebsiteUrl': None, 'vendorContactUrl': None, 'vendorPhone': None},
{'_id': ObjectId('61d672bccdfeeac110fa5756'), 'vendorName': 'Vendor Name 1', 'vendorWebsiteUrl': None, 'vendorContactUrl': None, 'vendorPhone': None},
{'_id': ObjectId('61d7b0970fe2c280e986ff5c'), 'vendorName': 'Vendor Name 1', 'vendorWebsiteUrl': None, 'vendorContactUrl': None, 'vendorPhone': None},
{'_id': ObjectId('61d7b1118c1680f2aee75222'), 'vendorName': 'Vendor Name 1', 'vendorWebsiteUrl': None, 'vendorContactUrl': None, 'vendorPhone': None}]


dic_ = {}
for k in list_[0]:
    dic_[k] = []
for l in list_:
    for k in l:
        dic_[k].append(l[k])

print(dic_)
serrie = pd.Series(dic_)
print(serrie)
df = pd.DataFrame(dic_)
print(df)