from collections import deque
 

def solution(scoville, K):




    count =0
    while scoville[0] < K  and len(scoville) > 1:

        scoville.append(scoville.pop(0)+scoville.pop(0)*2)

        scoville.sort()

        count += 1

    if scoville[0] >= K :
        return count
    else :
        return -1


print(solution([1,2, 300] , 10))



def solution(scoville, k):
    mix_cnt = 0
   
    while scoville[0] < k:

        try:
            scoville.append(scoville.pop(0) + (scoville.pop(0) * 2))
        except IndexError:
            return -1
        scoville.sort()    
        mix_cnt += 1
 
    return mix_cnt