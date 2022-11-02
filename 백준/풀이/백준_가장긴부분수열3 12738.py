from array import array
import bisect

n = int(input())

arr = list(map(int, input().split()))


dp = [0]*n

bidp = []
bisect.insort(bidp , (arr[0] , 1))

for i in range(1 , len(arr)) :
    
    x = bisect.bisect_left(bidp , (arr[i],0))
    if x == 0 :
        bisect.insort(bidp , (arr[i] , 1))
    else :
        dpnum , count = bidp[x-1]
        bisect.insort(bidp , (arr[i] , count+1))


a, b = bidp[-1]

print(b)