from urllib import request
import re


import tomxin.getInfo

def getFU():
#复旦大学
#if __name__ == '__main__':
    url = "http://www.career.fudan.edu.cn/jsp/recruit_info_list.jsp"
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'</head>','</body>')
    title = tomxin.getInfo.get_content(info,'key.+?title="','"')
    url = tomxin.getInfo.get_content(info,'key="','"')
    i=0
    for u in url:
        r_city="上海"
        r_school="复旦大学"
        r_title=title[i]
        r_trait = "FU" + u#这里要自己写提取规则
        r_url = "http://www.career.fudan.edu.cn/html/qzxx/zpxx/1.html?view=true&key=" + u
        title_url_real = r_url.replace('http://www.career.fudan.edu.cn/html/qzxx/zpxx/1.html?view=true&','http://www.career.fudan.edu.cn/jsp/recruit_info_detail.jsp?')
        r_content = tomxin.getInfo.get_url_content(title_url_real, "utf-8", '<div style="width:732px; overflow-y:auto;">', '<!--基本')
        print(r_title + "\n" + r_url)
        i += 1
