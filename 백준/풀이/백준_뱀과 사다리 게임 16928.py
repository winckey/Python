from collections import deque
import queue
from xml.dom import minicompat


N , M= map(int, input().split())

arr = [ i for i in range(101)]
visite = [ False for i in range(101)]
for _ in range(N) :
    a , b= map(int,input().split())
    arr[a] = b

for _ in range(M) :
    a , b= map(int,input().split())
    arr[a] = b    


def game () :
    
    mincount =999999
    queue = deque()
    count =0
    queue.append((1 , count))
    

    while queue : 
        point , count= queue.popleft()

        for i in range(1,7) :
            if point+i <= 100 and not visite[arr[point+i]] :
                visite[point+i] = True
                queue.append((arr[point+i] , count+1)) 
            if point+i <= 100 and arr[point+i] == 100 :
                mincount = min(mincount , count+1)
                
    return mincount

print(game())      