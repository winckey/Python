import queue
import sys
from collections import deque
input = sys.stdin.readline()

MAX = 100000
n,k = map(int,input.split())


visited = list(range(100000));

timeList = list(range(100000));


def BFS(start , end):
    
    queue = queue();
    queue.append(start);
    print(queue);
    while queue:
        


