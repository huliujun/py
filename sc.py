# coding=utf-8

import os
import sys
import requests

# 深度
skip = 1
# 第几个开始
start = 1

if len(sys.argv) == 2:
    skip = int(sys.argv[1])

if len(sys.argv) == 3:
    skip = int(sys.argv[1])
    start = int(sys.argv[2])

r = requests.get(
    'https://service.videowp.adesk.com/v1/aibizhi/category?appid=com.lovebizhi.ipad&appver=5.1&appvercode=64&channel=ipicture&lan=zh-Hans-CN&sys_model=iPhone&sys_name=iOS&sys_ver=11.4.1')
# print type(r.json())

imgListURL = 'https://service.videowp.adesk.com/v1/aibizhi/videowp?appid=com.lovebizhi.ipad&appver=5.1&appvercode=64&channel=ipicture&lan=zh-Hans-CN&limit=30&sys_model=iPhone&sys_name=iOS&sys_ver=11.4.1'

# 字符串的字典 转 字典类型 1、json(), 不支持单引号，2、veal()说可能存在安全问题 3、literal_eval不存在上述问题
for re in r.json()['res']['category']:

    # print re['name']
    # print re['id'] 

    if re['name'] != u'1':

        count = 1
        for i in range(skip):

            parm = {'category': re['id'], 'skip': str(i * 30)}
            listR = requests.get(imgListURL, params=parm)
            # print type(listR.json())
            for listRe in listR.json()['res']['videowp']:
                if count >= 416:
                    print '正在偷偷下载第 ' + str(count) + '个mm视频'
                    with open(re['name'] + '_' + listRe['name'] + '.mp4', 'wb') as f:
                        f.write(requests.get(listRe['video']).content)
                else:
                    print '第' + str(count) + '个mm视频跳过'
                count += 1
    else:
        print re['name'] + u'分类跳过'

print '下载完成'
