from collections import deque
 
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
 
 
def solution(m, n, picture):
    answer = [0, 0]
    visited = [[False] * n for _ in range(m)]
 
    def bfs(x, y):
        count = 1
        # 큐(Queue) 구현을 위해 deque 라이브러리 사용
        queue = deque([(x, y)])
        # 현재 노드를 방문 처리
        visited[x][y] = True
        color = picture[x][y]
        # 큐가 빌 때까지 반복
        while queue:
            # 큐에서 하나의 원소를 뽑아 출력
            x, y = queue.popleft()
            # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if -1 < nx < m and -1 < ny < n:
                    if not visited[nx][ny] and picture[nx][ny] == color:
                        queue.append((nx, ny))
                        visited[nx][ny] = True
                        count += 1
        answer[0] += 1
        answer[1] = max(answer[1], count)
 
    for i in range(m):
        for j in range(n):
            if not visited[i][j] and picture[i][j] != 0:
                bfs(i, j)
    return answer