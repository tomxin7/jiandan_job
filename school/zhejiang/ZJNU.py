from urllib import request
import re


import tomxin.getInfo

def getZJNU():
#if __name__ == '__main__':
    url = "http://zjnu.jysd.com/campus"
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'infoTit','pages')
    title = tomxin.getInfo.get_content(info,'_blank">','<')
    url = tomxin.getInfo.get_content(info,'href="','"')
    i=0
    for u in url:
        r_city="浙江"
        r_school="浙江师范大学"
        r_title=title[i]
        r_trait = "ZJNU" + u[-6:]
        r_url = "http://zjnu.jysd.com" + u
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", '</div>-->', 'clear:both')
        print(r_title + "\n" + r_url)
        i += 1
