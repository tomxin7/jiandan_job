
import tomxin.getInfo

def getHUST():
#华中科技大学
# if __name__ == '__main__':
    url = "http://job.hust.edu.cn/searchJob.jspx?type=2&fbsj="#高校就业网的网址
    html = tomxin.getInfo.get_source_head(url)
    info = tomxin.getInfo.get_info(html,'tchrtab_c_tit','pagination')
    title = tomxin.getInfo.get_content(info,'title="','"')
    url = tomxin.getInfo.get_content(info,'target.+?招聘信息.+?href="','"')
    i=0
    for u in url[0:10]:
        r_city="湖北"
        r_school="华中科技大学"
        r_title=title[i]
        r_trait = "HUST" + u[-10:-4]#这里要自己写提取规则
        r_url = "http://job.hust.edu.cn" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content_head(r_url, 'class="txt">', '</div>')
        print(r_title + "\n" + r_url)

