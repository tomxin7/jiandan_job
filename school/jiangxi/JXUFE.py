
import tomxin.getInfo

def getJXUFE():
#江西财经大学
#if __name__ == '__main__':
    url = "http://career.jxufe.edu.cn/module/getonlines?start_page=1&keyword=&recruit_type=&count=15&start=1&_=1516960852444"#高校就业网的网址
    info = tomxin.getInfo.get_source(url,"utf-8")
    title = tomxin.getInfo.get_content(info,'title":"','"')
    url = tomxin.getInfo.get_content(info,'recruitment_id":"','"')
    i=0
    for u in url[:10]:
        r_city="江西"
        r_school="江西财经大学"
        r_title=title[i]
        r_trait = "JXUFE" + u#这里要自己写提取规则
        r_url = "http://career.jxufe.edu.cn/detail/online?id=" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", 'class="details-content">', '<div class="pub-code">')
        # print(r_content)#这里获得详情页的内容
        print(r_title + "\n" + r_url)

