
import tomxin.getInfo

def getSCNU():
#华南师范大学
#if __name__ == '__main__':
    url = "http://career.scnu.edu.cn/Recruitment/index"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'listtitle','下一页')
    title = tomxin.getInfo.get_content(info,'alt.+?</td>.+?html">','</a>')
    url = tomxin.getInfo.get_content(info,'alt.+?href="','"')
    i=0
    for u in url[:15]:
        r_city="广东"
        r_school="华南师范大学"
        r_title=title[i]
        r_trait = "SCNU" + u[-10:-5]#这里要自己写提取规则
        r_url = u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", 'articlecontent">-->', '编辑')
        print(r_title + "\n" + r_url)

