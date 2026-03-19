para=input("enter para : ")
words=para.split()
pali=0
for i in words:
    if i==i[::-1]:
        pali+=1
print("number of wprds : ",len(words))
print("number of pallindrome : ",pali)                                                                            