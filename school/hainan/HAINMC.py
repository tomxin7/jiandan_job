
import tomxin.getInfo

def getHAINMC():
#海南医学院
# if __name__ == '__main__':
    url = "http://210.37.79.115:818/#"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"gbk")
    info = tomxin.getInfo.get_info(html,'<!-- content_23_2 start -->.+?c2_list">','c2_list_b')
    title = tomxin.getInfo.get_content(info,'target.+?>','<')
    url = tomxin.getInfo.get_content(info,'href="','"')
    i=0
    for u in url[:]:
        r_city="海南"
        r_school="海南医学院"
        r_title=title[i]
        r_trait = "HAINMC" + u[-32:]#这里要自己写提取规则
        r_url =  u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", '<div id="main">', '<div style="clear:both;"></div>')
        print(r_title + "\n" + r_url)

