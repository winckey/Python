import sys
from collections import deque


timeList = [sys.maxsize]*100001

def BFS(start , end):
    
    
    if(start == end):
        return 0

    queue = deque()
    queue.append(start)
    timeList[start] =0;
    time =0;

 
    while queue:

        target  = queue.popleft()
        time = timeList[target]


        for x in (target+1 , target-1):
            if(x>=0 and x<100001 and timeList[x] > time+1):
                queue.append(x)
                timeList[x] = time+1;
                
        if(target*2 < 100001 and timeList[target*2] > time):
            queue.append(target*2)
            timeList[target*2] = time;        

    return timeList[end]

input = sys.stdin.readline()

MAX = 100000
n,k = map(int,input.split())




print(BFS(n, k))