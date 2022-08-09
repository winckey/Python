import sys
from collections import deque

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
x = int(input())
count =0;



for i in arr : 
    for j in arr : 
        if(i + j  == x):
            count +=1;
            
            
print(count/2)            