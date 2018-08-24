# coding=utf-8

import os
import jieba
import jieba.posseg as pseg


seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式 默认

seg_list = jieba.cut_for_search("我来到北京清华大学,觉得这里挺好")  # 搜索引擎模式
print(", ".join(seg_list))

result= pseg.cut("我来到北京清华大学,觉得这里挺好的，123。你说呢，玩不了打装备闪退未到账没有到账")
for x in result:
    print x.word + "|" + x.flag


# list = [x.word for x in result if x.flag not in ['w']]

# print list

# print pwd

# print father_path

# print grader_father
