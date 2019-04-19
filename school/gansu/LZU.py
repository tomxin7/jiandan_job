
import tomxin.getInfo

def getLZU():
#兰州大学
# if __name__ == '__main__':
    url = "http://job.lzu.edu.cn/htmlfile/article/list/28/list_1.shtml"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'seg2_list','seg2_title')
    title = tomxin.getInfo.get_content(info,'href.+?>','<')
    url = tomxin.getInfo.get_content(info,'href="','"')
    i=0
    for u in url[:6]:
        r_city="甘肃"
        r_school="兰州大学"
        r_title=title[i]
        r_trait = "LZU" + u[-11:-6]#这里要自己写提取规则
        r_url = "http://job.lzu.edu.cn/" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", ' class="seg3_content">', '<script type="text/javascript">')
        print(r_title + "\n" + r_url)

