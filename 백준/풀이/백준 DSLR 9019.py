from collections import deque
from inspect import stack
import queue

def d ( n ) :
    return int(n)*2 % 10000 

def s ( n ) :
    r = int(n) - 1 
    if n == 0 :
        return 9999
    else :
        return r
    
def l ( n ) :
    
    r = 0
    r = n//1000 + ((n//100)%10)*1000 + ((n//10)%10)*100 + n%10*10
    return r
    
def r ( n ) :

    r = 0
    r = n//1000 *100 + ((n//100)%10)*10 + ((n//10)%10) + n%10*1000
    return r
    
    
    
    
for _ in range(int(input())):
    
    visited = [False for _ in range(10000)] 
    start , end = map(int , input().split())
  
    # test = 9989
    # print(d(test))
    # print(s(test))
    # print(l(test))
    # print(r(test))
    
    queue = deque()
    
    queue.append((start , [] ))
    
    
    while queue :
        
        num , method = queue.popleft()
        
        if num == end :
            print("".join(method))
            break;
        
        
        temp = d(num)
        if not visited[ temp] : 
            visited[temp] =True
            queue.append( (temp , method +['D']) ) 
        temp = s(num)
        if not visited[ temp] : 
            visited[temp] =True
            queue.append( (temp , method +['S'] )) 
        temp = l(num)
        if not visited[ temp] : 
            visited[temp] =True
            queue.append( (temp , method +['L']) ) 
        temp = r(num)
        if not visited[ temp] : 
            visited[temp] =True
            queue.append( (temp , method +['R'] ))         
                
        
    
    
