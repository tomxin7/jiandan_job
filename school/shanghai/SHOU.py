from urllib import request
import re


import tomxin.getInfo

def getSHOU():
#上海海洋大学
#if __name__ == '__main__':
    url = "http://jy.shou.edu.cn/#"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"gbk")
    info = tomxin.getInfo.get_info(html,'（全职）','c2_list_b')
    title = tomxin.getInfo.get_content(info,'_blank" >','</a>')
    url = tomxin.getInfo.get_content(info,'c2_list_text.+?href="','"')
    i=0
    for u in url:
        r_city="上海"
        r_school="上海海洋大学"
        r_title=title[i]
        r_trait = "SHOU" + u[-32:]#这里要自己写提取规则
        r_url = u
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", 'jobcontent">', '<!-- 职位收藏 -->')
        print(r_title + "\n" + r_url)
        i += 1
