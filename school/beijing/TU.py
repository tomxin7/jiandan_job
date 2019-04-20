from urllib import request
import re


import tomxin.getInfo

#清华大学
def getTU():
#if __name__ == '__main__':
    url = "http://career.cic.tsinghua.edu.cn/xsglxt/f/jyxt/anony/xxfb"
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'chapter1','pgDiv')
    title = tomxin.getInfo.get_content(info,'fbfw.+?>','</a>')
    url = tomxin.getInfo.get_content(info,'ahref="','"')
    i=0
    for u in url:
        r_city="北京"
        r_school="清华大学"
        r_title=title[i]
        r_trait = "TU" + u[-14:-6]#这里要自己写提取规则
        r_url = "http://career.cic.tsinghua.edu.cn/" + u
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", '<!-- 职位描述 -->', '单位简介')
        r_content=r_content+"<br><h6>注意：清华大学部分企业联系方式需要跳转回原网址查看</h6>"
        print(r_title + "\n" + r_url)
        i += 1
