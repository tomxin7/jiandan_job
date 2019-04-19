
import tomxin.getInfo

def getXIDIAN():
#西安电子科技大学
# if __name__ == '__main__':
    url = "http://job.xidian.edu.cn/index.html"#高校就业网的网址
    html = tomxin.getInfo.get_source_head(url)
    info = tomxin.getInfo.get_info(html,'id="tab5"','id="tab6">')
    # print(info)#去掉头尾，只要列表内容
    title = tomxin.getInfo.get_content(info,'jobs.+?>','<')
    url = tomxin.getInfo.get_content(info,'jobs','">')
    i=0
    for u in url[:]:
        r_city="陕西"
        r_school="西安电子科技大学"
        r_title=title[i]
        r_trait = "XIDIAN" + u[-10:-5]#这里要自己写提取规则
        r_url = "http://job.xidian.edu.cn/html/zpxx/jobs" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content_head(r_url, '</table>', '<div class="aWeixin">')
        print(r_title + "\n" + r_url)

