def power(n,m):
    if m==0:
        return 1
    else:
        return power(n,m-1)*n
print(power(2,4))