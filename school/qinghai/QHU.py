
import tomxin.getInfo

def getQHU():
#青海大学
# if __name__ == '__main__':
    url = "http://jyw.qhu.edu.cn/jyxx/tzgg_jyxx/zpxx/index.htm"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'pageList','class="page">')
    title = tomxin.getInfo.get_content(info,'href.+?>','<')
    url = tomxin.getInfo.get_content(info,'href="','"')
    i=0
    for u in url[:]:
        r_city="青海"
        r_school="青海大学"
        r_title=title[i]
        r_trait = "QHU" + u[:-4]#这里要自己写提取规则
        r_url = "http://jyw.qhu.edu.cn/jyxx/tzgg_jyxx/zpxx/" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", ' <div class="article">', '<div class="footer">')
        print(r_title + "\n" + r_url)

