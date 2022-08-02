import sys
from collections import deque
m,n,h = map(int,input().split()) # mn크기, h상자수
graph = []
queue = deque([])
 
for z in range(h):
    tmp = []
    for y in range(n):
        tmp.append(list(map(int,sys.stdin.readline().split())))
        for x in range(m):
            if tmp[y][x]==1:
                queue.append([z,y,x,1])
    graph.append(tmp)
    
    
dx = [1, 0 ,0 ,-1 ,0 ,0]
dy = [0 ,1 ,0 ,0 ,-1 ,0]
dz = [0 ,0 ,1 ,0 ,0 ,-1]


while(queue):
    z , y, x , time = queue.popleft();
    
    for nx , ny , nz in zip(dx , dy , dz):
        nx += x
        ny += y
        nz += z
        if 0<=nz< h and 0<=ny<n and 0<=nx<m :
            if graph[nz][ny][nx] == 0:
                queue.append([nz , ny , nx , time+1 ]);
                graph[nz][ny][nx] = time+1
                    
daytime = 0
for i in graph:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
        daytime = max(daytime,max(j))
print(daytime-1)
