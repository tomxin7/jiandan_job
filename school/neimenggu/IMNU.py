
import tomxin.getInfo

def getIMNU():
#内蒙古师范大学
# if __name__ == '__main__':
    url = "http://jy.imnu.edu.cn/c17.jsp"#高校就业网的网址
    html = tomxin.getInfo.get_source_head(url)
    info = tomxin.getInfo.get_info(html,'wrapper','pager')
    title = tomxin.getInfo.get_content(info,'nLink.+?>','</a>')
    url = tomxin.getInfo.get_content(info,'cont.+?href="','"')
    i=0
    for u in url[:]:
        r_city="内蒙古"
        r_school="内蒙古师范大学"
        r_title=title[i]
        r_trait = "IMNU" + u[:-7]#这里要自己写提取规则
        r_url = "http://jy.imnu.edu.cn/" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content_head(r_url,  'content">', '<div id="footer">')
        print(r_title + "\n" + r_url)

