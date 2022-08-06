from audioop import reverse


def solution(levels):
    

    
    levels.sort(reverse=True)
    
    a = round(len(levels)/4)
    
    
    
    answer = levels[a-1];
    print(answer)
    return answer

solution([1,2,3,4,5,6,7,8,9])