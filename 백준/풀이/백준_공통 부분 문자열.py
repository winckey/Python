
a = input()
b = input()
cmap = [[0]*(len(b) + 1) for _ in range(len(a) +1)] 
for i in range(1, len(a)+1) :
    for j in range(1, len(b)+1) :
        if a[i-1] == b[j-1] : 
            cmap[i][j] = cmap[i-1][j-1]+1
            
print(max(map ( max , cmap ) ))            

