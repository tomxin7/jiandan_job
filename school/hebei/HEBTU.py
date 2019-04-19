
import tomxin.getInfo

def getHEBTU():
#河北师范大学
# if __name__ == '__main__':
    url = "http://hebtu.jiuyeb.cn/index.php/Schoolh/News/news/xz/1/zxzp/1/setype/1"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'其他院校','下一页')
    title = tomxin.getInfo.get_content(info,'需求信息.+?>','<')
    url = tomxin.getInfo.get_content(info,'href="','"')
    i=0
    for u in url[:10]:
        r_city="河北"
        r_school="河北师范大学"
        r_title=title[i]
        r_trait = "HEBTU" + u[-12:-7]#这里要自己写提取规则
        r_url = "http://hebtu.jiuyeb.cn" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", 'liulanliang.png.+?</p>', '<!-- <span>岗位职责')
        print(r_title + "\n" + r_url)

