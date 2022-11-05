from collections import deque
import queue


for _ in range(int(input())):
    
    dy = [ -2 , -1 , 1 , 2, 2, 1, -1, -2]
    dx = [ 1  , 2  , 2 , 1,-1,-2,-2 , -1]
    
    
    
    l = int(input()) 
    sy , sx = map(int , input().split())
    ey , ex = map(int , input().split())
    visite = [[False]*l for i in range(l)]
    
    
    
    
    
    
    queue = deque()
    
    queue.append((sy , sx , 0))
    visite[sy][sx] = True
    while queue :
        
        ty , tx , count = queue.popleft()

        if ty == ey and tx == ex :

            print(count)
            break 
       
        
        for ny, nx in zip(dy , dx) :
            y = ny + ty
            x = nx + tx

            if  0<= y < l and 0<= x < l and not visite[y][x] :
                visite[y][x] = True
                queue.append( (y , x , count+1) )
            
        
        
    
    
