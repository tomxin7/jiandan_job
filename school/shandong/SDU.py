
import tomxin.getInfo

def getSDU():
#山东大学
# if __name__ == '__main__':
    url = "http://career.job.sdu.edu.cn/eweb/jygl/index.so?modcode=null&subsyscode=zpfw&type=ssoSearchZxzp&xxlb=5100"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'点击量','id="fenye')
    title = tomxin.getInfo.get_content(info,'omit.+?>','<')
    url = tomxin.getInfo.get_content(info,"omit.+?viewZpxx.+?'","', 'jygl_zpxxck")
    i=0
    for u in url[:]:
        r_city="山东"
        r_school="山东大学"
        r_title=title[i]
        r_trait = "SDU" + u#这里要自己写提取规则
        r_url = "http://career.job.sdu.edu.cn/eweb/jygl/index.so?modcode=jygl_zpxxck&subsyscode=zpfw&rklx=jyw&lmxhV=0402&type=ssoZxzpView&id=" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", 'tdnr.+?>', '<table>')
        print(r_title + "\n" + r_url)

