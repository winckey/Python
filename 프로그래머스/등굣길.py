def solution(m, n, puddles):
    
    ndiv = 1000000007
    
    dp = [[0]* (m+1) for _ in range(n+1) ]
    puddle = [[False]* (m+1) for _ in range(n+1) ]
    
    for y , x in puddles :
        puddle[x][y] = True
        
        
        
    dp [1][1] = 1
    
    for i in range(1 , n+1) :
        for j in range(1 , m+1) :
            
            if puddle[i][j] :
                continue
            
            dp[i][j] += (dp[i-1][j] + dp[i][j-1]) % 1000000007
    
    answer = dp[n][m]
    print(dp)
    return answer





solution(4,	3  ,[[2, 2] ]	)
