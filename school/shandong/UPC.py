
import tomxin.getInfo

def getUPC():
#中国石油大学
# if __name__ == '__main__':
    url = "http://career.upc.edu.cn/index.php/index/index/shownewsfreshlist/classID/10/np/1?_=1522243898465"#高校就业网的网址
    info = tomxin.getInfo.get_source(url,"utf-8")
    title = tomxin.getInfo.get_content(info,'title="','"')
    url = tomxin.getInfo.get_content(info,'href="','"')
    i=0

    for u in url[:13]:
        r_city="山东"
        r_school="中国石油大学"
        r_title=title[i]
        r_trait = "UPC" + u[-9:-5]#这里要自己写提取规则
        r_url = "http://career.upc.edu.cn" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", '点击量.+?</div>', '<!--引入footer-->')
        print(r_title + "\n" + r_url)

