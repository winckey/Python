def solution(N, number):
    
    dp = set()
    
    dp.add(N)
    
    for cnt in range(2 , 9) : 
        for x in dp : 
            dp.add(x + N)
            dp.add(x - N)
            dp.add(x * N)
            dp.add(x // N)
            if number == x + N or number == x - N or number == x * N or number == x // N :
                return cnt 

    
    
    answer = -1
    return answer


solution( 5 , 12)