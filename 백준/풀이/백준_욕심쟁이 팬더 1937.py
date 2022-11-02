from collections import deque

n = int(input())
gmax = -1
arr = [list(map(int , input().split())) for i in range(n)]

def bfs ( a , b ) :
    global gmax
    dy = [ 1, -1 , 0, 0]
    dx = [0 , 0, 1, -1]

    q = deque()
    
    q.append( (a , b, 1))

    while q : 
        y, x, count = q.popleft()
        for i in range(4) : 
            ny = dy[i] +y
            nx = dx[i] +x
            if  0<=ny < n and 0<= nx < n and arr[ny][nx] > arr[y][x] :
                gmax = max( gmax , count+1)  
                q.append( (ny , nx , count+1))



















for y in range(n) : 
    for x in range(n) :
        bfs( y, x)



print (gmax)




