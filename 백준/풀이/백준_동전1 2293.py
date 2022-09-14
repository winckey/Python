from collections import deque
 
n , t = map(int, input().split())

arr = [0]*(100000+1)
arr2 = [0]*(100000+1)
coin =[]
for i in range(n) :
    num =int(input());
    coin.append(num);



for c in coin :
    arr[c]= arr[c] +1
    for i in range (t+1) :
        if i - c >= 0 :
            arr2[i] = arr[i]+arr2[i-c]
        else :
            arr2[i] = arr[i]
    arr = arr2
    arr2 = [0]*(100000+1)      
print(arr[t])              