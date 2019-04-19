
import tomxin.getInfo

def getKMUST():
#昆明理工大学
# if __name__ == '__main__':
    url = "http://job.kmust.edu.cn/module/getonlines?start_page=1&keyword=&recruit_type=&count=15&start=1&_=1522680219599"#高校就业网的网址
    info = tomxin.getInfo.get_source(url,"utf-8")
    title = tomxin.getInfo.get_content(info,'company_name":"','"')
    url = tomxin.getInfo.get_content(info,'recruitment_id":"','"')
    i=0
    for u in url[:]:
        r_city="云南"
        r_school="昆明理工大学"
        r_title=title[i]
        r_trait = "KMUST" + u#这里要自己写提取规则
        r_url = "http://job.kmust.edu.cn/detail/online?id=" + u+ "&menu_id=4635"
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", ' <div class="details-content">', '<div class="pub-code">')
        print(r_title + "\n" + r_url)

