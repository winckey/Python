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
        
        ty , tx , count = queue.popleft()

        if ty == ey and tx == ex :

            print(count)
            break 
       
        
        for ny, nx in zip(dylist , dxlist) :
            y = ny + ty
            x = nx + tx

            if  0<= y < l and 0<= x < l and visite[y][x] == 0 :
                visite[y][x] = 1
                queue.append( (y , x , count+1) )
                

        
        
    
    
