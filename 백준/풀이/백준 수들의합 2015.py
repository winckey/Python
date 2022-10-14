import sys
from collections import defaultdict
n, m = map(int, input().split())
arr_n = list(map(int, sys.stdin.readline().split()))


rarr = defaultdict(int)
parr = []

count =0
psum =0;
for a in arr_n : 
    psum = psum + a ;
    parr.append(psum)

for a in parr :
    if a == m :
        count += 1
    
    count += rarr[a - m]
    rarr[a] += 1
        
print(count)         