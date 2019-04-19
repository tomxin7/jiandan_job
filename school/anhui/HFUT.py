
import tomxin.getInfo

def getHFUT():
#合肥工业大学
# if __name__ == '__main__':
    url = "http://gdjy.hfut.edu.cn/products/list/4.html"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'</thead>','</tbody>')
    title = tomxin.getInfo.get_content(info,'href.+?>','<')
    url = tomxin.getInfo.get_content(info,'href="','"')
    i=0
    for u in url[:11]:
        r_city="安徽"
        r_school="合肥工业大学"
        r_title=title[i]
        r_trait = "HFUT" + u[-9:-5]#这里要自己写提取规则
        r_url = "http://gdjy.hfut.edu.cn" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", '招聘详情.+?div.+?div>', '<div class="row">')
        print(r_title + "\n" + r_url)

