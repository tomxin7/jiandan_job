
import tomxin.getInfo

def getHBU():
#大学名称
# if __name__ == '__main__':
    url = "http://job.hbu.cn/index.php/gggs.html"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'textlist1','pageinfo')
    title = tomxin.getInfo.get_content(info,'title="','">')
    url = tomxin.getInfo.get_content(info,'href="','"')
    i=0
    for u in url[:10]:
        r_city="河北"
        r_school="河北大学"
        r_title=title[i]
        r_trait = "HBU" + u[-9:-5]#这里要自己写提取规则
        r_url = "http://job.hbu.cn" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", 'InfoContent">', '<!-- 频道')
        print(r_title + "\n" + r_url)

