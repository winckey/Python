import queue
import sys
from collections import deque
from typing import Deque

n = int(input())
m = int(input())
graph = [[]*n for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = []
queue = deque()
queue.append(1)
count =0;

while queue :
    target = queue.pop()
    
    if target not in visited :
        count += 1
        for temp in graph[target] :
            queue.append(temp)
        visited.append(target)

print(count-1)