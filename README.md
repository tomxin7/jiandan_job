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

##### 5、新增学校，如果没有自己学校的代码，可以复制demo这个文件，按照格式编写代码即可，针对爬虫不是很熟悉的同学，后期可能会写一个简单的入门教程


## 已收录高校

姓名|技能|排行
--|:--:|--:
刘备|哭|大哥
关羽|打|二哥
张飞|骂|三弟

## 更多好玩的

关注公众号：程序员的小浪漫，爱上简单的生活

![mark](http://qiniu.tomxin.cn/blog/180521/Echm6dehec.jpg?imageslim)
