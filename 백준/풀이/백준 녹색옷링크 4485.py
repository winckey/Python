
import heapq

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

tc = 0
while True:
    tc += 1
    n = int(input())
    if n == 0:
        break
    a = [list(map(int, input().split())) for _ in range(n)]
    
    q = []
    
    heapq.heappush(q , (a[0][0] , [0,0]))
    
    
    while q :
      
      dist , point = heapq.heappop(q)
      
      if point[0] == n-1 and point[1] ==n-1 :
        print("Problem "+str(tc)+": "+str(dist))
        break;
          
      for i in range(4) :
        ny = point[0] + dy[i]    
        nx = point[1] + dx[i]

        if 0<= ny < n and 0<= nx < n : 
            heapq.heappush(q , (dist + a[ny][nx] , [ny,nx]))
      