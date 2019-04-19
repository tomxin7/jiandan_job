
import tomxin.getInfo

def getCSU():
#中南大学
#if __name__ == '__main__':
    url = "http://jobsky.csu.edu.cn/Home/PartialArticleList"#高校就业网的网址
    values = {
        'pageindex': '1',
        'pagesize': '15',
        'typeid': '4',
        'followingdates': '-1'
    }
    info = tomxin.getInfo.get_info_post_data(url,values)
    title = tomxin.getInfo.get_content(info,'_blank">','</a>')
    url = tomxin.getInfo.get_content(info,'href="','"')
    i=0
    for u in url[:]:
        r_city="湖南"
        r_school="中南大学"
        r_title=title[i]
        r_trait = "CSU" + u[-4:]#这里要自己写提取规则
        r_url = "http://jobsky.csu.edu.cn" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", 'id="companyInfo".+?</table>', '<div id="contact">')
        print(r_title + "\n" + r_url)

