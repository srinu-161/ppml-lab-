def prime(n):
    for j in range (2,n):
        if n%j==0:
            break
        else:
            print("is prime")
n=int(input ("enter a number : "))
prime(n)