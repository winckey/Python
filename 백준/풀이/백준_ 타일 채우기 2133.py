N = int(input())


dp = [1 , 0 , 3] 

sum = 1

for i in range( 3 , N+1) :
    
    if i % 2 == 0 :
        dp.append(dp[i-2]*3 + sum *2 ) 
        sum += dp[i-2]
    else : 
         dp.append(0) 

print(dp)