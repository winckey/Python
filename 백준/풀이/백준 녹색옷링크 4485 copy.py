
from collections import deque
import heapq
import queue

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
tc = 0
while True:
    tc += 1
    n = int(input())
    if n == 0:
        break
    a = [list(map(int, input().split())) for _ in range(n)]
    temp = [[9999]*n for _ in range(n)]
    
    q = deque()
    q.append((0,0))
    temp[0][0] = a[0][0]
    while q :
      
      py , px = q.popleft()
         
      for i in range(4) :
        ny = py + dy[i]    
        nx = px + dx[i]

        if 0<= ny < n and 0<= nx < n :
          if a[ny][nx] + temp[py][px] < temp[ny][nx] : 
            temp[ny][nx] = a[ny][nx] + temp[py][px]
            q.append( (ny , nx ))

    print("Problem "+str(tc)+": "+str(temp[-1][-1]))
