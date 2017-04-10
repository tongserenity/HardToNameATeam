"""
2017 - 4 - 10 neko34
将获得的写到数据库中，目前还是暂时写到SampleData中
"""

import WebAPI.GetAPIData as gad

# 取PM2.5的网址
pm2_5Url = ""

# 从GetAPIData模块中获取urlString
def getData(urlString):
    htmlAns = gad.openUrl(urlString)

    return htmlAns

# 写入数据存储中，现在目前是SampleData.txt
def writeToDB(dataToStore, addrStore):
    myfile = open(addrStore, "w+")
    myfile.write(dataToStore)