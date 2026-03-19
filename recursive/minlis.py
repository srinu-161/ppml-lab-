def r_m(l):
    if len(l)==1:
        return l[0]
    else:
        m=r_m(l[1:])
        return l[0]if l[0]<m else m
lis=[1,2,3,422,0]
print (r_m(lis))