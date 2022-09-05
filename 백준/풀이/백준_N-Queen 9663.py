import copy


def fillRow(copyRow , x, y) :
    
    global n 
    
    
    frow = copy.deepcopy(copyRow)
    for i in range (n) :
        frow[y][i] = 1
        frow[i][x] = 1
  
    nx = x
    ny = y
    while True :
        nx = nx+ 1
        ny = ny+ 1 
        if nx >= n or ny >= n :
            break;
        frow[ny][nx] = 1
        
    nx = x
    ny = y
    while True :
        nx = nx- 1
        ny = ny+ 1 
        if nx < 0  or ny >= n :
            break;
        frow[ny][nx] = 1
        
    nx = x
    ny = y    
    
    while True :
        nx = nx+ 1
        ny = ny- 1 
        if nx >= n or ny < 0 :
            break;
        frow[ny][nx] = 1    
        
    nx = x
    ny = y       
            
    while True :
        nx = nx- 1
        ny = ny- 1 
        if nx < 0 or ny < 0 :
            break;
        frow[ny][nx] = 1        
    
    return frow


def dfs(count , copyRow) :
    global ans
    global n 
    if count == n :
        ans =ans + 1
        return
    
    
    for i in range(n) :
        if copyRow[i][count] != 1 :
            
            dfs(count+1 ,fillRow(copyRow, count , i))            

def solution(n1):
    global n 
    answer = 0
    n = n1
    row = [[0] * n for i in range(n)]
    dfs( 0 , row)
    return answer

n = 0
ans = 0



solution(4)

print(ans)





