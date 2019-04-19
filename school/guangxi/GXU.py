
import tomxin.getInfo

def getGXU():
#广西大学
#if __name__ == '__main__':
    url = "http://job.gxu.edu.cn/job_dwxx/list.asp?page=MQ=="#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"gb2312")
    info = tomxin.getInfo.get_info(html,'标 题',' </table>')
    # print(info)#去掉头尾，只要列表内容
    title = tomxin.getInfo.get_content(info,'</b>&nbsp;','</a>')
    url = tomxin.getInfo.get_content(info,'href="','"')
    i=0
    for u in url[:10]:
        r_city="广西"
        r_school="广西大学"
        r_title=title[i]
        r_trait = "GXU" + u[-8:-1]#这里要自己写提取规则
        r_url = "http://job.gxu.edu.cn/job_dwxx/" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "gb2312", '单位名称</td>', ' </tr>')
        r_content = "单位名称："+"<br>"+r_content
        r_content = r_content+"<br>"+"单位地址："+"<br>"+tomxin.getInfo.get_url_content(r_url, "gb2312", '单位地址</td>', ' </tr>')
        r_content = r_content+"<br>"+"联系电话："+"<br>"+tomxin.getInfo.get_url_content(r_url, "gb2312", '联系电话</td>', ' </tr>')
        r_content = r_content+"<br>"+tomxin.getInfo.get_url_content(r_url, "gb2312", 'LINE-HEIGHT.+?>', ' </tr>')
    #     print(r_content)#这里获得详情页的内容
        print(r_title + "\n" + r_url)

