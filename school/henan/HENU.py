
import tomxin.getInfo

def getHENU():
#河南大学
# if __name__ == '__main__':
    url = "http://job.henu.edu.cn/index.php/Zhaopin/zhaopinList?type=quanzhi"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'class="ul1">','class="ul2"')
    title = tomxin.getInfo.get_content(info,'【.+?</span>','</p>')
    url = tomxin.getInfo.get_content(info,'href="','"')
    i=0
    for u in url[:]:
        r_city="河南"
        r_school="河南大学"
        r_title=title[i].strip()
        r_trait = "HNU" + u[-18:-13]#这里要自己写提取规则
        r_url = "http://job.henu.edu.cn" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", 'class="yin".+?>', '<div class="niuLan">')
        print(r_title + "\n" + r_url)

