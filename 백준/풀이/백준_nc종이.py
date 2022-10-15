from bisect import insort
import copy
paper = [7,3,-7,5,-3]
n =2

smax = - 9999999

def dfs (count , arr, n) :
    
    global smax
    if count == n :
        smax = max(smax , max(arr))
        return
    
    copyarr = copy.deepcopy(arr)
    temparr = [];
    
    temp = [False]*len(arr)
    for i in range(1,len(copyarr)) :
        arr = copy.deepcopy(copyarr)
        s =1
        while i+s-1 < len(arr) and i-s >=0 :
            arr[i+s-1] = arr[i+s-1] + arr[i-s]
            temp[i-s] = True
            s = s+1 
        for i in range(len(temp)) :
            if not temp[i] :
                temparr.append(arr[i])  
    
        temp = [False]*len(arr)  
        smax = max(smax , max(arr))   
        dfs(count +1 , temparr , n)
        temparr = []
        
            
 
dfs(0 , paper , 2)
print (smax)      
        
    