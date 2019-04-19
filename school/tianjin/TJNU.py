
import tomxin.getInfo

def getTJNU():
#天津师范大学
#if __name__ == '__main__':
    url = "http://jyzd.tjnu.edu.cn/index/zpxx.htm"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'winstyle49562','首页')
    title = tomxin.getInfo.get_content(info,'title="','"')
    url = tomxin.getInfo.get_content(info,'href="..','"')
    i=0
    for u in url[:]:
        r_city="天津"
        r_school="天津师范大学"
        r_title=title[i]
        r_trait = "TJNU" + u[-9:-4]#这里要自己写提取规则
        r_url = "http://jyzd.tjnu.edu.cn" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", 'contentstyle49564">', ' <tr><td class="pagestyle49564')
        print(r_title + "\n" + r_url)

