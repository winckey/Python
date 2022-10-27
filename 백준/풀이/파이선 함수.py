def check4( a ) :
    
    a[0] = a[0] +2
    print(a[0] ) # 1
    return a

def check3( a ) :
       
    check4(a[:]) 
    print(a[0]) # 2  
    
    
check3( [1] ) # 3 1 



