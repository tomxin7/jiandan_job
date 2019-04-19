
import tomxin.getInfo

def getNUN():
#北方民族大学
# if __name__ == '__main__':
    url = "http://jyc.nun.edu.cn/eweb/jygl/zpfw.so?modcode=jygl_scfwzpxx&subsyscode=zpfw&type=searchZprd&sysType=TPZPFW&zpxxType=new"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'z_newsl','z_pages')
    title = tomxin.getInfo.get_content(info,'viewZpxx.+?>','</a>')
    url = tomxin.getInfo.get_content(info,"viewZpxx.+?'","'")
    i=0
    for u in url[:5]:
        r_city="宁夏"
        r_school="北方民族大学"
        r_title=title[i]
        r_trait = "NUN" + u#这里要自己写提取规则
        r_url = "http://jyc.nun.edu.cn/eweb/jygl/zpfw.so?modcode=jygl_scfwzpxx&subsyscode=zpfw&type=viewZpxx&id=" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", '<div class="z_content">', '<script type="text/javascript')
        print(r_title + "\n" + r_url)

