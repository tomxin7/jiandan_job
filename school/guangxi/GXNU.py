from urllib import request
import re


import tomxin.getInfo

def getGXNU():
#if __name__ == '__main__':
    url = "http://gxnu.ncss.org.cn/json/general_searchp?callback=jsonp1510741886235&recName=&natureCode=&industryCode=&recScale=&jobTitle=&category=&jobType=%E5%85%A8%E8%81%8C&areaCode=&degreeCode=&dayLimit=-1&siteId=10602&psize=9&callback=test"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = html
    title = tomxin.getInfo.get_content(info,'recName":"','"')
    url = tomxin.getInfo.get_content(info,'jobId":"','"')
    i=0
    for u in url:
        r_city="广西"
        r_school="广西师范大学"
        r_title=title[i]
        r_trait = "GXNU" + u[-18:]
        r_url = "http://gxnu.ncss.org.cn/job/view_job?jobId=" + u
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", '联系方式 -->', '<!--')
        r_content = r_content+"</br><h6>注意：广西师范大学招生网有介绍具体职位，有需要的同学请跳转原页面查看</h6>"
        print(r_title + "\n" + r_url)
        i += 1
