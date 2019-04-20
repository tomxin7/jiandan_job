from urllib import request
import re


import tomxin.getInfo

def getSJTU():
#上海交通大学
# if __name__ == '__main__':
    url = "http://www.job.sjtu.edu.cn/eweb/jygl/zpfw.so?modcode=jygl_zpxxck&subsyscode=zpfw&type=searchZpxx&zpxxType=new"
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'z_newsl','z_pages')
    title = tomxin.getInfo.get_content(info,'500px.+?jygl_scfwzpxx.+?>','</a></div>')
    url = tomxin.getInfo.get_content(info,"url.+?vie.+?'","',")
    i=0
    for u in url[:30]:
        r_city="上海"
        r_school="上海交通大学"
        r_title=title[i]
        r_trait = "SJTU" + u#这里要自己写提取规则
        r_url = "http://www.job.sjtu.edu.cn/eweb/jygl/zpfw.so?modcode=jygl_zpxxck&subsyscode=zpfw&type=viewZpxx&id=" + u
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", '招聘说明：', '附件</td>')
        r_content = r_content+"</br><h6>注意：上海交通大学招生网有介绍具体职位，有需要的同学请跳转原页面查看</h6>"
        print(r_title + "\n" + r_url)
        i += 1

