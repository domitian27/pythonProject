n = int(input("Number: "))
for i in range(n+1):
    print(i, end=" ")
    if i%2 == 0:
        print("even ")
    else:
        print("odd ")