num = int(input("Enter any number: "))

factor = 0

for i in range(1, num + 1):
    if num % i == 0:
        factor += 1

if factor == 2:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")