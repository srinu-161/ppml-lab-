dict={}
print (''' enter elements of
        dictionary''' )
for i in range(5):
    key=input("enter key word : ")
    value=input("enter value : ")
    dict[key]=value
print(dict.keys())
print(dict.values())
print(dict)