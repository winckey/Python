def solution(n):
    i =1
    while format(n, 'b').count('1') != format(n+i ,'b').count('1') :
            i = i +1
            
            
    answer = 0
    return n+i

print(solution(23))


