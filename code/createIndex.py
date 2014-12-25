#coding=utf8
import time
import string
import re
import MySQLdb


#输入文件的每一段是一篇文档,从0开始计数
#输出文件包括文档id和出现位置

def create_inverted_index(filename):
    print("read file %r...."%filename)
    src_data = open(filename).read()

    sub_list = []  #查找去重
    word = []
    result = {}
    
    sp_data = src_data.split('#')
    set_data = set(sp_data)
    word = list(set_data)

    src_list = src_data.split("\n")

    for w in range(0, len(word)):
        index = []
        for i in range(0,len(src_list)):#遍历所有文档
            sub_list = src_list[i].split('#') #文档中的每一个词项

            for j in range(0, len(sub_list)):
                if sub_list[j] == word[w]: #i代表文档编号，ｊ代表位置
                    index.append((i,j))
            result[word[w]] = index

    des_file = "des.txt"
    print('writing file...%r'%des_file)

    writefile = open(des_file, 'w')
#    termID = 0
    for k in result.keys():
#        termID += 1
#        cur.execute("insert into invertIndex(termID,term,DocID) values(%s,%s,%s)",(termID,str(k), str(result[k])))
        writefile.writelines(str(k) + ' ' + str(result[k]) + "\n")

    print("done")


#conn = MySQLdb.connect(host="127.0.0.1", user="root",passwd="nihao2a",db="invertedIndex")
#cur = conn.cursor()

start = time.time()
create_inverted_index("Result.txt")
end = time.time()

print "total time is %s"%str(end-start)
