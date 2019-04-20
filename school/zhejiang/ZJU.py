from urllib import request
import re


import tomxin.getInfo

def getZJU():
#if __name__ == '__main__':
    url = "http://www.career.zju.edu.cn/ejob/zpxxmorelogin.do"
    html = tomxin.getInfo.get_source(url,"gbk")#获取网页源码
    info = tomxin.getInfo.get_info(html,'点击量','<tr height="40px">')#去掉头尾，只要列表内容
    title = tomxin.getInfo.get_content(info,'png"/>','</a>')#获取标题
    url = tomxin.getInfo.get_content(info, 'target="_blank".+?href="', '">')
    i=0
    for u in url[0:7]:
        r_city="浙江"
        r_school="浙江大学"
        r_title=title[i].strip()
        r_trait = "ZJU" + u[-18:]
        r_url="http://www.career.zju.edu.cn/ejob/"+u
        r_content = tomxin.getInfo.get_url_content(r_url, "gbk", '用人单位简介</p>', '<div class="botframe_23">')#这里获得详情页的内容
        r_content="<h3>企业介绍</h3>"+r_content+"<h6>注意：浙大部分企业有详细职位介绍，请点击原网址查看</h6>"
        print(r_title + "\n" + r_url)
        i += 1
