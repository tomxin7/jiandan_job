from urllib import request
import re


import tomxin.getInfo

def getRUC():
#中国人民大学
# if __name__ == '__main__':
    url = "http://rdjy.ruc.edu.cn/html/main/col3/column_3_1.html"
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'columninfolist','listyjin')
    title = tomxin.getInfo.get_content(info,'6060.+?>','<')
    url = tomxin.getInfo.get_content(info,'href="','">')
    i=0
    for u in url[:]:
        r_city="北京"
        r_school="中国人民大学"
        r_title=title[i]
        r_trait = "RUC" + u[-6:-1] #这里要自己写提取规则
        r_url = "http://rdjy.ruc.edu.cn" + u
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", '<!--文章标题与内容-->', '<!--文章标题与内容-->')
        print(r_title + "\n" + r_url)
        i += 1
