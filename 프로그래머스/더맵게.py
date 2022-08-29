from collections import deque
 

def solution(scoville, K):




    count =0
    while scoville[0] < K  and len(scoville) > 1:


        a= scoville.pop(0)
        b= scoville.pop(0)


        scoville.append(a+b*2)

        scoville.sort()

        count += 1

    if scoville[0] >= K :
        return count
    else :
        return -1


print(solution([1,2, 300] , 10))