from urllib import request
import re


import tomxin.getInfo

def getHDU():
#if __name__ == '__main__':
    url = "http://career.hdu.edu.cn/module/getonlines?start_page=1&keyword=&count=15&start=1"
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = html
    title = tomxin.getInfo.get_content(info,'title":"','"')
    url = tomxin.getInfo.get_content(info,'recruitment_id":"','"')
    i=0
    for u in url[:10]:
        r_city="浙江"
        r_school="杭州电子科技大学"
        r_title=title[i]
        r_trait = "HDU" + u
        r_url = "http://career.hdu.edu.cn/detail/online?id=" + u
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", '<div class="details-content">', ' <div class="pub-code">')
        print(r_title + "\n" + r_url)
        i += 1
