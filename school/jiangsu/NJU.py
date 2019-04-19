
import tomxin.getInfo

#def getNJU():
#南京大学
if __name__ == '__main__':
    url = "http://job.nju.edu.cn/login/nju/home.jsp?type=xyzp&pageNow=1"#高校就业网的网址
    values = {
        'type': 'xyzp',
        'pageNow': '1'
    }
    html = tomxin.getInfo.get_info_post_data(url,values)
    info = tomxin.getInfo.get_info(html,'<div class="article-lists">','established')
    title = tomxin.getInfo.get_content(info,'_blank">','<')
    url = tomxin.getInfo.get_content(info,'href="','"')
    i=0
    for u in url[:]:
        r_city="江苏"
        r_school="南京大学"
        r_title=title[i].strip()
        r_trait = "NJU" + u[-52:]#这里要自己写提取规则
        r_url = "http://job.nju.edu.cn/login/nju/" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", ' <div class="artilce-content">', '<br/>')
        print(r_title + "\n" + r_url)

