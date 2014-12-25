import MySQLdb
import sys
import time
import os
import sets
import re
import string


conn = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '123456', charset='utf8', use_unicode=True)
        
curs = conn.cursor()
conn.select_db('invertedIndex')
    

def sql_select(x):
    a = []
    rows = []
    for i in range(len(x)):
        curs.execute("select `docID` from `Index` where `term` like %s", str(x[i]))
        rows.append(curs.fetchall())
    for i in range(len(x)):
        a.append(re.findall(r'\d+', str(rows[i])))
    return a

def and_op(x):
    start = time.time()
    c = sql_select(x)
    u = set.intersection(*map(set,c))
#    u = set.intersection(c)
#    j = 1
#    while j < len(x):
#        b = set(c[j]).intersection(c[j - 1])
#        j += 1
    end = time.time()
    return len(u), str(end-start)

def or_op(x):
    start = time.time()
    e = sql_select(x)
    k = 1
    u = set.union(*map(set,e))
#    while k < len(x):
#        d = set(e[k]).union(e[k - 1])
#        k += 1
    end = time.time()
    return len(u), str(end-start)

def main():
    while 1:
        x = raw_input().split()
        if(x[0] == 'q'):
            sys.exit(0)
        len1, time1 = and_op(x)
        len2, time2 = or_op(x)
        print "and: time = %s s, list_length = %s " %(time1, len1)
        print "or:  time = %s s, list_length = %s " %(time2, len2)

    conn.close()

if __name__ == "__main__":

    main()
