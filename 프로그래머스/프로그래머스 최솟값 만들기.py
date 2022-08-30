
max =9999999

def solution(A,B):
    answer = 0

    visite = [[False]*len(A) for i in range(2)]

    dfs(0 , A , B , 0 , visite)

    return max

def dfs(count , A , B , lsum , visite) :
    
    
    global max
    
    if count == len(A)  :
        if lsum < max :
            max = lsum
        return 
    
    
    for i in range(len(A)) :
        if not visite[0][i] :
            visite[0][i] = True
            
            for j in range(len(B)):
                  if not visite[1][j] :
                    visite[1][j] = True
                    lsum += A[i]*B[j]
                    count +=1
                    dfs(count , A , B , lsum , visite)
                    count -=1
                    lsum -= A[i]*B[j]
                    visite[1][j] = False
                    
            visite[0][i] = False        
    
    
    
print(solution(		[4, 10, 1], [1, 9, 1] ))