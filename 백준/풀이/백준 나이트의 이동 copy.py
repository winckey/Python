from collections import deque
import queue


for _ in range(int(input())):
    
    dxlist = [-2, -2, 2, 2, -1, 1,-1, 1]
    dylist = [-1, 1,-1, 1, -2, -2, 2, 2]
    l = int(input()) 
    sy , sx = map(int , input().rsplit())
    ey , ex = map(int , input().rsplit())
    visite = [[0] * l for _ in range(l)]
    
    
    
    
    
    
    queue = deque()
    
    queue.append((sy , sx , 0))
    visite[sy][sx] = 1
    while queue :
        
        y , x , count = queue.popleft()

        if y == ey and x == ex :

            print(count)
            break 
       
        
        for dy, dx in zip(dylist , dxlist) :
            ny = dy + y
            nx = dx + x

            if  0<= ny < l and 0<= nx < l and visite[ny][nx] == 0 :
                visite[ny][nx] = 1
                queue.append( (ny , nx , count+1) )
            
        
        
    
    
