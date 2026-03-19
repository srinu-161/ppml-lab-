def revs(s):
    if len(s)==0:
        return s
    else:
        return revs(s[1:])
print(revs("srts"))