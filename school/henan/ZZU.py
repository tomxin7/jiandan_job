
import tomxin.getInfo

import datetime



def getZZU():
#郑州大学
# if __name__ == '__main__':
    today = datetime.date.today()# 获取当前时间,
    url = "http://job.zzu.edu.cn:9009/service/business/college/content/content/getRecruitmentInfoList.xf"#高校就业网的网址
    values = {"channel_code":"ZPXX","rowsNum":"10","countsNum":"100","year":today.year,"month":today.month,"currentPage":"1"}
    info = tomxin.getInfo.get_info_post_data(url,values)
    title = tomxin.getInfo.get_content(info,'cand03":"','"')
    url = tomxin.getInfo.get_content(info,'cand01":',',"')
    i=0
    for u in url[:]:
        r_city="河南"
        r_school="郑州大学"
        r_title=title[i]
        r_trait = "ZZU" + u#这里要自己写提取规则
        r_url = "http://job.zzu.edu.cn/p/page/newsInfo.html?channel_code=ZPXX&cand01=" + u
        i += 1
        c_url="http://job.zzu.edu.cn:9009/service/business/college/content/content/getInfoDetail.xf"
        values = { "cand01": u}
        r_content = tomxin.getInfo.get_info_post_data(c_url, values)
        r_content = tomxin.getInfo.get_content(r_content, 'cand04":"', '","')
        print(r_title + "\n" + r_url)

