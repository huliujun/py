# python 学习
组内共享学习
在自己的电脑上克隆此项目：

git clone https://github.com/huliujun/py.git
# 学习资料
## python
* python菜鸟教程：[猛搓此连接](http://www.runoob.com/python/python-tutorial.html)

* python廖雪峰教程：[猛搓此连接](https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000
)
* 资源大全中文版：[猛搓此连接](https://github.com/jobbole/awesome-python-cn)
## 爬虫
* scrapy中文学习文档：[猛搓此连接](https://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html)

* bs4中文学习文档：[猛搓此连接](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#id4)

* xpath学习文档：[猛搓此连接](http://www.runoob.com/xpath/xpath-tutorial.html)

* 手机抓包软件推荐： [charles，猛搓去百度](https://www.baidu.com/s?ie=utf-8&wd=charles%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95)

## 数据分析
* numpy中文学习文档：[猛搓此连接](https://yiyibooks.cn/xx/NumPy_v111/index.html)

* pandas中文学习文档：[猛搓此连接](https://yiyibooks.cn/dongyongping1015/pandas_0220/html/10min.html)

* 利用Python进行数据分析(中文版)： [猛搓下载PDF](http://file3.data.weipan.cn/31580122/8477461aaf63578ae5957cb7381bb152b2b05612?ip=1535613055,101.86.117.219&ssig=FsOFPN2FJm&Expires=1535613655&KID=sae,l30zoo1wmz&fn=%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%EF%BC%8C%E4%B8%AD%E6%96%87%E7%89%88%EF%BC%88%E6%89%AB%E6%8F%8F%E7%89%88%EF%BC%89.pdf&se_ip_debug=101.86.117.219&from=1221134)


## 相关工具推荐
* json格式化：[猛搓此连接1](https://www.json.cn/)
   [猛搓此连接2](http://www.bejson.com/)
   
* 简单的git学习（对菜菜来说够了）：[猛搓此连接](http://www.bootcss.com/p/git-guide/)
* git进阶：[官方中文文档](https://git-scm.com/book/zh/v2)

## 学习案例
   按部就班系统学习枯燥无味，来几个案例给学习加点料
   * 案例1：bs4爬取app store苹果榜单
        * 见 hot.py
        * 需有本地数据库支持，表结构见appstore_hot_bak.sql
        * 默认爬取今天的排行榜数据，参数1可制定日期如：
            ```
            python hot.py 20180828
            ```
   * 案例2：抓包爬取  短视频/图片（有mm）
        * 见 sc.py(视频) scimg.py(图片)
        * 运行脚本自动下载，默认深度为1（无参数）
        * 第一个参数为下载深度，第二个参数为下载起点（解决断点后续加入异步下载）如：
            ```
            python sc.py 10 100
            ```
        * 下载目录：../resource(图片) ../mp4(视频)
   * 案例3：分词 将一些句子切出分词并统计
        * 见fenci/fen.py
        * 将需要分词的句子存放在fenci/txt/文件夹，格式为txt，脚本自动读取该文件夹下所有txt文件，然后输分词集于fenci/result，并逆序排列分词

***
*好好学习天天向上*
***  