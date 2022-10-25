import sys

case = int(input())
for _ in range(case) :
    n=int(input())
    arr =[0]+list(map(int,input().split()))
    
    dp = [[0]*(len(arr)) for i in range(len(arr)) ]
    ssum = [0 for _ in range(n+1)]
    for i in range (1 , len(ssum)) : 
        ssum[i] = ssum[i-1] + arr[i]

    for i in range (1 , len(dp) - 1) : 
        for j in range ( 1,  len(dp) - i) : 
            temp_min = sys.maxsize
            for k in range (i) : 
                temp_min = min( temp_min , dp[j][j+k] + dp[j+k+1][j+i])
            dp[j][j+i] = temp_min + ssum[j+i]-ssum[j-1]    

    print(dp[1][n])
    


           