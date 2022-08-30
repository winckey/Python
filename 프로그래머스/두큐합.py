from collections import deque


def solution(queue1, queue2):
    
    deq1 = deque(queue1)
    deq2 = deque(queue2)
    
    lenDeq1 = len(deq1)
    lenDeq2 = len(deq2)
    
    
    count1 =0;
    count2 =0;
    
    sum1 = sum(deq1)
    sum2 = sum(deq2)
    while count1 < lenDeq1 or count2 < lenDeq2 :
        
        if sum1 == sum2 :    
            return count1+count2
        
        elif sum1 > sum2 :
            temp = deq1.popleft()
            sum1 -= temp
            deq2.append(temp);
            sum2 += temp
            count1 +=1
        
        elif sum1 < sum2 :
            temp = deq2.popleft()
            sum2 -= temp
            deq1.append(temp);
            sum1 += temp
            count2 +=1
            
            
    return -1