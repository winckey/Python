import sys
from collections import defaultdict
n = input()
arr = list(map(int, sys.stdin.readline().split()))

arr = [[False]* n for i in range(n)]

for _ in range(m) :
    a , b = map(int , input().split())      
    if psum1[a] == psum1[b] :
        print(1)
    else :
        print(0)    