# -*- coding: utf8 -*-

import os
import sys
import MySQLdb
import urllib2
from bs4 import BeautifulSoup
import datetime

reload(sys)
sys.setdefaultencoding("utf-8")

def get_soup(url):
        res = urllib2.urlopen(url)
        html = res.read()
        soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
        data = soup.find_all('a', attrs={'style': 'min-height: 100px;', 'target': '_blank'})
        return data



if len(sys.argv)==1:
        now = datetime.datetime.now()
        date = now.strftime('%Y%m%d')
else:
        date = sys.argv[1]

print date
urls=[                            
        'https://www.chandashi.com/home/ranking/index/type/free/genre/0/country/cn.html?date='+date,
        'https://www.chandashi.com/home/ranking/index/type/free/genre/6014/country/cn.html?date='+date,
        'https://www.chandashi.com/home/ranking/index/type/free/genre/6002/country/cn.html?date='+date,
        'https://www.chandashi.com/home/ranking/index/type/grossing/country/cn/date.html?date='+date,
        'https://www.chandashi.com/home/ranking/index/type/grossing/genre/6014/country/cn.html?date='+date,
        ]
conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='123456',
        db ='my_db',
		charset='utf8',
        )
cur = conn.cursor()
conn.autocommit(1)#数据库自动提交
j = 1
for url in urls:
        if j==1:
                free = 1
                type = 0
                name = u'免费总榜'
        elif j==2:
                free = 1
                type = 1
                name = u'免费游戏榜'
        elif j==3:
                free = 1
                type = 2
                name = u'免费工具榜'
        elif j==4:
                free = 0
                type = 0
                name = u'畅销总榜'
        else:
                free = 0
                type = 1
                name = u'畅销游戏榜'
        j=j+1

        data = get_soup(url)
        tmp = []
        i = 1
        for chr in data:
                tu = (chr.string, i,free,type,date[0:4]+'-'+date[4:6]+'-'+date[6:8]+'-')
                i = i + 1
                tmp.append(tu)
        tup = tuple(tmp)
        #print tup
        cur.executemany("insert into my_db.appstore_hot_bak (name,rank,free,type,date) values(%s,%s,%s,%s,%s)",tup)
        print name+u'top200导入成功'

        datamore = get_soup(url+'?view=more')
        tmpm = []
        im = 201
        for chrm in datamore:
                tum = (chrm.string, im,free,type,date[0:4]+'-'+date[4:6]+'-'+date[6:8]+'-')
                im = im + 1
                tmpm.append(tum)
        tupm = tuple(tmpm)
        #print tup
        cur.executemany("insert into my_db.appstore_hot_bak (name,rank,free,type,date) values(%s,%s,%s,%s,%s)",tupm)
        print name+u'更多导入成功'
