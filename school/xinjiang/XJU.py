
import tomxin.getInfo

def getXJU():
#新疆大学
# if __name__ == '__main__':
    url = "http://zsjy.xju.edu.cn/zpxx.htm"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'line127895_0','首页')
    title = tomxin.getInfo.get_content(info,'title="','"')
    url = tomxin.getInfo.get_content(info,'href="','"')
    i=0
    for u in url[:10]:
        r_city="新疆"
        r_school="新疆大学"
        r_title=title[i]
        r_trait = "XJU" + u[-8:-4]#这里要自己写提取规则
        r_url = "http://zsjy.xju.edu.cn/" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", 'form127879a">', '<span>关闭窗口')
        print(r_title + "\n" + r_url)

