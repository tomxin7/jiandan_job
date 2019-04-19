
import tomxin.getInfo

def getSHZU():
#石河子大学
# if __name__ == '__main__':
    url = "http://scc.shzu.edu.cn/7640/list.htm"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'wp_article_list','wp_paging_w6')
    title = tomxin.getInfo.get_content(info,"title='","'")
    url = tomxin.getInfo.get_content(info,"href='","'")
    i=0
    for u in url[:10]:
        r_city="新疆"
        r_school="石河子大学"
        r_title=title[i]
        r_trait = "SHZU" + u[-21:-9]#这里要自己写提取规则
        r_url = "http://scc.shzu.edu.cn" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", '<div class="entry">', '<div class="clear">')
        print(r_title + "\n" + r_url)

