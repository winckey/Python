

from collections import deque
import queue

maxNum =0
m = int(input())
graph =[]
for i in range(m):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] > maxNum:
            maxNum = graph[i][j] 
            
            
visited = [[False] * m for _ in range(m)]


queue = deque()





dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
year = 0

result =0

for h in range(maxNum):
    count =0 
    visited = [[False] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            if graph[i][j] > h and not visited[i][j] :
                visited[i][j] = True
                queue.append((i,j))
                while queue:
                    y , x = queue.popleft()
                    for ty , tx in zip(dy , dx) :
                            ny = y+ ty
                            nx = x+ tx
                            if m > ny >=0 and m > nx >= 0 and not visited[ny][nx] and graph[ny][nx] > h:
                                visited[ny][nx] = True
                                queue.append((ny,nx))              
                count = count +1                
    result = max(result  ,count)
    
print(result)