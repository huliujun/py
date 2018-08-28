# -*- coding: utf8 -*-

import sys
import MySQLdb
import urllib2
from bs4 import BeautifulSoup
import datetime

reload(sys)
sys.setdefaultencoding("utf-8")

# 获取参数，默认今天
if len(sys.argv) == 1:
    now = datetime.datetime.now()
    date = now.strftime('%Y%m%d')
else:
    date = sys.argv[1]

# 连接数据库
conn = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='my_db',
    charset='utf8',
)
cur = conn.cursor()
conn.autocommit(1)  # 数据库自动提交

# 爬虫获取块
def get_soup(url):
    a_all=[]
    res = urllib2.urlopen(url)
    html = res.read()
    soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
    p = soup.find_all('p', attrs={'class': 'developer'})
    for a in p:
        a_all.append(a.find('a'))
    return a_all

# 爬取信息配置
json_config = [
    {'free':1,'type':0,'name':u'免费总榜','url':'https://www.chandashi.com/home/ranking/index/type/free/genre/0/country/cn.html?date=' + date},
    {'free':1,'type':1,'name':u'免费游戏榜','url':'https://www.chandashi.com/home/ranking/index/type/free/genre/6014/country/cn.html?date=' + date},
    {'free':1,'type':2,'name':u'免费工具榜','url':'https://www.chandashi.com/home/ranking/index/type/free/genre/6002/country/cn.html?date=' + date},
    {'free':0,'type':0,'name':u'畅销总榜','url':'https://www.chandashi.com/home/ranking/index/type/grossing/country/cn/date.html?date=' + date},
    {'free':0,'type':0,'name':u'畅销游戏榜','url':'https://www.chandashi.com/home/ranking/index/type/grossing/genre/6014/country/cn.html?date=' + date}
]

# 循环爬取
for value in json_config:
    tmp = []
    i = 1
    a_all = get_soup(value['url'])
    for a in a_all:
        tu = (a.get('title'), a.string, i, value['free'], value['type'], date[0:4] + '-' + date[4:6] + '-' + date[6:8])
        i = i + 1
        tmp.append(tu)

    a_all_more = get_soup(value['url'] + '&view=more')
    for a in a_all_more:
        tu = (a.get('title'), a.string, i, value['free'], value['type'], date[0:4] + '-' + date[4:6] + '-' + date[6:8])
        i = i + 1
        tmp.append(tu)
    tup = tuple(tmp)
    cur.executemany("insert into my_db.appstore_hot_bak (name,corp,rank,free,type,date) values(%s,%s,%s,%s,%s,%s)", tup)
    print value['name'] + u'导入成功'
print u'脚本运行完毕'