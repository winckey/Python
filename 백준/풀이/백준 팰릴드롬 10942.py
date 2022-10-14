import sys
from collections import defaultdict
n = input()
arr = list(map(int, sys.stdin.readline().split()))

arr.insert(0,0)

psum1 = []
psum2 = []

ps1 = 0
ps2 = 0
for i in range(1, len(arr)) :
    ps1 +=arr[i]
    ps2 +=arr[-i]
    psum1.append(ps1)
    psum2.append(ps2)
psum1.insert(0,0)
psum2.insert(0,0) 
    
for i in range(1, len(psum1)) :
    psum1[i] += psum2[-i]   
    
    
m = int(input())

for _ in range(m) :
    a , b = map(int , input().split())      
    if psum1[a] == psum1[b] :
        print(1)
    else :
        print(0)    