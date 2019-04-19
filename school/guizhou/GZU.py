
import tomxin.getInfo

def getGZU():
#贵州大学
# if __name__ == '__main__':
    url = "http://jobs.gzu.edu.cn/gzujobs/client/recruitment/2"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'news_cont newscont1 gray','pagebar')
    title = tomxin.getInfo.get_content(info,'title="','"')
    url = tomxin.getInfo.get_content(info,'href="','"')
    i=0
    for u in url[:7]:
        r_city="贵州"
        r_school="贵州大学"
        r_title=title[i]
        r_trait = "GZU" + u[-5:]#这里要自己写提取规则
        r_url = "http://jobs.gzu.edu.cn/" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", '企业简介</th>', '<th>招聘地点</th>')
        print(r_title + "\n" + r_url)

