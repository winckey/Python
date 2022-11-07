import sys
from collections import deque
sys.setrecursionlimit(100000)

n,k = map(int,input().split())
cnt = 0
visited = [0 for _ in range(100000)]

def bfs(v):
    global cnt
    queue = deque()
    queue.append((v,cnt))

    while queue:
        v,dep = queue.popleft()
        dv = [1,-1,v]

        if v == k:
            print(dep)
            return

        for nv in (v -1 , v+1 , v*2):
           
            if 0<=nv<100000 :
                visited[nv] = min (dep+1 , visited[nv])
                queue.append((nv,dep+1))

bfs(n)