
import tomxin.getInfo

def getHEBUT():
#河北工业大学
# if __name__ == '__main__':
    url = "http://ugs.hebut.edu.cn/portal/home/employment-website.html?baseCommonImageTextVo.menuId=10&type=5100320000000042"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    # print(html)#获取网页源码，如果报错，可能是上面编码的问题
    info = tomxin.getInfo.get_info(html,'sub_title','pagination')
    # print(info)#去掉头尾，只要列表内容
    title = tomxin.getInfo.get_content(info,'target="_blank">','<')
    url = tomxin.getInfo.get_content(info,'href="','"')
    i=0
    for u in url[:]:
        r_city="天津"
        r_school="河北工业大学"
        r_title=title[i].strip()
        r_trait = "HEBUT" + u[-16:-11]#这里要自己写提取规则
        r_url = "http://ugs.hebut.edu.cn" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", 'lass="article">', '<div class="footer">')
        # print(r_content)#这里获得详情页的内容
        print(r_title + "\n" + r_url)

