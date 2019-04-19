
import tomxin.getInfo

def getHNU():
#湖南大学
# if __name__ == '__main__':
    url = "https://hnu.bysjy.com.cn/module/getonlines?start_page=1&keyword=&recruit_type=%E6%AD%A3%E5%BC%8F%E6%8B%9B%E8%81%98&count=15&start=1&_=1538988002013"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    title = tomxin.getInfo.get_content(html,'title":"','","')
    url = tomxin.getInfo.get_content(html,'recruitment_id":"','"')
    i=0
    for u in url[:]:
        r_city="湖南"
        r_school="湖南大学"
        r_title=title[i]
        r_trait = "HNU" + u#这里要自己写提取规则
        r_url = "https://hnu.bysjy.com.cn/detail/online?id=" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", '<div class="details-content">', '<a href="javascript:;"')
        print(r_title + "\n" + r_url)

