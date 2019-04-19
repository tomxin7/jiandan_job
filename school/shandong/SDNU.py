
import tomxin.getInfo

#def getSDNU():
#山东师范大学
if __name__ == '__main__':
    url = "http://www.career.sdnu.edu.cn/wlzpCompany.aspx"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'class="infoBox ','class="pagination">')
    title = tomxin.getInfo.get_content(info,'span1.+?blank">','<')
    url = tomxin.getInfo.get_content(info,'span1.+?href="','"')
    i=0
    for u in url[:10]:
        r_city="山东"
        r_school="山东师范大学"
        r_title=title[i]
        r_trait = "SDNU" + u[-9:-5]#这里要自己写提取规则
        r_url = "http://www.career.sdnu.edu.cn/" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", '<!----------校园招聘----------->', '<script>')
        print(r_title + "\n" + r_url)

