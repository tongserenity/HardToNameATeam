import urllib.request as ur
import urllib
"""
2017 - 4 - 10 neko34
从网络中获取对应的数据，调用对应的API
"""


def openUrl(urlString):
    html = ur.urlopen(urlString).read()

    return html

