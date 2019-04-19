
import tomxin.getInfo

#def getXJTU():
#西安交通大学
if __name__ == '__main__':
    url = "http://job.xjtu.edu.cn/jobindexl.do"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,' class="jsnr">','id="tab2"')
    title = tomxin.getInfo.get_content(info,'title="','"')
    url = tomxin.getInfo.get_content(info,'href="','".+?title')
    i=0
    for u in url[:1]:
        r_city="陕西"
        r_school="西安交通大学"
        r_title=title[i]
        r_trait = "XJTU" + u[-18:]#这里要自己写提取规则
        r_url = "http://job.xjtu.edu.cn" + u
        print(r_title)
        print(r_trait)
        print(r_url)
        i += 1
    #     r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", 'strat', 'end')
    #     print(r_content)#这里获得详情页的内容
    #     print(r_title + "\n" + r_url)

