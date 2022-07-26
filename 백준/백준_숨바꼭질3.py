import queue
import re
import sys
from collections import deque

visited = [False]*100001
timeList = [0]*100001

def BFS(start , end):

    if(start == end):
        return 0

    queue = deque()
    queue.append(start)
    time =0;
    visited[start] = True;
    while queue:

        target  = queue.popleft()
        time = timeList[target]
        
        if(target+1 <= 100000 and not visited[target +1]):
          
            if(target+1 == end):
                return time+1;
            queue.append(target+1)
            timeList[target+1] =time + 1
            visited[target+1] = True
            
        if(target != 0 and not visited[target -1]):
            if(target-1 == end):
                return time+1
            queue.append(target-1)
            timeList[target-1] =time + 1
            visited[target-1] = True
                    
        if(target*2 <= 100000 and not visited[target *2]):
            if(target*2 == end):
                return time
            queue.append(target*2)
            timeList[target*2] =time
            visited[target*2] = True

        
        


input = sys.stdin.readline()

MAX = 100000
n,k = map(int,input.split())




print(BFS(n, k))

