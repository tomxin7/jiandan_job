from urllib import request
import re


import tomxin.getInfo

def getXMU():
# if __name__ == '__main__':
    url = "http://jyzd.xmu.edu.cn/platform/require_list?level1=1&level2=0"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'baseinfo','pagination-father')
    title = tomxin.getInfo.get_content(info,'title="','"')
    url = tomxin.getInfo.get_content(info,'href="','"')
    i=0
    for u in url:
        r_city="福建"
        r_school="厦门大学"
        r_title=title[i]
        r_trait = "XMU" + u[-4:]
        r_url = "http://jyzd.xmu.edu.cn/" + u
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", '<hr style="background-color:#ddd;height:1px"/>', '</form>')
        print(r_title + "\n" + r_url)
        i += 1
