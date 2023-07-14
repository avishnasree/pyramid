n = 6
for i in range(n,0,-1):
    for k in range(0,n-i+1):
        print(" ",end="")
    for j in  range(0,i):
        print("*",end="")
    print()