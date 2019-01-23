symbol = "*"
for j in range(1,5,1):
    for i in range(1, j+1, 1):
        print(symbol,end="")
    print("")

print("\n"+("="*50)+"\n"*2)

count = 1
while count < 5:
    print("*" * count)
    count = count + 1
