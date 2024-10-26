n = int(input("Number: "))
prod = 1
for i in range(1, n+1):
    prod *= i
print(f"{n}! is {prod}")