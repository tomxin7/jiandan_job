
import tomxin.getInfo
def getFZU():
# 福州大学
# if __name__ == '__main__':
    url = "http://www.fjrclh.com/newslistnew.asp?classid=16&Nclassid=42"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'colMR','下一页')
    title = tomxin.getInfo.get_content(info,"_blank'>","</a>")
    url = tomxin.getInfo.get_content(info,"href='","'")
    i=0
    for u in url:
        r_city="福建"
        r_school="福州大学"
        r_title=title[i]
        r_trait = "FZU" + u[-5:]#这里要自己写提取规则
        r_url = "http://www.fjrclh.com/" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", 'news-entry">', '<div id="qrcode"')
        print(r_title + "\n" + r_url)


