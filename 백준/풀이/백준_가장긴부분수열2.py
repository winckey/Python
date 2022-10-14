from array import array
import bisect

n = int(input())
maxCout = 1;
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
        maxCout = max(maxCout , count+1)
        if x == len(bidp) :
            bidp.append((arr[i] , count+1))    
        else :
            dpnum2 , count2 = bidp[x]
            if dpnum2 == arr[i] :
                if count2 < count+1 :
                    bidp[x] = (arr[i] , count+1)
            else :
                bidp.insert(x ,(arr[i] , count+1) )


a, b = bidp[-1]

print(maxCout)