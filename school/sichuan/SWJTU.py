
import tomxin.getInfo

def getSWJTU():
#西南交通大学
# if __name__ == '__main__':
    url = "http://106.3.35.197/eweb/jygl/zpfw.so?modcode=jygl_zpxxck&subsyscode=zpfw&type=searchZpxx&xxlb=5100"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'z_newsl','z_pages')
    title = tomxin.getInfo.get_content(info,"viewZpxx.+?>","</a>")
    url = tomxin.getInfo.get_content(info,"viewZpxx.+?'","'")
    i=0
    for u in url[:7]:
        r_city="四川"
        r_school="西南交通大学"
        r_title=title[i]
        r_trait = "SWJTU" + u#这里要自己写提取规则
        r_url = "http://106.3.35.197/eweb/jygl/zpfw.so?modcode=jygl_zpfwzprd&subsyscode=zpfw&type=viewZpxx&id=" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", 'z_content">', '<script type="text/javascript">')
        print(r_title + "\n" + r_url)

