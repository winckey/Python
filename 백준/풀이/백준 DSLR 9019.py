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
    r = n//1000 + ((n//100)%10)*10 + ((n//10)%10)*100 + n%10*1000
    
    return r
    
def r ( n ) :

    r = 0
    r = n//1000 *100 + ((n//100)%10)*10 + ((n//10)%10) + n%10*1000
    
    return r
    
    
    
for _ in range(int(input())):
    
    
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
        
        
        queue.append( (d(num) , method +['D']) ) 
        queue.append( (s(num) , method +['S'] )) 
        queue.append( (l(num) , method +['L']) ) 
        queue.append( (r(num) , method +['R'] ))     
        
        
    
    
