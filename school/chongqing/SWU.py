
import tomxin.getInfo

def getSWU():
#西南大学
# if __name__ == '__main__':
    url = "http://bkjyw.swu.edu.cn/s/bkjy/wlzp/index_2.html"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'cnt_lst','pageset')
    # print(info)#去掉头尾，只要列表内容
    title = tomxin.getInfo.get_content(info,'blank>','</a>')
    url = tomxin.getInfo.get_content(info,'href="','"')
    i=0
    for u in url[:]:
        r_city="重庆"
        r_school="西南大学"
        r_title=title[i]
        r_trait = "SWU" + u[-12:-5]#这里要自己写提取规则
        r_url = "http://bkjyw.swu.edu.cn/" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", 'ct-b-top"></div>', '<div class="ct-b-btn">')
        print(r_title + "\n" + r_url)

