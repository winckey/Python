
    
    
dx = [1, 0 ,0 ,-1 ,0 ,0]
dy = [0 ,1 ,0 ,0 ,-1 ,0]
dz = [0 ,0 ,1 ,0 ,0 ,-1]


max = -1

x , y, z , time = 1, 1, 1, 1;
    
for nx , ny , nz in zip( list(map(lambda dx: dx + x  , dx)) , list(dy) , list(dz)) :

    print(nx  , ny , nz)
