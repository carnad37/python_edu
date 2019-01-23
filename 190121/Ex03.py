for i in range(2,10,1):
    for j in range(1,10,1):
        div = i*j
        print("%d * %d = %d"%(i,j,div),end="\t")
    print("\n")
print("\n"+("="*50)+"\n"*2)

for i in range(1,10,1):
    for j in range(2,10,1):
        div = i*j
        print("%d * %d = %d"%(j,i,div),end="\t")
    print("\n")


#i * j인데,->으로 j가 상승.
#두번째는 j가 ->로 상승.
