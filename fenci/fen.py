# coding=utf-8
import jieba
import os
import jieba.posseg as pseg
import xlwt

# 切词
def jieba_seg(sentence):
    result = pseg.cut(sentence)
    list = [x.word for x in result if x.flag not in ['x', 'r']]
    return list
# 获取目录下csv文件
def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.txt':
                L.append(os.path.join(root, file))
    return L

# 自定义词典位置，格式为 .txt 编码是utf-8
dictFile = "./fenci/dict.txt"
jieba.load_userdict(dictFile)

# 自动识别并输入待分词统计文件 格式为 .csv 编码是utf-8
for inputFile in file_name('./fenci/txt/'):
    # 输出文件，输出为 .xls 格式
    outputFile = './fenci/result/' + inputFile.split('/')[-1].split('.')[0] + u'_结果.xls'
    words_num = {}
    filetxt = open(inputFile)
    for line in filetxt:
        words_list = jieba_seg(line)
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

    # 循环写入输出文件
    for i, p in enumerate(data):
        for j, q in enumerate(p):
            table.write(i, j, q)
    file.save(outputFile)
    print inputFile.split('/')[-1] + u'已分词，写入：' + outputFile
print u'脚本运行完毕'







