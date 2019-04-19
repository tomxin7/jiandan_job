
import tomxin.getInfo

def getAHU():
#安徽大学
# if __name__ == '__main__':
    url = "http://www.job.ahu.edu.cn/detach.portal?pageIndex=1&.pmn=view&groupid=22&action=bulletinsMoreView&pageSize=&.ia=false&.pen=pe2"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'id="blpe2"','pagination')
    title = tomxin.getInfo.get_content(info,'title.+?>','<')
    url = tomxin.getInfo.get_content(info,'title.+?href="','"')
    i=0
    for u in url[:]:
        r_city="安徽"
        r_school="安徽大学"
        r_title=title[i]
        r_trait = "AHU" + u[-36:]#这里要自己写提取规则
        r_url = "http://www.job.ahu.edu.cn/" + u.replace("amp;","")
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", 'fontBig.+?</div>', '<script')
        print(r_title + "\n" + r_url)


