# wap to check wetehr a string  is a symmetrical or pallindrome

s = input("Enter a string: ")
z=(str(str(s)[::1]))
if s==z:
    print("it is pallindrome")
else:
    print("it is not pallindrome")