def finder(inp):
    num = [x for x in inp if inp.count(x)==1]
    if num[0]!=None:
        print num[0]
    else:
        print "None found"

try:
    input = map(int,raw_input().strip())
    finder(input)
except:
    print "please enter integers only"
