N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)] 

w =0
b =0


    
def arrSum (arr) :
    asum = 0;
    for i in arr :
        asum = asum + sum(i)
            
    return asum  

def div (divpaper , l) :
    
    
    if arrSum(divpaper) == l*l :
        b = b+1
        return 
    elif arrSum(divpaper) == 0 :
        w = w+ 0
        return    
    
    
    
    divpaper1 = []
    for i in range(int(l/2)) :
        divpaper1.append([])
        divpaper1[i].append(divpaper[i][0:int(l/2)])

    divpaper2 = []
    for i in range(int(l/2)) :
        divpaper2.append([])
        divpaper2[i].append(divpaper[i][int(l/2):int(l)])

    divpaper3 = []
    for i in range(int(l/2),l) :
        divpaper3.append([])
        divpaper3[i-int(l/2)].append(divpaper[i][0:int(l/2)])
        
  
    divpaper4 = []
    for i in range(int(l/2) ,l) :
        divpaper4.append([])
        divpaper4[i-int(l/2)].append(divpaper[i][int(l/2):int(l)])
              
    div (divpaper1 , l/2)
    div (divpaper2 , l/2)
    div (divpaper3 , l/2)
    div (divpaper4 , l/2)

div(paper , len(paper))    
    
print(b , w)      