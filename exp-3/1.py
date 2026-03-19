#wpa to check string is palinderome or not
s=input("enter a word : ")
if s[0:len(s)]==s[::-1]:
    print("entered string is pallindrome")
else:
    print("entered string is not a pallindrome") 