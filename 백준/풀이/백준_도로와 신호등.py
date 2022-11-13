import sys
from copy import deepcopy
input = sys.stdin.readline

N,L = map(int, input().split())
sinho = [list(map(int, input().split())) for _ in range(N)]
location = 0
min = -1
sumRG = 0

while location <= L :
    if len(sinho) > 0:
        if location == sinho[0][0]:
            for i in range(1,3):
                sumRG += sinho[0][i]
                if min <= sumRG:
                    if i == 1: #Red
                        min = sumRG
                        sumRG = 0
                        del sinho[0]
                        break
                    elif i == 2: #Green
                        sumRG = 0
                        del sinho[0]
                        break
        else:
            location += 1
            min += 1
    else:
        location += 1
        min += 1
print(min-1)