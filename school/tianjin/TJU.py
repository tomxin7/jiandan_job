
import tomxin.getInfo



def getTJU():
#天津大学
#if __name__ == '__main__':
    url = "http://job.api.twtstudio.com/api/recruit/index/1/1"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    # print(html)#获取网页源码，如果报错，可能是上面编码的问题
    info = tomxin.getInfo.get_info(html,'info',']')
    title = tomxin.getInfo.get_content(info,'title":"','",')
    url = tomxin.getInfo.get_content(info,'id":"','",')
    i=0
    for u in url[:]:
        r_city="天津"
        r_school="天津大学"
        r_title=title[i].encode('utf-8').decode('unicode_escape')#转换为Unicode
        r_trait = "TJU" + u#这里要自己写提取规则
        r_url = "http://job.api.twtstudio.com/api/recruit/detail/1/" + u
        # print(r_title)
        # print(r_trait)
        # print(r_url)
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", 'content":"', '",')
        r_content = r_content.encode('utf-8').decode('unicode_escape')
        r_content = r_content.encode('utf-8').decode('unicode_escape')#这里需要两次转换
        r_content=r_content.replace('\\','')

        print(r_title + "\n" + r_url)

