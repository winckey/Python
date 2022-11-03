from lib2to3.pgen2.token import AMPER
import sys
from collections import defaultdict
import copy



def dfs (end , s , amap , count ) :

    if s == end :
        visited[end] = min (visited[end] , count )
        return 
    
    for i in amap[s] : 
        if visited[i] > count : 
            visited[i] = count 
            dfs (end , i , amap , count+1 ) 



n = int(input())

a, b = map(int , input().split())

case = int(input())
amap = [[] for i in range(n+1)]
visited = [999999]*(n+1)

for i in range(case) : 
    y , x = map(int , input().split())
    amap[x].append(y)
    amap[y].append(x)
 
dfs(a , b  , amap , 1)
 
    
if visited[a] == 999999 :  
    print(-1)
else : 
    print(visited[a])    


        
