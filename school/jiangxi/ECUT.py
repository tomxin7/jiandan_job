
import tomxin.getInfo

def getECUT():
#东华理工大学
# if __name__ == '__main__':
    url = "http://jyb.ecut.edu.cn/zpxx_4196/list.htm"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'class="wp_article_list"','id="wp_paging_w6"')
    title = tomxin.getInfo.get_content(info,"title='","'")
    url = tomxin.getInfo.get_content(info,"href='","'")
    i=0
    for u in url[:10]:
        r_city="江西"
        r_school="东华理工大学"
        r_title=title[i]
        r_trait = "ECUT" + u[-20:-9]#这里要自己写提取规则
        r_url = "http://jyb.ecut.edu.cn" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", '<div class="entry">', '<div class="wrapper" id="footer"')
        r_content="<div><div><div><div>"+r_content
        print(r_title + "\n" + r_url)

