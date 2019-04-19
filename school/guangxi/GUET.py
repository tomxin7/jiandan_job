
import tomxin.getInfo

def getGUET():
#桂林电子科技大学
#if __name__ == '__main__':
    url = "http://job.guet.edu.cn/Home/ArticleList?label=16"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'访问人次','disabled')
    # print(info)#去掉头尾，只要列表内容
    title = tomxin.getInfo.get_content(info,'title="','">')
    url = tomxin.getInfo.get_content(info,'href="','"')
    i=0
    for u in url[:10]:
        r_city="广西"
        r_school="桂林电子科技大学"
        r_title=title[i]
        r_trait = "GUET" + u[-12:]#这里要自己写提取规则
        r_url = "http://job.guet.edu.cn" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", 'font02">', '</tr>')
        print(r_title + "\n" + r_url)

