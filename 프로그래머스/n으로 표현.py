def solution(triangle):
    
    
    dp = [[-1]* (len(triangle)+1) for _ in range(len(triangle))]
    
    
    dp[0][1] = triangle[0][0]
    
    
    for i in range(1 , len(dp)) :
        for j in range(1, i+2) :
            dp[i][j] = max (dp[i-1][j-1] , dp[i-1][j]) + triangle[i][j-1]
    
    print(dp)
    answer = max ( map (max , dp ))
    return answer



solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])