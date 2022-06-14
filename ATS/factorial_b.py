from math import prod


num=int(input(":"))
a=[]
l_list=[]
for i in range(1,num+1):
    a.append(i)
    r=prod(a)
    t=1/r
    l_list.append(t)
    print(sum(l_list)+1)