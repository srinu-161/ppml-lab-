sem=input("enter the sentence : ")
das=""
for x in sem:
    if x.islower():
        das+=x.upper()
    elif x.isupper():
        das+=x.lower()
       
print (das)