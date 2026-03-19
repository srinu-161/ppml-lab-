#FIBBONACI AND ADD EVEN NUMBERS
# Generate Fibonacci sequence up to 1000
fibonacci = [0, 1]
while True:
    next_val = fibonacci[-1] + fibonacci[-2]
    if next_val > 1000:
        break
    fibonacci.append(next_val)

even_fibonacci = [num for num in fibonacci if num % 2 == 0]
sum_even = sum(even_fibonacci)

print("Fibonacci sequence up to 1000:", fibonacci)
print("Even Fibonacci numbers:", even_fibonacci)
print("Sum of even Fibonacci numbers:", sum_even)   