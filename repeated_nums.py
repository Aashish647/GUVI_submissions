num = (raw_input().strip())
res=""
if num<0:
    print 0
else:
    for i in num:
        if num.count(i)>1:
                res.append(i)

                print int(res)
