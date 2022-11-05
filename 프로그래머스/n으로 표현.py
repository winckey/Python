def solution(N, number):
    
    dp = []
   
    
    dp.add(N)
    
    for cnt in range(2 , 9) : 
        setdp = set()
        setdp.add
        for x in dp : 
            setdp.add(x + N)
            setdp.add(x - N)
            setdp.add(x * N)
            setdp.add(x // N)

    
    
    answer = -1
    return answer


solution( 5 , 12)