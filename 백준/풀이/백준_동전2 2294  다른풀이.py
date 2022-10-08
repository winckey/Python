intmax = 999999

n, k = map(int, input().split())
c = [int(input()) for i in range(n)] # 코인의 종류
dp = [intmax for i in range(k+1)] # 사이즈 k+1만큼의 리스트 선언
dp[0] = 0 # 인덱스 0은 동전을 1개만 쓸 때의 경우의 수를 고려하기 위해 선언

for i in c:
    for j in range(i, k+1):
        if j-i >= 0:
            dp[j] = min(dp[j] ,dp[j - i] + 1)
            
if dp[k] == intmax :
    print(-1)       
else :         
    print(dp[k])