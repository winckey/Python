


n , m = map(int, input().split())


arr = list(map(int, input().split()))

count =0
for i in range(len(arr)) :
    sum =0;
    for j in range(i,len(arr)) :
        sum = sum + arr[j]
        if sum%m ==0 :
            count = count +1
            
            
print(count)        