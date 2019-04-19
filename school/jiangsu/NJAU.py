
import tomxin.getInfo

def getNJAU():
#南京农业大学
# if __name__ == '__main__':
    url = "http://njau.91job.gov.cn/campus/index?city="#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'infoBox','ctl')
    title = tomxin.getInfo.get_content(info,'_blank">','<')
    url = tomxin.getInfo.get_content(info,'href="','"')
    i=0
    for u in url[:]:
        r_city="江苏"
        r_school="南京农业大学"
        r_title=title[i]
        r_trait = "SEU" + u[-6:]#这里要自己写提取规则
        r_url = "http://njau.91job.gov.cn" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", '</dl>.+?/div>', '<scrip')
        print(r_title + "\n" + r_url)

