from collections import deque


m,n = map(int, input().split())
arr = [ list(map(int, input())) for _ in range(n)]


arr2 = [[999]*m for i in range(n)]
arr2[0][0] = 0

dx = [ 0 , 0 , 1, -1]
dy = [ 1 , -1, 0 , 0]

q = deque()

q.append((0 ,0))

while q :
    y , x = q.popleft()

    for ty , tx in zip(dy , dx) :
        
        ny = ty + y
        nx = tx + x
        if ny >=0 and nx >= 0 and ny < n and nx < m :
            if arr2[y][x] + arr[ny][nx] < arr2[ny][nx] :
                arr2[ny][nx] = arr2[y][x] + arr[ny][nx]
                q.append((ny , nx))
    
    
    
print(arr2[n-1][m-1])
    

