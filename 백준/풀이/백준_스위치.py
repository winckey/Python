#1:17

import sys
from copy import deepcopy
n = int(input())
switch = list(map(int,input().split()))
student = [list(map(int,input().split())) for _ in range(int(input()))]

def onoff(arr,type,n):
    switch2 = deepcopy(arr)

    if type == 1:
        i = 1
        while i*(n+1) <= len(arr):
            if i*(n+1) <= len(arr):
                if switch2[i*(n+1)-1] == 0:
                    switch2[i*(n+1)-1] = 1
                    i += 1
                elif switch2[i*(n+1)-1] == 1:
                    switch2[i*(n+1)-1] = 0
                    i += 1
            else:
                break

    elif type == 2:
        if switch2[n] == 0:
            switch2[n] = 1
        elif switch2[n] == 1:
            switch2[n] = 0

        i = 1
        while n+i<len(arr):
            if 0<=n-i and n+i<len(arr):
                if arr[n-i] == arr[n+i]:
                    if switch2[n-i] == 0:
                        switch2[n-i] = 1
                        switch2[n+i] = 1
                        i += 1
                    elif switch2[n-i] == 1:
                        switch2[n-i] = 0
                        switch2[n+i] = 0
                        i += 1
                else: break
            else: break
    return switch2

for type, num in student:
    switch = onoff(switch,type,num-1)



for i in range(0, n, 20):    # 스위치의 상태를 1번 스위치에서 시작하여 마지막 스위치까지 한 줄에 20개씩 출력
    print(*switch[i:i+20])