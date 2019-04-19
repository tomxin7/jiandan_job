
import tomxin.getInfo

def getYNNU():
#云南师范大学
# if __name__ == '__main__':
    url = "http://job.ynnu.edu.cn/index.php/Schoolp/News/lists?id=909"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'class="yinRightContains','下一页')
    title = tomxin.getInfo.get_content(info,'reds">','<')
    url = tomxin.getInfo.get_content(info,'href="','"')
    i=0
    for u in url[:11]:
        r_city="云南"
        r_school="云南师范大学"
        r_title=title[i]
        r_trait = "YNNU" + u[-12:-7]#这里要自己写提取规则
        r_url = "http://job.ynnu.edu.cn/" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", 'class="newat on">', '><div style="displa')
        print(r_title + "\n" + r_url)

