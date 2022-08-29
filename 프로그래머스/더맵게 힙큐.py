from heapq import *
 

def solution(scoville, K):




    count =0
    heapify(scoville)
    while scoville[0] < K  and len(scoville) > 1:

        heappush( scoville,heappop(scoville)+heappop(scoville)*2)
        count += 1

    if scoville[0] >= K :
        return count
    else :
        return -1


print(solution([1,2, 300] , 10))

