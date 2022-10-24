n,m = map(int, input().split())
stuff = [[0,0]]

for _ in range(n):
    stuff.append(list(map(int, input().split())))


dp = [[0]*(m+1) for i in range(n+1)]  


for i in range( 1, n+1 ) :
    for j in range(1 , m+1) : 
        w,v  =stuff[i]
        
        if j < w :
            dp[i][j] = dp[i-1][j]
        else :
            dp[i][j] = max(dp[i-1][j] , dp[i-1][j-w] + v)
            
print (dp[n][m])            