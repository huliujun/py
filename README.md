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

* 手机抓包软件推荐： charles(功能简单，可自行百度)

## 相关工具推荐
* json格式化：[猛搓此连接](https://www.json.cn/
   [猛搓此连接](http://www.bejson.com/)
   
* 简单的git学习（对菜菜来说够了）：[猛搓此连接](http://www.bootcss.com/p/git-guide/)
* git进阶：[猛搓此连接](https://git-scm.com/docs)

## 学习案例
   按部就班系统学习枯燥无味，来几个案例给学习加点料
   * 案例1：bs4爬取app store苹果榜单
        * 见 hot.py
        * 需有本地数据库支持，表结构见appstore_hot_bak.sql
        * 默认爬取今天的排行榜数据，参数1可制定日期如：python hot.py 20180828
   * 案例2：抓包爬取  短视频/图片（有mm）
        * 见 sc.py(视频) scimg.py(图片)
        * 运行脚本自动下载，默认深度为1（无参数）
        * 第一个参数为下载深度，第二个参数为下载起点（解决断点后续加入异步下载）如：python sc.py 10 100
        * 下载目录：../resource(图片) ../mp4(视频)
   * 案例3：分词 将一些句子切出分词并统计
        * 见Fenci.py
        * 将需要分词的句子存放csv文件，脚本自动读取并输出xls文件的分词集，并逆序排列
       