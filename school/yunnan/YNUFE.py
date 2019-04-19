
import tomxin.getInfo
import time

#def getYNUFE():
#云南财经大学
if __name__ == '__main__':
    url = "http://jy.ynufe.edu.cn/module/getonlines?start=0&count=16&keyword=&professionals=&recruit_type="#高校就业网的网址
    info = tomxin.getInfo.get_source(url,"utf-8")
    title = tomxin.getInfo.get_content(info,'title":"','"')
    url = tomxin.getInfo.get_content(info,'recruitment_id":"','"')
    i=0
    for u in url[:]:
        r_city="云南"
        r_school="云南财经大学"
        r_title=title[i]
        r_trait = "YNUFE" + u#这里要自己写提取规则
        r_url = "http://jy.ynufe.edu.cn/detail/online?id=" + u
        print(r_title)
        print(r_trait)
        print(r_url)
        i += 1
        c_url="http://jy.ynufe.edu.cn/detail/getonlinedetail?online_id="+u
        time.sleep(5)
        r_content = tomxin.getInfo.get_url_content(c_url, "utf-8", 'content":"', '",')
        print(r_content)#这里获得详情页的内容
        print(r_title + "\n" + r_url)

