

from dis import dis


n , bcost = map(int, input().split())


app= list(map(int, input().split()))

cost= list(map(int, input().split()))


visite = [False]* (bcost+1)
dist = [9999999] *(bcost+1)
dist[0] = 0

case = []
case.append(0)

for i in range(len(app)) :
    temp = []
    for c in case : 
        if c + app[i] <= bcost and dist[c + app[i]] > dist[c]+cost[i] :
            dist[c + app[i]] = dist[c]+cost[i]
    
            if not visite[c + app[i]] : 
                visite[c + app[i]] = True
                temp.append(c+app[i])     
                
    case.extend(temp)
    
print(dist[bcost])