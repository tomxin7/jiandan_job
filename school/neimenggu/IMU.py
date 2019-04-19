
import tomxin.getInfo

def getIMU():
#内蒙古大学
# if __name__ == '__main__':
    url = "http://job.imu.edu.cn/JobInfo/List/24"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'所在位置.+?首页','上一页')
    title = tomxin.getInfo.get_content(info,'target.+?>','<')
    url = tomxin.getInfo.get_content(info,'href="','"')
    i=0
    for u in url[:6]:
        r_city="内蒙古"
        r_school="内蒙古大学"
        r_title=title[i].strip()
        r_trait = "IMU" + u[-4:]#这里要自己写提取规则
        r_url = "http://job.imu.edu.cn" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", '关闭.+?</table>', ' <td height="100')
        print(r_title + "\n" + r_url)

