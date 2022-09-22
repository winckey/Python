n, k = map(int, input().split())
dp = [999999 for i in range(100000+1)] # 사이즈 k+1만큼의 리스트 선언
 # 인덱스 0은 동전을 1개만 쓸 때의 경우의 수를 고려하기 위해 선언

for _ in range(n) :
    num = int(input())
    dp[num] = 1  


for i in range(k+1):
    s = i-1
    e = 1
    
    while s >= e :
        dp[i] = min(dp[i] , dp[s]+dp[e])
        s = s-1
        e = e+1
        
if dp[k] == 999999 :
    print(-1)
else       :
    print(dp[k])