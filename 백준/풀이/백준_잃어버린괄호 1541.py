import sys
from unittest import result
input = sys.stdin.readline

s = input()

cnt = 0
num = []
f = []
temp = ""



for i in s:
    if i=='-' or i=='+':
        num.append(int(temp))
        f.append(i)
        temp = ""
    else :
        temp= temp+i
num.append(int(temp))

 
temp = 0 
result =0
for i in range(len(num)-1 , 0 , -1) :
    temp += num[i]
    if (f[i-1]) == '-' :
        result -= temp ;
        temp =0

result += temp        
result += num[0]        
print(result)