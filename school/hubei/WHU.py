
import tomxin.getInfo

def getWHU():
#武汉大学
#if __name__ == '__main__':
    url = "http://www.xsjy.whu.edu.cn/zftal-web/zfjy!wzxx!whdx10486/dwzpxx_cxWzDwzpxxEX.html?zpdxType=1#iframe_139754366237057873"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'id="wzxssl"','</body>')
    title = tomxin.getInfo.get_content(info,'title="','"')
    url = tomxin.getInfo.get_content(info,"href='","'")
    i=0
    for u in url:
        r_city="湖北"
        r_school="武汉大学"
        r_title=title[i]
        r_trait = "WHU" + u[-9:]#这里要自己写提取规则
        r_url = "http://www.xsjy.whu.edu.cn" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", 'class="position_infor02">', '<!--联系方式-->')
    #     print(r_content)#这里获得详情页的内容
        print(r_title + "\n" + r_url)

