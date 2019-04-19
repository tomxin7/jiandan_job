
import tomxin.getInfo

def getNWPU():
#西北工业大学
# if __name__ == '__main__':
    url = "http://job.nwpu.edu.cn/jobInfoList.do?page=1&order=infoPlus.submitTime&sort=desc&filter=%7bstatus%3a1%2cworkType%3a0%7d&ext=0"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'<!-- END PAGE TITLE & BREADCRUMB-->','pagination ')
    title = tomxin.getInfo.get_content(info,'title.+?>','<')
    url = tomxin.getInfo.get_content(info,'<h3>.+?href="','".+?title')
    i=0
    for u in url[:]:
        r_city="陕西"
        r_school="西北工业大学"
        r_title=title[i].strip()
        r_trait = "NWPU" + u[-5:]#这里要自己写提取规则
        r_url = "http://job.nwpu.edu.cn" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", '职位描述</h4>', '<hr>')
        print(r_title + "\n" + r_url)
