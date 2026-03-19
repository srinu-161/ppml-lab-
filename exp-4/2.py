count = 0
n = int(input("Enter a number: "))
i = 1

while i <= n:
    if n % i == 0:
        count += 1
    i += 1

if count == 2:
    print("Your number is prime.")
else:
    print("Your number is not prime.")