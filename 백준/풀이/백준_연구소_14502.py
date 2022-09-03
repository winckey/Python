from collections import deque
import copy



def dfsWall(count ,graph ) : 
    if count == 3 :
        for i in range(len(graph)):
             for j in range(len(graph[0])):
                 if 2 == graph[i][j] : # 필요한 연산 수행
                     gqueue.append((i ,j)) 
        bfs(copy.deepcopy(graph))
        return

    for i in range(n) :
        for j in range(m) :
            if graph[i][j] ==0 :
                graph[i][j] =1
                dfsWall(count+1 , graph)
                graph[i][j] =0



def bfs (graph):

    while gqueue :
        y , x = gqueue.popleft()
        for nx , ny in zip(dx,dy) : 
            tx = x +nx
            ty = y +ny
            if tx > -1 and ty > -1 and ty < n and tx < m and graph[ty][tx] ==0 :
                graph[ty][tx] =2 
                gqueue.append((ty,tx))


    global max
    s = 0
    for  i in graph :
        s = s + i.count(0)
        
    if max < s :
        max = s
    return 

max = -1
n, m = map(int, input().split())
rgraph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
gqueue = deque()
for i in range(n):
    rgraph.append(list(map(int, input().split())))




dfsWall(0 , copy.deepcopy(rgraph))

print(max)











