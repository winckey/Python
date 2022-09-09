

from collections import deque
import queue


m = int(input())
graph = [list(map(int, input().split())) for _ in range(m)]

visited = [[False] * m for _ in range(m)]


queue = deque()





dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
year = 0


count =0 
for i in range(m):
    for j in range(m):
        
        if graph[i][j] > m and not visited[i][j] :
            visited[i][j] = True
            queue.append((i,j))
            while queue:
                y , x = queue.popleft()
                for ty , tx in zip(dy , dx) :
                        ny = y+ ty
                        nx = x+ tx
                        if m > ny >=0 and m > nx >= 0 and not visited[ny][nx] and graph[ny][nx] > m:
                            visited[ny][nx] = True
                            queue.append((y,x))              
            count = count +1                
    
    
print(count)