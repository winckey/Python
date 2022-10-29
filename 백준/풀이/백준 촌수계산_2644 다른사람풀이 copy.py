import sys
## 입력 받기



n = int(sys.stdin.readline())

a,b = map(int,sys.stdin.readline().split())

m = int(sys.stdin.readline())

amap = [[] for i in range(n+1)]
visited = []

for i in range(m) :
    y , x = map (int , input().split())
    amap[y].append(x)
    amap[x].append(y)
    
    
def dfs (amap , end , start , count , visited) :
  
  
  if end == start :
      print(count)
      return  

  for i in amap[start] :
      if i not in visited :
       
        temp = visited[:]  
        temp.append(i)
        dfs (amap , end , i , count + 1 , temp)
  

     
    
dfs(amap , a , b   , 0 , visited)      
    






































# visited = [False] * (n+1)
# # 2차원 배열
# graph = [[] for _ in range(n+1)]
# result = []

# # 배열에 노드의 값들 넣기
# for _ in range(m):
#   x, y = map(int,sys.stdin.readline().split())
#   graph[x].append(y)
#   graph[y].append(x)

# # DFS 구현
# def dfs(v,cnt):
#   cnt += 1
#   visited[v] = True
#   # 찾아야 하는 사람의 번호를 방문했을 때
#   if v == b:
#     result.append(cnt)
#   for i in graph[v]:
#     if not visited[i]:
#       dfs(i,cnt)

# dfs(a,0)

# ## 출력
# if len(result) == 0:
#   print(-1)
# else:
#   print(result[0]-1)