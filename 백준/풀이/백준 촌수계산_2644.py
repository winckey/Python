import sys
from collections import defaultdict
import copy

minCount = 999999


def dfs (end , s , visited , amap , count ) :
    
    global minCount
    
    if s == end :
        minCount = min (minCount , count)
        return 
    
    for i in range(len(amap)) : 
        if amap[s][i] !=0 and not visited[s][i]:
            visited[s][i] = True
            dfs(end ,  i , visited , amap , count+1) 
            visited[s][i] = False
            
n = int(input())

a, b = map(int , input().split())

case = int(input())
amap = [[0]*(n+1) for i in range(n+1)]
visited = [[False]*(n+1) for i in range(n+1)]

for i in range(case) : 
    y , x = map(int , input().split())
    amap[x][y] = 1
    amap[y][x] = 1
    
dfs(b , a , visited , amap , 0)

if minCount == 999999 :  
    print(-1)
else : 
    print(minCount)    


        
