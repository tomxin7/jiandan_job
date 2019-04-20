
import tomxin.getInfo


def getUESTC():
#电子科技大学
# if __name__ == '__main__':
    url = "http://www.jiuye.org/sys/fore.php?op=listRecruit&callback=jQuery18303119128149962722_1522675123427"#高校就业网的网址
    info = tomxin.getInfo.get_source(url,"utf-8")
    title = tomxin.getInfo.get_content(info,'rec_enter_name":"','"')
    url = tomxin.getInfo.get_content(info,'rec_No":"','"')
    i=0
    for u in url[:]:
        r_city="四川"
        r_school="电子科技大学"
        r_title=title[i].encode('utf-8').decode('unicode_escape')
        r_trait = "UESTC" + u#这里要自己写提取规则
        r_url = "http://www.jiuye.org/career/info/Recruitment.html?id=" + u +"&rectype=1"
        i += 1
        values = {
            'rec_id': u,
        }
        r_content = tomxin.getInfo.get_info_post_data("http://www.jiuye.org/sys/fore.php?op=viewRecruit&callback=jQuery183023468175340026032_1522675700552",values)
        r_content=r_content.encode('utf-8').decode('unicode_escape')#这里获得详情页的内容
        r_content = tomxin.getInfo.get_content(r_content, 'rec_content":"', '"')
        r_content = r_content[0].replace('\\', '')
        print(r_title + "\n" + r_url)

