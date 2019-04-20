
import tomxin.getInfo


def getHIT():
#大学名称
# if __name__ == '__main__':
    url = "http://job.hit.edu.cn/info/getSxxxData"#高校就业网的网址
    values = {"bkxlyq":"0","bsxlyq":"0","dwhy":"","dwmc":"","dwxz":"","gjc":"","gzdd":"","gzddsheng":"","page":"1","pageSize":"12","skip":"0","ssxlyq":"0","take":"12"}
    info = tomxin.getInfo.get_info_post_json_data(url,values)
    title = tomxin.getInfo.get_content(info,'DWMC":"','"')
    url = tomxin.getInfo.get_content(info,'ZPXXID":"','"')
    i=0
    for u in url[:10]:
        r_city="黑龙江"
        r_school="哈尔滨工业大学"
        r_title=title[i]
        r_trait = "HIT" + u#这里要自己写提取规则
        r_url = "http://job.hit.edu.cn/info?dj=Mw--"
        i += 1
        url = "http://job.hit.edu.cn/index/getZpxxXqAndSetLlcsById"  # 高校就业网的网址
        values = {"zpxxid":u}
        r_content = tomxin.getInfo.get_info_post_json_data(url, values)
        r_content = tomxin.getInfo.get_content(r_content,'ZWYQ":"','",.+?ZPXXID')
        r_content = r_content[0].replace('\\', '')
        print(r_title + "\n" + r_url)

