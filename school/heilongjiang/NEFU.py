
import tomxin.getInfo

def getNEFU():
#东北林业大学
# if __name__ == '__main__':
    url = "http://job.nefu.edu.cn/catalog/view/2"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'招聘信息]','条记录')
    # print(info)#去掉头尾，只要列表内容
    title = tomxin.getInfo.get_content(info,'<span>','<')
    url = tomxin.getInfo.get_content(info,'detail','"')
    i=0
    for u in url[:]:
        r_city="黑龙江"
        r_school="东北林业大学"
        r_title=title[i]
        r_trait = "NEFU" + u[-5:]#这里要自己写提取规则
        r_url = "http://job.nefu.edu.cn/detail" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", 'summary">', '上一篇')
        print(r_title + "\n" + r_url)

