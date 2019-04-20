from urllib import request
import re


import tomxin.getInfo


def getPKU():
#北京大学
#if __name__ == '__main__':
    url = "https://scc.pku.edu.cn/home!recruitList.action?category=1"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"UTF-8")
    info = tomxin.getInfo.get_info(html,'id="articleList"','</tbody>')
    title = tomxin.getInfo.get_content(info,'href.+?>','<')
    url = tomxin.getInfo.get_content(info,'href="','"')
    i=0
    for u in url:
        r_city="北京"
        r_school="北京大学"
        r_title=title[i].strip()
        r_trait = "PKU" + u[-31:-5]#这里要自己写提取规则
        r_url = "https://scc.pku.edu.cn/" + u
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", 'articleContext">', '<!-- /#wrapper -->')
        print(r_title + "\n" + r_url)
        i += 1
