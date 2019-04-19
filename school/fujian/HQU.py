from urllib import request
import re
import pymysql

import tomxin.getInfo
import _thread


def getHQU():
# if __name__ == '__main__':
    url = "http://bys.hqu.edu.cn/zpzl/zpxx.htm"
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,"line_u3_0","</table>")
    title = tomxin.getInfo.get_content(info,'title="','">')
    url = tomxin.getInfo.get_content(info, 'href="..', '"')
    i=0
    for u in url[0:7]:
        r_city="福建"
        r_school="华侨大学"
        r_title=title[i]
        r_trait = "HQU" + u[-9:-4]
        r_url="http://bys.hqu.edu.cn/"+u
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", 'artibody">', '<div class="viewBottomTools">')
        if r_content.find("下载免费小巧") == -1:#这是筛选没有福昕的内容才插入数据库
            tomxin.setMysql.setWorkhub(r_city,r_school,r_title,r_content,r_trait,r_url)
        i += 1
