# input 입력 받기
n = int(input())
solution = list(map(int, input().split(' ')))

# 정렬하기
solution.sort()

start = 0
end = n - 1 

min = 2e+9+1

num1 =0;
num2 =0;

while start < end :
    
    nsum = solution[start] + solution[end]
    if nsum == 0 : 
        print(solution[start], solution[end])
        exit(0)
    
    if abs(nsum) < min :
        min = abs(nsum)
        num1 = start
        num2 = end
    
    
    if  nsum < 0:
        start += 1
        

    else :
        end -= 1



print(solution[num1], solution[num2])