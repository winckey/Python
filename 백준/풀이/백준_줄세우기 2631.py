from bisect import bisect, bisect_left
import sys
from collections import deque

n = int(input())

arr= []
for i in range(1, n+1) : 
    arr.append(int(input()))

dp = []
dp.append(arr[0])
lens = 1


for i in range(1, n) : 
    if arr[i] > dp[-1] :
        dp.append(arr[i])
        lens += 1
    else : 
        x =bisect_left(dp , arr[i])
        dp[x] = arr[i]   


print(lens)

