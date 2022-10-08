n, k = map(int, input().split())


n100 = n%10*100
n10 = n%100-n%10
n1 = int(n/100)


k100 = k%10*100
k10 = k%100-k%10
k1 = int(k/100)



print(max(n100+n10+n1,k100+k10+k1 ))