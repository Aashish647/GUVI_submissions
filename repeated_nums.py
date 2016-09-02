def counter(num):
    d = {}
    for i in num:
        if num.count(i)>1:
                d[i] = num.count(i)

    res=""
    for i in d:
        if d[i]>1:
            res.append(i)
    print int(res)



num = (raw_input().strip())
res=""
try:
    num = int(num)
except:
    print "input should be a string"
    exit(0)

if num<0:
    print 0
else:
    counter(num)
