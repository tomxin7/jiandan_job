
import tomxin.getInfo

def getOUC():
#中国海洋大学
# if __name__ == '__main__':
    url = "http://career.ouc.edu.cn/zftal-web/zfjy!ykfw/zpztgl_cxZpztList.html?doType=query"#高校就业网的网址
    info = tomxin.getInfo.get_source(url,"utf-8")
    title = tomxin.getInfo.get_content(info,'dwmc":"','"')
    url = tomxin.getInfo.get_content(info,'id":"','"')
    i=0
    for u in url[:]:
        r_city="山东"
        r_school="中国海洋大学"
        r_title=title[i]
        r_trait = "OUC" + u#这里要自己写提取规则
        r_url = "http://career.ouc.edu.cn/zftal-web/zfjy!ykfw/zpztgl_cxWzZpxxNry.html?id=" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", '<!--主体-->', '<div class="bot_jyfw">')
        print(r_title + "\n" + r_url)

