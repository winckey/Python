# input 입력 받기
import math



# 소수 판별 함수


N = int(input())

arr =[]


a = [False, False] + [True] * (N-1)
arr = []

for i in range(2, N+1):
    if a[i]:
        arr.append(i)
        for j in range(2*i, N+1, i):
            a[j] = False
if len(arr) == 0 :
    print(0)
    exit(0)

num1 =0;
num2 =0;
sum = arr[num1];
count =0;
while num1 <= num2 :
    
    if sum == N :
        count += 1
    
    if sum > N :
        sum -= arr[num1]
        num1 +=1
        
        
    else :
        num2 +=1     
        if num2 < len(arr) :
            sum += arr[num2]    
        else :
            break;
        
        
        
print(count)
        
        
    