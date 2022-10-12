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
    l2 = int(l/2)
    global b
    global w
    sumResult = arrSum(divpaper)
    
    if sumResult == l*l :
        b = b+1
        return 
    elif sumResult == 0 :
        w = w+ 1
        return    
    
    
    
    divpaper1 = []
    for i in range(l2) :

        divpaper1.append(divpaper[i][0:l2])

    divpaper2 = []
    for i in range(l2) :

        divpaper2.append(divpaper[i][l2:int(l)])

    divpaper3 = []
    for i in range(l2,l) :
  
        divpaper3.append(divpaper[i][0:l2])
        
  
    divpaper4 = []
    for i in range(l2 ,l) :
        divpaper4.append(divpaper[i][l2:int(l)])
              
    div (divpaper1 , l2)
    div (divpaper2 , l2)
    div (divpaper3 , l2)
    div (divpaper4 , l2)

div(paper , len(paper))    
    
print(b , w)      