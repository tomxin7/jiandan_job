<p align="center">
  <img src="http://qiniu.tomxin.cn/blog/20190420/s8waQ0Qn0ybF.png?imageslim" alt="" width=200>
</p>
<p align="center">
  <a href="http://jiandan.live/">
    <img src="https://img.shields.io/badge/build-passing-brightgreen.svg" alt="">
  </a>
  <a href="http://tomxin.cn">
     <img src="https://img.shields.io/badge/author-tomxin7-orange.svg" alt="">
  </a>
</p>


# :black_nib: 简单校招

> 每年春招/秋招，接近千万的应届毕业生拥入人才市场，在这场无硝烟的战役中，如何获取高效精准的获取校招信息至关重要。很多同学喜欢在招聘网站投递简历，但是大部分企业在招聘网站上发布的是社招信息，所以校招简历经常石沉大海。而我们很容易忽视的是学校维护的就业信息网，这些信息大部分都是校园招聘信息，而且时效性和可靠性很高，本项目收录了全国大部分省市的高校，你可以通过简单的编程，例如推送自己想要的校招信息到自己的邮箱，不必24小时盯着这些网站，留给自己更多准备面试的时间。

## 原理说明
> 本项目与各高校无关，感谢负责维护就业信息网的老师、同学们

本项目封装了一些简单的方法，让你可以在不到20行的代码基础上，爬取到各高校就业信息网公开的校招数据<br>
主要会爬取3块内容
- 招聘信息标题
- 招聘信息对应的URL
- 招聘内容

你可以根据自己的需要，对爬取到的数据进行处理<br>
常见的几种玩法
- 比如想找java相关的工作，爬取到对应的企业后，通过python的邮件模块，把对应信息发送到自己邮箱
- 学校的就业信息网界面太老旧了？爬取内容入库，自己写一个美腻的界面，提供给同学们使用（此方案有风险~~）
- 如果你缺少实践的项目，又不喜欢各种商城、管理系统，可以花点时间考虑，然后使用简单校招开发一个好玩又不俗套的项目

## 环境要求
- Python 3.6

## 使用方式
##### 1、安装python3.6以上版本
```
https://www.python.org/getit/
```

##### 2、获取源码
```
牛客网git源
git clone https://git.nowcoder.com/8161485/jiandan_job.git

github源
git clone https://github.com/tomxin7/DouYinFaceTech
```
##### 3、清华大学为例，直接运行main即可得到对应校招信息
```
import school.beijing.TU

if __name__ == '__main__':
    school.beijing.TU.getTU()
    
```
##### 4、修改学校，例如修改为北京大学

beijing：修改为自己的省份/直辖市<br>
TU：修改为对应学校的简称
```
import school.beijing.PKU

if __name__ == '__main__':
    school.beijing.PKU.getPKU()
```

##### 5、新增学校

如果没有自己学校的代码，可以复制demo这个文件，按照格式编写代码即可，针对爬虫不是很熟悉的同学，后期可能会写一个简单的入门教程


## 已收录高校

地区|学校|学校简称|就业信息网
--|:--:|:--:|:--:
北京|清华大学|TU|<a href="http://career.cic.tsinghua.edu.cn/xsglxt/f/jyxt/anony/xxfb">点我跳转</a>
北京|北京大学|PKU|<a href="https://scc.pku.edu.cn/home!recruitList.action?category=1">点我跳转</a>
北京|中国人民大学|RUC|<a href="http://career.ruc.edu.cn/cms/employment/">点我跳转</a>
北京|中国农业大学|CAU|<a href="http://scc.cau.edu.cn/recruitmentinfo.html/?type=zhaopin">点我跳转</a>
上海|复旦大学|FU|<a href="http://www.career.fudan.edu.cn/jsp/recruit_info_list.jsp">点我跳转</a>
上海|上海交通大学|SJTU|<a href="http://www.job.sjtu.edu.cn/eweb/jygl/zpfw.so?modcode=jygl_zpxxck&subsyscode=zpfw&type=searchZpxx&zpxxType=new">点我跳转</a>
天津|天津大学|TJU|<a href="http://job.api.twtstudio.com/api/recruit/index/1/1">点我跳转</a>
天津|天津师范大学|TJNU|<a href="http://jyzd.tjnu.edu.cn/index/zpxx.htm">点我跳转</a>
天津|河北工业大学|HEBUT|<a href="http://ugs.hebut.edu.cn/skip-page/employment-website.html?menuId=10">点我跳转</a>
重庆|重庆大学|CQU|<a href="http://www.job.cqu.edu.cn/type/00001010207.html">点我跳转</a>
重庆|西南大学|SWU|<a href="http://bkjyw.swu.edu.cn/s/bkjy/wlzp/">点我跳转</a>
重庆|重庆师范大学|CQNU|<a href="http://job.cqnu.edu.cn/eweb/jygl/zpfw.so?modcode=jygl_scfwzpxx&subsyscode=zpfw&type=searchZprd&sysType=TPZPFW&zpxxType=new">点我跳转</a>
重庆|西南政法大学|SWUPL|<a href="http://jyb.swupl.edu.cn/jyxx/xwzpxx/index.htm">点我跳转</a>
黑龙江|哈尔滨工业大学|HIT|<a href="http://job.hit.edu.cn/info?dj=Mw--">点我跳转</a>
黑龙江|哈尔滨工程大学|HRBEU|<a href="http://job.hrbeu.edu.cn/1708/list.htm">点我跳转</a>
黑龙江|东北林业大学|NEFU|<a href="http://job.nefu.edu.cn/catalog/view/2">点我跳转</a>
黑龙江|黑龙江大学|HLJU|<a href="http://job.hlju.edu.cn/login/list.jsp?secondNav=zpfw&thirdNav=zpxx">点我跳转</a>
辽宁|大连理工大学|DLUT|<a href="http://202.118.65.2/app/index.html">点我跳转</a>
辽宁|大连海事大学|DLOU|<a href="http://job.dlou.edu.cn/3717/list.psp">点我跳转</a>
吉林|吉林大学|JLU|<a href="http://jdjyw.jlu.edu.cn/index.php?r=front/recruit&type=1">点我跳转</a>
吉林|长春理工大学|CUST|<a href="http://job.cust.edu.cn/root/list.vm?dir=L-aLm-iBmOS_oeaBry_nvZHnu5zmi5vogZjkv6Hmga8&rows=20">点我跳转</a>
河北|河北大学|HBU|<a href="http://job.hbu.cn/index.php/gggs.html">点我跳转</a>
河北|河北师范大学|HEBTU|<a href="http://hebtu.jiuyeb.cn/index.php/Schoolh/News/news/xz/1/zxzp/1/setype/1">点我跳转</a>
河南|郑州大学|ZZU|<a href="http://job.zzu.edu.cn/p/page/jobCalendar.html?channel_code=ZPXX&type=2#/?year=2018&month=3&type=2">点我跳转</a>
河南|河南科技大学|HAUST|<a href="http://zjc.haust.edu.cn/index/jycyzdzx/jysy/zpgg.htm">点我跳转</a>
山东|山东大学|SDU|<a href="http://career.job.sdu.edu.cn/eweb/wfc/app/pager.so?type=goPager&requestPager=pager&pageMethod=first&currentPage=3">点我跳转</a>
山东|中国海洋大学|OUC|<a href="http://career.ouc.edu.cn//type_pr/00001010303.html">点我跳转</a>
山东|中国石油大学(华东)|UPC|<a href="http://career.upc.edu.cn/index.php/index/index/shownewslist/classID/10/newsid/3090/np/3">点我跳转</a>
山东|山东师范大学|SDNU|<a href="http://www.career.sdnu.edu.cn/wlzpCompany.aspx">点我跳转</a>
山西|太原理工大学|TYUT|<a href="http://jiuye.tyut.edu.cn/">点我跳转</a>
陕西|西北工业大学|NWPU|<a href="http://job.nwpu.edu.cn/jobInfoList.do?page=1&order=infoPlus.submitTime&sort=desc&filter=%7bstatus%3a1%2cworkType%3a0%7d&ext=0">点我跳转</a>
陕西|长安大学|CHD|<a href="http://jyzx.chd.edu.cn/website/news_list.aspx?category_id=13">点我跳转</a>
陕西|西安电子科技大学|XIDIAN|<a href="http://job.xidian.edu.cn/index.html">点我跳转</a>
陕西|西北大学|NWU|<a href="http://jiuye.nwu.edu.cn/website/news_list.aspx?category_id=111">点我跳转</a>
安徽|合肥工业大学|HFUT|<a href="http://gdjy.hfut.edu.cn/products/list/4.html">点我跳转</a>
安徽|安徽大学|AHU|<a href="http://www.job.ahu.edu.cn/detach.portal?pageIndex=1&.pmn=view&groupid=22&action=bulletinsMoreView&pageSize=&.ia=false&.pen=pe2">点我跳转</a>
安徽|安徽师范大学|AHNU|<a href="http://60.174.234.53:264/index.php/zxzp.html">点我跳转</a>
海南|海南医学院|HAINMC|<a href="http://210.37.79.115:818/#">点我跳转</a>
江苏|东南大学|SEU|<a href="http://seu.91job.gov.cn/campus/index?city=">点我跳转</a>
江苏|南京农业大学|NJAU|<a href="http://njau.91job.gov.cn/campus/index?city=">点我跳转</a>
江苏|河海大学|HHU|<a href="http://hhu.91job.gov.cn/">点我跳转</a>
四川|电子科技大学|UESTC|<a href="http://www.jiuye.org/career/info/otherRec.html?page=1&">点我跳转</a>
四川|西南交通大学|SWJTU|<a href="http://106.3.35.197/eweb/jygl/zpfw.so?modcode=jygl_zpxxck&subsyscode=zpfw&type=searchZpxx&xxlb=5100">点我跳转</a>
广东|华南理工大学|SCUT|<a href="http://jyzx.6ihnep7.cas.scut.edu.cn/jyzx/xs/zpxx/wlzp/">点我跳转</a>
广东|中山大学|SYSU|<a href="https://career.sysu.edu.cn/(S(px1cs2mv2q3s5n2y3racroqm))/Management_Demand/JOL_Require/Public/RequireManage.aspx">点我跳转</a>
广东|暨南大学|JNU|<a href="http://career.jnu.edu.cn/showmore.php?actiontype=0">点我跳转</a>
广东|华南师范大学|SCNU|<a href="http://career.scnu.edu.cn/Recruitment/index">点我跳转</a>
广东|广州大学|GZHU|<a href="http://zsjy.gzhu.edu.cn/jy_list.jsp?urltype=tree.TreeTempUrl&wbtreeid=1101">点我跳转</a>
福建|厦门大学|XMU|<a href="http://jyzd.xmu.edu.cn/">点我跳转</a>
福建|福州大学|FZU|<a href="http://www.fjrclh.com/newslistnew.asp?classid=16&Nclassid=42">点我跳转</a>
福建|福建师范大学|FNU|<a href="http://career.fjnu.edu.cn/?category-69.cfm">点我跳转</a>
福建|华侨大学|HQU|<a href="http://bys.hqu.edu.cn/zpzl/zpxx.htm">点我跳转</a>
湖北|武汉大学|WHU|<a href="http://www.xsjy.whu.edu.cn/zftal-web/zfjy!wzxx!whdx10486/dwzpxx_cxWzDwzpxxEX.html?zpdxType=1#iframe_139754366237057873">点我跳转</a>
湖北|华中科技大学|HUST|<a href="http://job.hust.edu.cn/searchJob.jspx?type=2&fbsj=">点我跳转</a>
湖北|中南财经政法大学|ZNUFE|<a href="http://jyzx.znufe.edu.cn/career/recruit-4">点我跳转</a>
广西|广西大学|GXU|<a href="http://job.gxu.edu.cn/job_dwxx/list.asp?page=MQ==">点我跳转</a>
广西|广西师范大学|GXNU|<a href="http://www.cg.gxnu.edu.cn/index.aspx">点我跳转</a>
广西|桂林电子科技大学|GUET|<a href="http://job.guet.edu.cn/Home/ArticleList?label=16">点我跳转</a>
浙江|浙江大学|ZJU|<a href="http://www.career.zju.edu.cn//type/01010302.html">点我跳转</a>
浙江|杭州电子科技大学|HDU|<a href="http://career.hdu.edu.cn/module/onlines">点我跳转</a>
浙江|浙江工业大学|ZJUT|<a href="http://zjut.jysd.com/">点我跳转</a>
浙江|浙江师范大学|ZJNU|<a href="http://zjnu.jysd.com/campus">点我跳转</a>
湖南|中南大学|CSU|<a href="http://jobsky.csu.edu.cn/Home/ArticleList/4">点我跳转</a>
湖南|湖南大学|HNU|<a href="http://scc.hnu.edu.cn/">点我跳转</a>
江西|江西财经大学|JXUFE|<a href="http://career.jxufe.edu.cn/module/onlines">点我跳转</a>
江西|东华理工大学|ECUT|<a href="http://jyb.ecut.edu.cn/zpxx_4196/list.htm">点我跳转</a>
云南|昆明理工大学|KMUST|<a href="http://job.kmust.edu.cn/module/onlines?menu_id=4635">点我跳转</a>
云南|云南师范大学|YNNU|<a href="http://job.ynnu.edu.cn/index.php/Schoolp/News/lists?id=909">点我跳转</a>
云南|云南财经大学|YNUFE|<a href="http://jy.ynufe.edu.cn/module/onlines">点我跳转</a>
贵州|贵州大学|GZU|<a href="http://jobs.gzu.edu.cn/gzujobs/client/recruitment/2">点我跳转</a>
贵州|贵州师范大学|GZNU|<a href="http://zjc.gznu.cn:888/recruitment/network">点我跳转</a>
贵州|贵州民族大学|GZMU|<a href="http://zjc.gzmu.edu.cn/jyxxw/xs/jyxx/jy.htm">点我跳转</a>
青海|青海大学|QHU|<a href="http://jyw.qhu.edu.cn/jyxx/tzgg_jyxx/zpxx/index.htm">点我跳转</a>
青海|青海师范大学|QHNU|<a href="http://jc.qhnu.edu.cn/home-article-index-modnav-10.shtml">点我跳转</a>
甘肃|兰州大学|LZU|<a href="http://job.lzu.edu.cn/htmlfile/article/list/28/list_1.shtml">点我跳转</a>
甘肃|西北师范大学|NWNU|<a href="http://grad.nwnu.edu.cn/?c=article&a=type&tid=26">点我跳转</a>
甘肃|兰州交通大学|LZJTU|<a href="http://jyzx.lzjtu.edu.cn/eweb/jygl/zpfw.so?modcode=jygl_zpxxck&subsyscode=zpfw&type=searchZpxx">点我跳转</a>
内蒙古|内蒙古大学|IMU|<a href="http://job.imu.edu.cn/JobInfo/List/24">点我跳转</a>
内蒙古|内蒙古农业大学|IMAU|<a href="http://job.imau.edu.cn/xs/jyxx/xxfb.htm">点我跳转</a>
内蒙古|内蒙古师范大学|IMNU|<a href="http://jy.imnu.edu.cn/c17.jsp">点我跳转</a>
宁夏|北方民族大学|NUN|<a href="http://jyc.nun.edu.cn/eweb/jygl/zpfw.so?modcode=jygl_scfwzpxx&subsyscode=zpfw&type=searchZprd&sysType=TPZPFW&zpxxType=new">点我跳转</a>
新疆|新疆大学|XJU|<a href="http://zsjy.xju.edu.cn/zpxx.htm">点我跳转</a>
新疆|石河子大学|SHZU|<a href="http://scc.shzu.edu.cn/7640/list.htm">点我跳转</a>
新疆|新疆师范大学|XJNU|<a href="http://jyzdzx.xjnu.edu.cn/1445/list.htm">点我跳转</a>
新疆|西藏大学|UTIBET|<a href="http://www.utibet.edu.cn/news/article_38_58_0.html">点我跳转</a>


## 现有网站
如果你不想自己开发一套网站，可以直接使用我部署的服务<br>
http://jiandan.live/

## 后话
各高校就业信息网地址/结构可能变更，导致部分爬虫失效，可以在<a href="https://github.com/tomxin7/jiandan_job/issues">ISSUES</a>中提交，我会抽时间修复，当然一个人的力量是有限的，希望更多的同学可以加入进来，提交更加优质的代码。

## 如何联系我？
邮箱：admin@tomxin.cn<br>
个人主页：http://tomxin.cn


![mark](http://qiniu.tomxin.cn/181043_76e4d5b8_87650.png)





























