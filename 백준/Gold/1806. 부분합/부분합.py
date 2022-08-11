import sys

n, x = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

end = 0
start = 0

arrLen = 99999

numSum = arr[start]
while start <= end:
    # numSum = sum(arr[start:end+1]) # 3항연산자 min max sum 공부및 변수로 사용금지

    if numSum >= x:
        arrLen = min(end - start + 1, arrLen)
        numSum -= arr[start]
        start += 1


    elif numSum < x:
        end += 1
        if end >= n:
            break
        numSum += arr[end]

print(0 if  arrLen == 99999 else arrLen)
