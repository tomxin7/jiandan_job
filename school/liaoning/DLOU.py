
import tomxin.getInfo

def getDLOU():
#大学名称
# if __name__ == '__main__':
    url = "http://job.dlou.edu.cn/3717/list.psp"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'simpleList"> ','wp_paging_w3"> ')
    title = tomxin.getInfo.get_content(info,"title='","'")
    url = tomxin.getInfo.get_content(info,"href='","'")
    i=0
    for u in url[:]:
        r_city="辽宁"
        r_school="大连海洋大学"
        r_title=title[i]
        r_trait = "DLOU" + u[-20:-9]#这里要自己写提取规则
        r_url = "http://job.dlou.edu.cn" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", '面板2"> ', '</table>')
        print(r_title + "\n" + r_url)

