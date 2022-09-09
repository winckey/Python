import collections
from copy import deepcopy


n, m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]


def reduce (graph2) :

    graph = deepcopy(graph2)
    
    for i in range(n) :
        for j in range(m) :
            if graph2[i][j] != 0 :
                for tx , ty in zip(dx , dy) :
                    if n > ty + i >=0 and m > tx + j >=0 and graph[ty + i][tx + j] == 0 :
                        if graph2[i][j] == 0 :
                            break;
                        graph2[i][j] = graph2[i][j]-1;

    return graph2
    
def bfs (graph) :
    
    visite = [[False] * m for _ in range(n) ]
    
    count = 0;
    queue = collections.deque()
    for i in range(n) :
        for j in range(m) :
            if graph[i][j] != 0 and not visite[i][j]:
                queue.append((i,j))
                visite[i][j] = True
                while queue :
                    y , x = queue.popleft()
                    for tx , ty in zip(dx , dy) :
                        ny = ty + y
                        nx = tx + x
                        if n > ny >=0 and m > nx >=0 and graph[ny][nx] != 0 and not visite[ny][nx]:
                            queue.append( (ny , nx) )
                            visite[ny][nx] = True
                count = count +1
    
    if count >= 2 :
        return True
    else : 
        return False
    
year = 0;    
    
while True :
    if bfs(graph) :
        print(year)
        break;
    
    graph = reduce(graph)
    year = year+1
        