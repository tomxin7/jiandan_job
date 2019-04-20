from urllib import request
import urllib
import re
import socket
import time
import ssl
import json
ssl._create_default_https_context = ssl._create_unverified_context
def get_source(url,encoding):
    timeout = 50#这里是设置超时时间
    socket.setdefaulttimeout(timeout)
    response = request.urlopen(url)
    return response.read().decode(encoding)

#会发送浏览器信息
def get_source_head(url):
    timeout = 10  # 这里是设置超时时间
    socket.setdefaulttimeout(timeout)
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"    })
    oper = urllib.request.urlopen(req)
    data = oper.read().decode("utf-8")
    return data

def get_info(info,reStart,reEnd):
    regex = r'' + reStart + '(.*?)' + reEnd
    pat=re.compile(regex,re.S)
    info=re.findall(pat,info)
    return info[0]

def get_content(info,reStart,reEnd):
    regex = r''+reStart+'(.*?)'+reEnd
    pat=re.compile(regex,re.S)
    content=re.findall(pat,info)
    return content

def get_url_content(url,encoding,reStart,reEnd):
    html = get_source(url,encoding)
    content=get_content(html, reStart, reEnd)
    return str(content[0])
#会发送浏览器信息
def get_url_content_head(url,reStart,reEnd):
    html = get_source_head(url)
    content = get_content(html, reStart, reEnd)
    return str(content[0])

def Function(city,school,function):
    try:
        print(school + "开始爬取")
        function()
        print(school + "爬取成功")
    except Exception as err:
        print("爬取错误：" + str(err))

#休息规则
def sleepTime():
    #获取当前小时
    nowHour=int(time.strftime('%H', time.localtime()))
    if nowHour>=17 and nowHour <=23 :
        print("休息一个小时")
        time.sleep(60*60)
    if nowHour>=0 and nowHour<= 6 :
        print("休息2.5个小时")
        time.sleep(2.5*60*60)
    if nowHour>=7 and nowHour<=16:
        print("休息30分钟")
        time.sleep(30*60)

#适用于需要发送data才能获取内容的网页
import urllib.request
'''
url = 'http://jobsky.csu.edu.cn/Home/PartialArticleList'
values = {
    'pageindex': '1',
    'pagesize': '15',
    'typeid':'4',
    'followingdates':'-1'
}
'''
def get_info_post_data(url,values):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

    data = urllib.parse.urlencode(values)
    # that params output from urlencode is encoded to bytes before it is sent to urlopen as data
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    response = urllib.request.urlopen(req)
    html = response.read()
    return html.decode('utf-8')

#当需要传输的数据是json格式的时候使用
def get_info_post_json_data(url,value):
    # json串数据使用
    value = json.dumps(value).encode(encoding='utf-8')
    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/json"}
    req = request.Request(url=url,data=value,headers=header_dict)
    res = request.urlopen(req)
    res = res.read()
    return (res.decode('utf-8'))