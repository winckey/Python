import sys
from collections import defaultdict
n = input()
arr = [0]+list(map(int, sys.stdin.readline().split()))

dp = [[False]*(len(arr)) for _ in range(len(arr))]


def check( s  , e ) :
    if dp[s][e] :
        return True

    if e - s <= 1 :
        if arr[s] == arr[e] :
            dp[s][e] = True
            return True
        else : 
            return False
    if not check ( s +1 , e- 1) :
        return False
    dp[s][e] = True
    return True   

    
m = int(input())        
        

for _ in range(m) :
    a , b = map(int , input().split())      
    
    if (check(a , b)) :
        print(1)
    else :
        print(0)
