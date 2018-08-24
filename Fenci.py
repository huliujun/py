# coding=utf-8
import pandas as pd
import jieba
import os
import jieba.posseg as pseg
import xlwt


def jieba_seg(sentence):
    result = pseg.cut(sentence)
    list = [x.word for x in result if x.flag not in ['x', 'r']]
    return list


# 替换句子中的特殊字符
def replace_new(sentence):
    list_w = [",", ".", "，", "。", "？", "！", "……", "~", " ", "'", "(", ")", "*", "+", "-", "/"]
    temp = sentence
    for w in list_w:
        temp = str(temp).replace(w, "")
    return temp


def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.csv':
                L.append(os.path.join(root, file))
    return L


# 当前文件的路径
pwd = os.getcwd()
# 自动识别并输入待分词统计文件 格式为 .csv 编码是utf-8
inputFile = file_name(pwd)[0]
# 输出统计好的文件，输出为 .xls 格式
outputFile = os.path.splitext(inputFile)[0] + "_结果.xls"
# 自定义词典位置，格式为 .txt 编码是utf-8
dictFile = "/Users/huliujun/py/dict.txt"

df = pd.read_csv(inputFile)
# print df.head
jieba.load_userdict(dictFile)

words_num = {}
rows_num = int(df.size)
print("处理的数据行数为：%d" % rows_num)

for i in range(0, rows_num):  # 迭代 0 到 最后一行 之间的数字
    sentences = df.loc[i].values[0]
    # new_s = replace_new(sentences)

    words_list = jieba_seg(sentences)

    for word in words_list:

        temp = words_num.get(word, 0)
        if (temp == 0):
            words_num[word] = 1
        else:
            words_num[word] = temp + 1

# 排序字典，按value 逆序 返回 tuple构成的数组
data = sorted(words_num.items(), key=lambda x: x[1], reverse=True)

file = xlwt.Workbook(encoding='utf-8')
table = file.add_sheet('words and counts')

# 循环写入
for i, p in enumerate(data):
    for j, q in enumerate(p):
        table.write(i, j, q)
file.save(outputFile)
