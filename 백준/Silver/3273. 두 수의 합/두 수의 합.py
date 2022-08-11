import sys
from collections import deque

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
x = int(input())

arr.sort()
end = N - 1
start = 0

count = 0

while start < end:
    sum = arr[start] + arr[end]
    if sum == x:
        count += 1
    if sum >= x:
        end -= 1
    elif sum < x:
        start += 1

print(count)
