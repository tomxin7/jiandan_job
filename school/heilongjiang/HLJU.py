
import tomxin.getInfo

def getHLJU():
#黑龙江大学
# if __name__ == '__main__':
    url = "http://job.hlju.edu.cn/login/list.jsp?secondNav=zpfw&thirdNav=zpxx"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'class="list-list">','text-align:center')
    title = tomxin.getInfo.get_content(info,'href.+?>','<')
    url = tomxin.getInfo.get_content(info,'href="','">')
    i=0
    for u in url[:1]:
        r_city="黑龙江"
        r_school="黑龙江大学"
        r_title=title[i]
        r_trait = "HLJU" + u[-36:]#这里要自己写提取规则
        r_url = u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", 'content-text">', '<a title="分享到新浪')
        print(r_title + "\n" + r_url)

