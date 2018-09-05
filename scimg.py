# -*- coding: utf8 -*-
import os
import sys
import requests
import click
reload(sys)
sys.setdefaultencoding('utf-8')

r = requests.get(
    'http://service.aibizhi.adesk.com/v1/lightwp/category?appid=com.lovebizhi.ipad&appver=5.1&appvercode=64&channel=ipicture&lan=zh-Hans-CN&sys_model=iPhone&sys_name=iOS&sys_ver=11.4.1')

imgListURL = 'http://service.aibizhi.adesk.com/v1/vertical/category/4e4d610cdf714d2966000000/vertical?adult=0&appid=com.lovebizhi.ipad&appver=5.1&appvercode=64&channel=ipicture&first=1&lan=zh-Hans-CN&limit=30&skip=0&sys_model=iPhone&sys_name=iOS&sys_ver=11.4.1'

@click.command()
@click.option('--skip', default=1, help='深度')
@click.option('--start', default=1, help='第几个开始')
def go(skip, start):
    print("skip num:", skip)
    print("start num:", start)
    count = 1
    # 循环深度
    for i in range(skip):
        # 得到分类id
        for re in r.json()['res']['category']:
            # 循环深度首次创建文件夹
            if i == 0:
                mkdir(u'../resource/' + re['name'])
            # 组合链接
            listR = requests.get('http://service.aibizhi.adesk.com/v1/vertical/category/' + re[
                'id'] + '/vertical?adult=0&appid=com.lovebizhi.ipad&appver=5.1&appvercode=64&channel=ipicture&first=1&lan=zh-Hans-CN&limit=30&skip=' + str(
                i * 30) + '&sys_model=iPhone&sys_name=iOS&sys_ver=11.4.1')
            # print type(listR.json())
            for listRe in listR.json()['res']['vertical']:
                if count >= start:
                    print u'正在偷偷下载第 ' + str(count) + u' 张图片 分类为：' + re['name'] + u' 深度为：' + str(i)
                    with open(u'../resource/' + re['name'] + '/' + re['name'] + '_' + listRe['id'] + '.jpg', 'wb') as f:
                        f.write(requests.get(listRe['img']).content)
                else:
                    print '第' + str(count) + u' 张图片跳过 分类为：' + re['name'] + u' 深度为：' + str(i)
                count += 1

    print u'下载完成'

# 字符串的字典 转 字典类型 1、json(), 不支持单引号，2、veal()说可能存在安全问题 3、literal_eval不存在上述问题

def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print path + ' 创建成功'
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print path + ' 目录已存在'
        return False


if __name__ == "__main__":
    go()





