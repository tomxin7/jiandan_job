
import tomxin.getInfo

def getNWU():
#西北大学
# if __name__ == '__main__':
    url = "http://jiuye.nwu.edu.cn/website/news_list.aspx?category_id=111"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'nei_content_right_txt_list">',' class="flickr">')
    title = tomxin.getInfo.get_content(info,'href.+?>','<')
    url = tomxin.getInfo.get_content(info,"href='","'")
    i=0
    for u in url[:]:
        r_city="陕西"
        r_school="西北大学"
        r_title=title[i]
        r_trait = "NWU" + u[-4:]#这里要自己写提取规则
        r_url = "http://jiuye.nwu.edu.cn/website/" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", 'entry.+?>', 'class="foot">')
        print(r_title + "\n" + r_url)

