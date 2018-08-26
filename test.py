# coding=utf-8

# import os
# import jieba
# import jieba.posseg as pseg
import sys
import os

if len(sys.argv) == 2 :
    print sys.argv[1]
# print(sys.argv[1])

# seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式

# seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
# print("Default Mode: " + "/ ".join(seg_list))  # 精确模式 默认

# seg_list = jieba.cut_for_search("我来到北京清华大学,觉得这里挺好")  # 搜索引擎模式
# print(", ".join(seg_list))

# result= pseg.cut("我来到北京清华大学,觉得这里挺好的，123。你说呢，玩不了打装备闪退未到账没有到账")
# for x in result:
#     print x.word + "|" + x.flag


# list = [x.word for x in result if x.flag not in ['w']]

# print list

# print pwd

# print father_path

# print grader_father


def mkdir(path):
 
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
 
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
 
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path) 
 
        print path+' 创建成功'
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print path+' 目录已存在'
        return False
 

# 调用函数
mkdir('../mkpath')

with open('../mkpath/abc.txt', 'wb') as f:
    f.write('abc')
