from collections import deque


cn = int(input())
carr = list(map(int, input().split()))
gn = int(input())
garr = list(map(int, input().split()))


a = sum(carr)

visite = [False] * (a+1);


q = deque()
list = deque()
for i in carr : 
    

    
    while q : 
        num = q.popleft()
        list.append(num)
        if not visite[abs(i- num)] :
            list.append(i-num)  
            visite[i-num] = True        
            
        if i+ num < len(visite) and  not visite[abs(i+ num)] :
            list.append(i+num)
            visite[i+num] = True
        
    q = list    
    list = deque()    
    q.append(i)
    visite[i] = True        
    
for i in garr :
    
    if i>= len(visite) or not visite[i] :
        print("N",end=' ')
       
    else :
        print("Y",end=' ')