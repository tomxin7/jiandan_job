
import tomxin.getInfo

def getCQU():
#重庆大学
# if __name__ == '__main__':
    url = "http://www.job.cqu.edu.cn/dwr/call/plaincall/portalAjax.getNewsXml.dwr"#高校就业网的网址
    values = {
        'callCount': '1',
        'page': '/type/00001010207.html',
        'httpSessionId': 'BA6242B552A3A977E38B48E253A236A4',
        'scriptSessionId': '10FB69B2A9C5DB75813C86F285112D3A582',
        'c0-scriptName': 'portalAjax',
        'c0-methodName': 'getNewsXml',
        'c0-id': '0',
        'c0-param0': 'string:0000101',
        'c0-param1': 'string:00001010207',
        'c0-param2': 'string:news_',
        'c0-param3': 'number:15',
        'c0-param4': 'number:1',
        'c0-param5': 'null:null',
        'c0-param6': 'null:null',
        'batchId': '0'
    }

    html = tomxin.getInfo.get_info_post_data(url,values)
    info = html.encode('utf-8').decode('unicode_escape')#获取网页源码，如果报错，可能是上面编码的问题
    title = tomxin.getInfo.get_content(info,'<title.+?ATA',']')
    url = tomxin.getInfo.get_content(info,'<link.+?ATA',']')
    i=0
    for u in url[:8]:
        r_city="重庆"
        r_school="重庆大学"
        r_title=title[i][1:]
        r_trait = "CQU" + u[-23:-5]#这里要自己写提取规则
        r_url = u[1:]
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "gbk", 'yyxwym.+?script>', '<div class="bar">')
        print(r_title + "\n" + r_url)

