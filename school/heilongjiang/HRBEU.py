
import tomxin.getInfo

def getHRBEU():
#哈尔滨工程大学
# if __name__ == '__main__':
    url = "http://job.hrbeu.edu.cn/1708/list.htm"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'wp_article_list','id="wp_paging_w6"')
    title = tomxin.getInfo.get_content(info,"title='","'")
    url = tomxin.getInfo.get_content(info,"href='","'")
    i=0
    for u in url[:1]:
        r_city="黑龙江"
        r_school="哈尔滨工程大学"
        r_title=title[i]
        r_trait = "HRBEU" + u[-21:-9]#这里要自己写提取规则
        r_url = "http://job.hrbeu.edu.cn" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", 'entry">', '<div class="foot">')
        print(r_title + "\n" + r_url)

