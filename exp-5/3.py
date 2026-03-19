# Celsius to Fahrenheit conversion using while loop
celsius = 0 
limit = 50
while celsius <= limit:
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}C = {fahrenheit}F")
    celsius += 10 