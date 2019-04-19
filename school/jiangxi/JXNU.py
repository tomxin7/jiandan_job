
import tomxin.getInfo

def getJXNU():
#江西师范大学
# if __name__ == '__main__':
    url = "http://jy.jxnu.edu.cn/index.php/Home/Recruitment/recruitment/type/2.html"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    # print(html)#获取网页源码，如果报错，可能是上面编码的问题
    info = tomxin.getInfo.get_info(html,'recruitment表-->',' class="page-container">')
    # print(info)#去掉头尾，只要列表内容
    title = tomxin.getInfo.get_content(info,'html">','</a>.+?class="pull-right"')
    url = tomxin.getInfo.get_content(info,'href="','">')
    i=0
    for u in url:
        r_city="江西"
        r_school="江西师范大学"
        r_title=title[i]
        r_trait = "JXNU" + u[-9:-5]#这里要自己写提取规则
        r_url = "http://jy.jxnu.edu.cn/" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", 'publish-time.+?<br>', '<div class="share" >')
        print(r_title + "\n" + r_url)

