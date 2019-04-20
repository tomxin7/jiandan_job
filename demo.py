
import tomxin.getInfo

''''
快速开发专属你的校招爬虫
'''
#def getUNAME():
#大学名称
if __name__ == '__main__':
    url = ""#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    print(html)#获取网页源码，如果报错，可能是上面编码的问题
    # info = tomxin.getInfo.get_info(html,'start','end')
    # print(info)#去掉头尾，只要列表内容
    # title = tomxin.getInfo.get_content(info,'start','end')
    # url = tomxin.getInfo.get_content(info,'href="','"')
    # i=0
    # for u in url:
    #     print(u)
    #     print(title[i])
    #     i+=1
    # for u in url[:1]:
    #     r_city="省份"
    #     r_school="学校名称"
    #     r_title=title[i]
    #     r_trait = "学校简称" + u[-18:]#这里要自己写提取规则
    #     r_url = "http://www.career.zju.edu.cn/ejob/" + u
    #     print(r_title)
    #     print(r_trait)
    #     print(r_url)
    #     i += 1
    #     r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", 'strat', 'end')
    #     print(r_content)#这里获得详情页的内容
    #

